from Encrypt_04 import *
Kurwa = Semiconductor(6, ["か", "け", "ね", "ぬ", "が", "ず"])
value0 = Kurwa.Encode(int(input("value:  ")))
value1 = Kurwa.Decode(value0)
print("6: ", value0, value1)
