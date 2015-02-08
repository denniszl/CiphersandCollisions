from Crypto.Cipher import AES
import sys
import binascii
from ctypes import c_uint32
from struct import *

# keyfile = open('aes_key.hex','r')
# iv = open('aes_iv.hex', 'r')
# plaintext = open('aes_plaintext.txt', 'w')
cipher = open('aes_weak_ciphertext.hex', 'r')
outfile = open('wat.txt', 'w')
# "00000000000000000000000000000000"
hexcipher = cipher.read()
key = "00000000000000000000000000000000"


for i in range(0,32):
	mode = AES.MODE_CBC
	# print binascii.hexlify(pack('>qq', 0,i))
	# decrypter = AES.new(binascii.hexlify(pack('qqqq', 0,0,0,i)), mode)
	decrypter = AES.new((pack('>qqqq', 0,0,0,i)), mode)

	plaintextout = decrypter.decrypt(binascii.unhexlify(hexcipher))


	print "key num: "
	outfile.write("key num:")
	outfile.write("\n")
	print i
	outfile.write(str(i))
	outfile.write("\n")
	print "key:"
	outfile.write("key:")
	outfile.write("\n")
	print pack('>qqqq', 0,0,0,i)
	outfile.write(binascii.hexlify(pack('>qq', 0,i)))
	outfile.write("\n")
	print "text: "
 	outfile.write("text:")
 	outfile.write("\n")
	print plaintextout
	outfile.write(plaintextout)
	outfile.write("\n")

# print plaintextout

# plaintext.write(plaintextout)

# keyfile.close()
# iv.close()
# plaintext.close()
# outfile.close()
cipher.close()
