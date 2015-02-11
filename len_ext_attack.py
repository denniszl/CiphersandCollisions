import urllib
from pymd5 import md5, padding
with open('query.txt','r') as myfile:
	query = myfile.read()
with open('command3.txt','r') as myfile:
	command3 = myfile.read()
token = query.split('=')[1].split('&')[0]
params = query.split('&')
message = params[1] + '&' + params[2] + '&' + params[3]
length = len(message) + 8
bits = (length + len(padding(length*8)))*8
h = md5(state=token.decode('hex'), count=bits)
h.update(command3)
newtoken = h.hexdigest()
ret = query.split('=')[0] + '=' + newtoken + '&' + message + urllib.quote(padding(length*8)) + command3
with open('query_updated.txt','w') as text_file:
	text_file.write('{}'.format(ret))
