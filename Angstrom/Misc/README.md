[AngstromCTF](https://2020.angstromctf.com/challenges) - Misc
===============

CHALLENGES
----------------------

3. [ ws1 ](#ws1)
4. [ clam clam clam ](#clam)
5. [ ws2 ](#ws2)
9. [ Shifter ](#shifter)
10. [ ws3 ](#ws3)
12. [ Noisy ](#noisy)



<a name="ws1"></a>
## 3. ws1 (30 points)

**Challenge description**

Find my password from this recording (:

**Solution**

"ws1" is a reference to Wireshark.
The attached recording.pcapng can be opened with Wireshark to see the recording of the internet traffic. Manually looking trough the data showed the flag pretty quick.

Flag: actf{wireshark_isn't_so_bad_huh-a9d8g99ikdf}


<a name="clam"></a>
## 4. clam clam clam (70 points)

**Challenge description**

clam clam clam clam clam clam clam clam clam `nc misc.2020.chall.actf.co 20204` clam clam clam clam clam clam

**Hint**

`U+000D`

**Solution**

Using netcat to connect to the port results in a spam of `c{malc_malc_malc_malc_malc}\nclam{clam_clam_clam_clam_clam}\n`. I used the python script clam.py to process the incoming spam better.  When scrolling trough the spam the text `type "clamclam" for salvation` showed up, I guess one could automate to recognize other characters than clam{}/n_.
Typing `clamclam` in the terminal is no easy feat with the spam going on. With python this is easily done (don't forget to send the `/n`!).

Flag: actf{cl4m_is_my_f4v0rite_ctfer_in_th3_w0rld}

<a name="ws2"></a>
## 5. ws2 (80 points)

**Challenge description**

No ascii, not problem :)

recording.pcapng

**Hint**

` What did I send? `

**Solution**

Second part of the wireshark challenge. This time an image shows up as being uploaded (line no 64). The image can be saved by going to File -> Export objects -> HTTP.

The file isn't recognized as an image file because of a WebKitFormBoundary header. After deleting this header (first 4 lines and the last line) the image shows up correctly:

![img/ws2.png](img/ws2.png)

Flag: actf{ok_to_b0r0s-4809813}

<a name="shifter"></a>
## 9. Shifter (160 points)

**Challenge Desciption**

What a strange challenge...

It'll be no problem for you, of course!

`nc misc.2020.chall.actf.co 20300`

**Hint**

`Do you really need to calculate all those numbers?`

**Solution**

The port returns a series of 50 challenges like:

```
Solve 50 of these epic problems in a row to prove you are a master crypto man like Aplet123!
You'll be given a number n and also a plaintext p.
Caesar shift `p` with the nth Fibonacci number.
n < 50, p is completely uppercase and alphabetic, len(p) < 50
You have 60 seconds!
--------------------
Shift DXWREJZUFLJWVB by n=6
```
I made the script shifter.py actually calculate the fibonacci number and encrypts the plaintext with the ceasar cypher and the calculated shift. Time doesnt seem restricted. When time is more restricted and the n is limited like this I could also have googled or calculated the 50 terms.

Flag: actf{h0p3_y0u_us3d_th3_f0rmu14-1985098}


<a name="ws2"></a>
## 10. ws3 (180 points)

**Challenge description**

What the... record.pcapng

**Hint**

Did I send something? Or...

**Solution**

Open the record.pcapng with wireshark and export all http objects.
Binwalk the biggest file and export it with:

`binwalk -e git-receive-pack`

To get the image:

![img/ws3.png](img/ws3.png)

Flag: actf{git_good_git_wireshark-123323}

<a name="noisy"></a>
## 12. Noisy (240 points)

**Challenge description**

My furrier friend tried to send me a morse code message about some new furs, but he was using a noisy connection. I think he repeated it a few times but I still can't tell what he said, could you figure out what he was trying to tell me? Here's the code he used.

(the flag is not in the actf{} format, it's all lowercase, 1 repetition only)

**Hint**

The code that was used to generate the transmission is included

**Solution**

The downloaded transmission is a list of 28800 floats. The code that was used to generate it used morse code and converted it to 0's and 1's. For short, 10 1's and 10 0's, for long 20 1's and 10 0's and for space 30 0's. 

```
import numpy as np
from random import gauss
morse = REDACTED
repeats = REDACTED
pointed = []
for c in morse:
    if c == ".":
        pointed.extend([1 for x in range(10)])
    if c == "-":
        pointed.extend([1 for x in range(20)])
    if c == " ":
        pointed.extend([0 for x in range(20)])
    pointed.extend([0 for x in range(10)])

with open("points.txt", "w") as f:
    for _ in range(repeats):
        signal = pointed
        output = []
        for x, bit in enumerate(signal):
            output.append(bit + gauss(0,2))

        signal = list(np.array(output) - .5)
        f.write('\n'.join([str(x) for x in signal])+"\n")
f.close()
```

When the morse code has been transformed to ones and zeros the list gets scrambled with a gaussian distribution with the mean of 0 and a standard deviation of 2. They substract 0.5 from these scrambled floats and write that to a list.

They note that only the flag is being transmitted over and over. We can use that to see if a certain spacing between the bits shows a similat pattern to 10 * ones and 30 * zeros.

The python script noisy.py checks for different message lengths. With each message length the median or mean can be calculated (after adding the 0.5) over all the bits in their position  to approach the unscrambled bit. Using steps of 10 because the bits follow this pattern. A check on the before mentioned patterns returned 7 possible message lengths for me. 

Message length of 960 bits:

```
111111111100000000-100111111111111111111100000100000-100000-100000000000000000000001111111111111111111100000000001111111111000000001-1000000000000000000000000000000111111111111111111110000000000111111111111111111110000000000111111011111111111110000000000000000000-1000000000000000000001111211111000000000011111111110000000000000000000000000000000000000000111111011100000000001111111111000000000011111111110000000000000000000000000000000000-100000111111111111111111110000000000111111111100000000001111111111111111110100000000001111111211111111111100000000000000000000000100000000000000001111111111111111111100000000-1011111111210000000000000000100000-1000000000000000001111111111111111111100000000001111112111111111121100000000001111111111111111111100000000000000000000000000000000000-1000011111121110000000000111111111100-1000000000000000000000000000000000000011111111110000000000111111111100000000001111111111000000000000000000000000000000000000000011111111110000000000
```

The median wasn't able to fully restore the data, with a bit of manual cleanup:

```
111111111100000000001111111111111111111100000000000000000000000000000000000000001111111111111111111100000000001111111111000000000000000000000000000000000000000011111111111111111111000000000011111111111111111111000000000011111111111111111111000000000000000000000000000000000000000011111111110000000000111111111100000000000000000000000000000000000000001111111111000000000011111111110000000000111111111100000000000000000000000000000000000000001111111111111111111100000000001111111111000000000011111111111111111111000000000011111111111111111111000000000000000000000000000000000000000011111111111111111111000000000011111111110000000000000000000000000000000000000000111111111111111111110000000000111111111111111111110000000000111111111111111111110000000000000000000000000000000000000000111111111100000000001111111111000000000000000000000000000000000000000011111111110000000000111111111100000000001111111111000000000000000000000000000000000000000011111111110000000000
```

Now to translate to morsecode (think about order of replacing)

```
short = (10*'1')+(10*'0')
long = (20*'1')+(10*'0')
space = (30*'0')

message2 = message.replace(long, '-')
message2 = message2.replace(short, '.')
message2 = message2.replace(space, ' ')
```

gives the morse code message:

```
.- -. --- .. ... -.-- -. --- .. ... .
```

For this I used this [online morse code translator](https://morsecode.world/international/translator.html) to get the flag:

Flag: anoisynoise
