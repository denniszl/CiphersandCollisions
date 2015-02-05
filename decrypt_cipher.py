keyfile = open('sub_key.txt','r')
ciphertextfile = open('sub_ciphertext.txt', 'r')
outputfile = open('sub_plaintext.txt', 'w')

key = keyfile.readline()

#for chars in range(length(key)):

keyarr = []

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for chars in key:
	keyarr.append(chars)

ciphertext = ciphertextfile.read()

plainarr = []

for chars in range(len(ciphertext)):
	# print chars
	# print ciphertext[chars]
	if ciphertext[chars] in keyarr:
		# print "hello\n"
		plainarr.append(alphabet[keyarr.index(ciphertext[chars])])
		# print keyarr[keyarr.index(ciphertext[chars])]
	else:
		plainarr.append(ciphertext[chars])

for chars in plainarr:
	outputfile.write(chars)

# print keyarr
# print plainarr

outputfile.close()
keyfile.close()
ciphertextfile.close()