[Vulnersity](https://tryhackme.com/room/vulnversity)
===============

Tasks
----------------------

1. [ Deploy the machine ](#deploy)
2. [ Reconnaissance ](#reconnaissance)
3. [ Locating directories using GoBuster ](#gobuster)
4. [ compromise webserver ](#compromise)
5. [ Privelege Escalation ](#privesc)

<a name="deploy"></a>
## 1. Deploy the machine

```
IP=XXX
```

<a name="reconnaissance"></a>
## 2. Reconnaissance

Check which versions are running:

```
nmap -sV $IP
```

#2 How many ports are open?

```
6
```

#3 What version of the squid proxy is running on the machine?

```
3.5.12
```

#4 How many ports will nmap scan if the flag -p-400 was used?

```
400
```

#5 Using the nmap flag -n what will it not resolve?

```
DNS
```

#6 What is the most likely operating system this machine is running?

```
Ubuntu
```

#7 What port is the web server running on?
```
3333
```

<a name="gobuster"></a>
## 3. Locating directories using GoBuster

```
gobuster -u http://$IP:3333 -w /usr/share/wordlists/common.txt
```

#2 What is the directory that has an upload form page?

```
/internal/
```

<a name="compromise"></a>
## 4. Compromise the webserver


#1. Try upload a few file types to the server, what common extension seems to be blocked?
```
.php
```

#2. Check allowed extensions, what extension is allowed?

I used the python script check_extensions.py for this instead of BurpSuite

```
.phtml
```

#tty upgrade elevation techniques](http://netsec.ws/?p=337) 

Clean alternative without python:

```
/usr/bin/script -qC /bin/bash /dev/null
```
Go out of netcat session
```
stty raw -echo
```
Go in netcat session again
```
nc -lnvp PORT
export TERM=xterm
```

#5 What user was running the web server?

```
bill
```
