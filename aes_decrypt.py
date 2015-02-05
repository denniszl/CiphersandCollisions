from Crypto.Cipher import AES
import sys
import binascii

keyfile = open('aes_key.hex','r')
cipher = open('aes_ciphertext.hex', 'r')
iv = open('aes_iv.hex', 'r')
plaintext = open('aes_plaintext.txt', 'w')

#Convert the hex files into binary.
hexkey = keyfile.read()
intkey = int(hexkey, 16)
# print hexkey
# print intkey

hexcipher = cipher.read()
intcipher = int(hexcipher, 16)
#print intcipher

hexiv = iv.read()
intiv = int(hexiv, 16)
# print intiv
# print sys.getsizeof(intiv)

# theiv = binascii.unhexlify("6e8c712be648a2f8b2c99464b03f66e9")
# thekey = binascii.unhexlify("f0f187646513ae039bc8b0b3bc2fb8e768d2dec005c1dd02403e9b4c0490dfc0")
theiv = binascii.unhexlify(hexiv)
thekey = binascii.unhexlify(hexkey)

mode = AES.MODE_CBC

decrypter = AES.new(str(thekey), mode, str(theiv))
plaintextout = decrypter.decrypt(binascii.unhexlify(hexcipher))

# print plaintextout

plaintext.write(plaintextout)

keyfile.close()
cipher.close()
iv.close()
plaintext.close()