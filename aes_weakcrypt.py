from Crypto.Cipher import AES
import sys
import binascii
from ctypes import c_uint32
from struct import *

# keyfile = open('aes_key.hex','r')
# iv = open('aes_iv.hex', 'r')
# plaintext = open('aes_plaintext.txt', 'w')
cipher = open('aes_weak_ciphertext.hex', 'r')
# "00000000000000000000000000000000"
hexcipher = cipher.read()
key = "00000000000000000000000000000000"


for i in range(0,32):
	mode = AES.MODE_CBC

	decrypter = AES.new(pack('qqqq', 0,0,0,i), mode)

	plaintextout = decrypter.decrypt(binascii.unhexlify(hexcipher))


	print "key num: "
	print i
	print "key:"
	print pack('qqqq', 0,0,0,i)
	print "text: "
	print plaintextout

# print plaintextout

# plaintext.write(plaintextout)

# keyfile.close()
# iv.close()
# plaintext.close()
cipher.close()