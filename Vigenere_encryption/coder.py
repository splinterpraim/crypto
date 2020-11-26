line = 100
alf=[chr(ord('a') + i) for i in range(26)]

key = 'hello'
codering_msg=''
key = input('Enter key: ').lower()
#coding
try:
	with open('input.txt', 'r') as file_input:
		msg_input = file_input.read().lower()
		print('\nINPUT TEXT:\n','-'*line,f'\n{msg_input}\n', '-'*line)
		msg=msg_input
		for i in '.!,? \n':
			msg = msg.replace(i,'')
		
		key*=len(msg)//len(key)+1
		for k,v in enumerate(msg):
			codering_msg+=alf[((alf.index(v)+ord(key[k])-ord('a'))%len(alf))]
except FileNotFoundError:
	print('File is not found')
	exit()

#add puncktuation
for k,v in enumerate(msg_input):
	if v in '.!,? \n':
		codering_msg=codering_msg[:k]+v+codering_msg[k:]

#write in file
try:
	with open('output.txt', 'w') as file_output:
		msg = file_output.write(codering_msg)
except FileNotFoundError:
	print('File is not found')
	exit()

print('\nCODED TEXT:\n','-'*line,f'\n{codering_msg}\n', '-'*line)





		