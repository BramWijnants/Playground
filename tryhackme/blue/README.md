[Blue](https://tryhackme.com/room/blue)
===============

Tasks
----------------------

1. [ Recon ](#recon)
2. [ Gain access ](#access)
3. [ Escalate ](#escalate)
4. [ Cracking ](#cracking)
5. [ Find flags! ](#flags)

<a name="recon"></a>
## 1. Recon

```
IP=XXX
```
Some nmap scans to check vulnerabilities

```
nmap -sV -vv -Pn --script vuln $IP
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

<a name="access"></a>
## 2. Gain access


