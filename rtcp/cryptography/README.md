RiceTeaCatPanda - Cryptography
===============

HOOOOOOOOOOMEEEEEE RUNNNNNNNNNNNNN!!!!! (50 points)
-----------------------

**Challenge**

AND JAKE IS ROUNDING THE BASES \
HE PASSES BASE 32!!! \
HE ROUNDS BASE 64!!!!!!! \\
WE'RE WITNESSING A MIRACLE!!!!!!!!!!!!!

Just one more base to go ;D

**Hint**

```
Ecbf1HZ_kd8jR5K?[";(7;aJp?[4>J?Slk3<+n'pF]W^,F>._lB/=r
```

**Solution**

Hint is ['Base85'](https://en.wikipedia.org/wiki/Ascii85) (also named Ascii85) encoded. 
Decode either with Python (see home_run.py - using the base64 python package) or use online tools like ['cryptii'](https://cryptii.com/).

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

The secret consists of 32 hexadecimal digits which indicates a 128-bit (16-byte) ['MD5'](https://en.wikipedia.org/wiki/MD5) hash.
A lot of MD5 hashes (including this one) can be decrypted with ['online tools'](https://www.md5online.org/md5-decrypt.html).

Flag: rtcp{chocolate_mmm}
