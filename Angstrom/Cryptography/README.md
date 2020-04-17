[AngstromCTF](https://2020.angstromctf.com/challenges) - Cryptography
===============

CHALLENGES
----------------------

1. [ Keysar ](#Keysar)


<a name="Keysar"></a>
## 1. Keysar (40 points)

**Challenge description**

Hey! My friend sent me a message... He said encrypted it with the key ANGSTROMCTF.

He mumbled what cipher he used, but I think I have a clue.

Gotta go though, I have history homework!!

agqr{yue_stdcgciup_padas}

**Hint**

`Keyed caesar, does that even exist??`

**Solution**

Name hints towards the caesar cipher but the caesar cipher does not need a key. Apparently there is a [Keyed Caesar cipher](http://rumkin.com/tools/cipher/caesar-keyed.php) which puts the key infront of the alphabet after the shift of the letters. Using the online tool the flag can easily be found (shift of 0).

Flag: actf{yum_delicious_salad}

