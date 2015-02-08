# your code here

inStr = raw_input("Input:")
mask = 0x3FFFFFFF
outHash = 0

for byte in inStr:
	intermediate_value = ((ord(byte) ^ 0xCC) << 24) | ((ord(byte) ^ 0x33) << 16) | ((ord(byte) ^ 0xAA) << 8) | ((ord(byte) ^ 0x55))
	outHash = (outHash&mask) + (intermediate_value&mask)

print hex(outHash)


# print inStr