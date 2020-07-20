[Metasploit](https://tryhackme.com/room/rpmetasploit)
===============

Tasks
----------------------

1. [ Initializing... ](#initializing)
5. [ Move that shell! ](#revshell)

<a name="initializing"></a>
## 1. Initializing...

```
IP=XXX

msfdb init # initialize new metasploit database (if needed)

msfconsole # open metasploit console

db_status # check connection with database
```

<a name="revshell"></a>
## 5. Move that shell!

nmap with metasploit, can also be combined with stuff like -sC, -sV, -oN. Commands as hosts, services and vulns now are updated

```

db_nmap -sV BOX-IP 

search multi/handler # easy search function

use 6 # select exploit based on search results

```

after using the exploit migrate to another process with `migrate`
