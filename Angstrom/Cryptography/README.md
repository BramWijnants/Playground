[AngstromCTF](https://2020.angstromctf.com/challenges) - Cryptography
===============

CHALLENGES
----------------------

1. [ Keysar ](#Keysar)
3. [ Wacko Images ](#wacko)

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

<a name="wacko"></a>
## 3. Wacko Images (90 points)

**Challenge description**

How to make hiding stuff a e s t h e t i c? And can you make it normal again? enc.png image-encryption.py

The flag is `actf{x#xx#xx_xx#xxx}` where `x` represents any lowercase letter and `#` represents any one digit number.

**Solution**

![img/enc.png](img/enc.png)


`pixel[i] = pixel[i] * key[i] % 251`