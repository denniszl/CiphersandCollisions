import distance

str1 = open('str1.txt', 'r')
str2 = open('str2.txt', 'r')

plainstr1 = str1.read()
plainstr2 = str2.read()

print distance.hamming(plainstr1, plainstr2)

str1.close()
str2.close()