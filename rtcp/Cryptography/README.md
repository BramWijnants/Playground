[RiceTeaCatPanda](https://riceteacatpanda.wtf/challenges) - Cryptography
===============

HOOOOOOOOOOMEEEEEE RUNNNNNNNNNNNNN!!!!! (50 points)
-----------------------

**Challenge**

AND JAKE IS ROUNDING THE BASES \
HE PASSES BASE 32!!! \
HE ROUNDS BASE 64!!!!!!! \
WE'RE WITNESSING A MIRACLE!!!!!!!!!!!!!

Just one more base to go ;D

**Hint**

```
Ecbf1HZ_kd8jR5K?[";(7;aJp?[4>J?Slk3<+n'pF]W^,F>._lB/=r
```

**Solution**

The flag is [Base85](https://en.wikipedia.org/wiki/Ascii85) (also named Ascii85) encoded. 
Decode either with Python (see home_run.py - using the base64 python package) or use an online tool like [cryptii](https://cryptii.com/).

Flag: rtcp{uH_JAk3_w3REn't_y0u_4t_Th3_uWust0r4g3}

Don't Give The GIANt a COOKie (100 points)
-----------------------

**Challenge**

It was just a typical day in the bakery for Delphine. She was preparing her famous chocolate cake, when all of a sudden a GIANt burst through the doors of her establishment and demanded a cookie. Being the strong-willed girl she was, Delphine refused and promptly threw her rolling pin at the GIANt. Doing what any sensible being would do when faced with projectiles, the GIANt let out a shriek and ran out of the shop. Delphine smiled to herself, it was another day well done.

But oh? What's this? It seems the GIANt dropped this behind while he was screaming and scrambling out of the shop.

```
69acad26c0b7fa29d2df023b4744bf07
```

**Hint**

This challenge still follows typical flag format, just wrap your answer with rtcp{answer_here}.

Non-case sensitive.

**Solution**

The secret consists of 32 hexadecimal digits which indicates a 128-bit (16-byte) [MD5](https://en.wikipedia.org/wiki/MD5) hash. Alot of MD5 hashes (including this one) can be decrypted with [online decoders](https://www.md5online.org/md5-decrypt.html). 


Flag: `rtcp{chocolate_mmm}`

15 (100 points)
--------------------------

**Challenge**
```
Lhzdwt eceowwl: Dhtnwt Pcln Eaao Qwoohvw

Okw qsyo okcln bah'i fslo cl baht Dhtnwt Pcln dhtnwt cy yazwalw'y eaao ehlnhy. Dho sy co ohtly aho, okso zcnko dw fkso bah nwo. S 4vksllwt hmqasiwi s mkaoa slalbzahyqb oa okw ycow ykafvsycln kcy ewwo cl s mqsyocv dcl ae qwoohvw, fcok okw yosowzwlo: "Okcy cy okw qwoohvw bah wso so Dhtnwt Pcln." Sizcoowiqb, kw ksi ykawy al. Dho okso'y wgwl fatyw.

Okw mayo fwlo qcgw so 11:38 MZ al Xhqb 16, sli s zwtw ofwlob zclhowy qsowt, okw Dhtnwt Pcln cl rhwyocal fsy sqwtowi oa okw tanhw wzmqabww. So qwsyo, C kamw kw'y tanhw. Kaf ici co ksmmwl? Fwqq, okw DP wzmqabww ksil'o twzagwi okw WJCE isos etaz okw hmqasiwi mkaoa, fkcvk yhnnwyowi okw vhqmtco fsy yazwfkwtw cl Zsbecwqi Kwcnkoy, Akca. Okcy fsy so 11:47. Oktww zclhowy qsowt so 11:50, okw Dhtnwt Pcln dtslvk siitwyy fsy mayowi fcok fcykwy ae ksmmb hlwzmqabzwlo. Ecgw zclhowy qsowt, okw lwfy yosocal fsy valosvowi db slaokwt 4vksllwt. Sli oktww zclhowy qsowt, so 11:58, s qclp fsy mayowi: DP'y "Owqq hy sdaho hy" alqclw eathz. Okw eaao mkaoa, aokwtfcyw plafl sy wjkcdco S, fsy soosvkwi. Vqwgwqsli Yvwlw Zsnsuclw valosvowi okw DP cl rhwyocal okw lwjo isb. Fkwl rhwyocalwi, okw dtwspesyo ykceo zslsnwt ysci "Ak, C plaf fka okso cy. Kw'y nwoocln ectwi." Zbyowtb yaqgwi, db 4vksl. Laf fw vsl sqq na dsvp oa wsocln aht esyo eaai cl mwsvw.

tovm{v4T3Ehq_f1oK_3J1e_i4O4}
```
Challenge Author: Jess (the other one)/J

**Solution**

The challenge text seems to have the spaces in the right place but the characters seem translated. This text is written with a substitution cipher. With this kind of cipher more text than the flag alone is needed to decrypt it. [Guballa](https://www.guballa.de/substitution-solver) can be used to decode this substitution cipher and supports mulitple languages. It gives the decrypted text and the used encryption key:

```
abcdefghijklmnopqrstuvwxyz     This clear text ...
sdviwenkcxpqzlamrtyohgfjbu     ... maps to this cipher text
```

[Quipquip](https://quipqiup.com/) is another tool to solve these substitution ciphers and has an input field for clues such as `tovm=rtcp`. This solver had more difficulties with uppercase characters, luckily the flag submissions for this ctf are case insensitive.

Flag: `rtcp{c4r3ful_w1th_3x1f_d4t4}`

notice me senpai (100 points)
---------------------------

**Challenge**

uwu...senpai placed this note on my desk before class but i cant wead what it says!!!!!! can you hewp me????????? uwu tysm

`tlyrc_o_0pnvhu}{137rmi__i_omwm`

Challenge Author: Jess (the other one)/J

**Solution**

The characters of the flag are scrambled in their order but with the . Using [Railfence]('http://rumkin.com/tools/cipher/railfence.php') the flag can be decreypted with 6 rails and an offset of 9. 

Flag: `rtcp{im_1n_lov3_wi7h_y0ur_mom}`

Their are different ciphers which scamble characters this way. Trying the different tools mentioned in [John Hammonds ctf-katana](http://rumkin.com/tools/cipher/railfence.php) would be a great start for these kind of encryptions.

To be continued...
---------------------------