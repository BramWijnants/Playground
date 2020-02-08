import base64

hint = b"""Ecbf1HZ_kd8jR5K?[";(7;aJp?[4>J?Slk3<+n'pF]W^,F>._lB/=r"""

#data is base85 encoded
#decoding base85
hint_decoded_bytes = base64.a85decode(hint)

#bytes to string
flag = hint_decoded_bytes.decode('utf-8')

print(flag)
