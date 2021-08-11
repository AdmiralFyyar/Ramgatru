from Encrypt_04 import *
text = str(input("text:\n")); threads = int(input("threads:  "))
keys = []
for index in range(0, threads):
	KeyIndex = "Key" + str(index) + ":  "
	keys.append(float(input(KeyIndex)))
Encrypt(text, keys, int(input("RandKey:  ")), 0, threads)
