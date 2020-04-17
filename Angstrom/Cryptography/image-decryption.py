#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import array
import PIL

enc_flag = PIL.Image.open("enc.png")
img = array(enc_flag)

key = [41, 37, 23]

translate_dict_list = [{},{},{}]

# loop trough all color possibilities and build a dictionary of
# encoded values
for color in range(0, 256):
    translate_dict_list[0][color*41%251] = color
    translate_dict_list[1][color*37%251] = color
    translate_dict_list[2][color*23%251] = color

a, b, c = img.shape
    
for x in range (0, a):
    for y in range (0, b):
        pixel = img[x, y]
        for i in range(0,3):
            pixel[i] = translate_dict_list[i][pixel[i]]
        img[x][y] = pixel

enc = PIL.Image.fromarray(img)
enc.save('dec.png')
