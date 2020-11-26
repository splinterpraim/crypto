line=100
alf=[chr(ord('a') + i) for i in range(26)]
key = 'hello'
key = input('Enter key: ').lower()
try:
	with open('output.txt', 'r') as file_output:
		msg_output = file_output.read()
		print('\nOUTPUT TEXT:\n','-'*line,f'\n{msg_output}\n', '-'*line)
		codering_msg=msg_output
		for i in '.!,? \n':
			codering_msg = codering_msg.replace(i,'')
		key*=len(codering_msg)//len(key)+1
		decodering_msg=''
		for k,v in enumerate(codering_msg):
			decodering_msg +=alf[((alf.index(v)-ord(key[k])+ord('a'))%len(alf))]
		for k,v in enumerate(msg_output):
			if v in '.!,? \n':
				decodering_msg=decodering_msg[:k]+v+decodering_msg[k:]
		print('\nDECODED TEXT:\n','-'*line,f'\n{decodering_msg}\n', '-'*line)
except FileNotFoundError:
	print('File is not found')
	exit()