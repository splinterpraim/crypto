import math
alf=[chr(ord('a') + i) for i in range(26)]
line = 100
frequensy_letter={'a':8.17,
				  'b':1.49,
				  'c':2.78,
				  'd':4.25,
				  'e':12.7,
				  'f':2.23,
				  'g':2.02,
				  'h':6.09,
				  'i':6.97,
				  'j':0.15,
				  'k':0.77,
				  'l':4.03,
				  'm':2.41,
				  'n':6.75,
				  'o':7.51,
				  'p':1.93,
				  'q':0.1,
				  'r':5.99,
				  's':6.33,
				  't':9.06,
				  'u':2.76,
				  'v':0.98,
				  'w':2.36,
				  'x':0.15,
				  'y':1.97,
				  'z':0.05}
try:
	with open('output.txt', 'r') as file_output:
		msg_output = file_output.read()
		print()
		print('\nCRIPTO TEXT:\n','-'*line,f'\n{msg_output}\n', '-'*line)
		msg=msg_output
		for i in '.!,? \n':
			msg = msg.replace(i,'')

		#find length of  key
		for x in range(len(msg)-1):
			new_msg = msg[::x+1]
			index = sum([((new_msg.count(y)/len(new_msg))**2) for y in alf])


			if index > 0.062:
				#find shift of key
				print('')
				shift=[]

				
				for i in range(x+1):
					for_key = msg[i::x+1]
					key_full={}
					#frequency letters of text on key's symbols
					for j in alf:
						key_full[j]=(for_key.count(j)/len(for_key))*100
					
					#frequency letters of text and of alfabet 
					#counting shift
					max_key_d=max(key_full, key=key_full.get)
					max_key_alf=max(frequensy_letter, key=frequensy_letter.get)
					shift.append(alf.index(max_key_alf)-alf.index(max_key_d))

				sw=0
				new_text=''
				#shift all letters of text
				for let in msg:
					new_text+=alf[(ord(let)-ord('a')+shift[sw])%26]
					if sw==(len(shift)-1):
						sw=-1
					sw+=1
				for k,v in enumerate(msg_output):
					if v in '.!,? \n':
						new_text=new_text[:k]+v+new_text[k:]
				print()
				print('\nDECRYPTED TEXT:\n','-'*line,f'\n{new_text}\n', '-'*line)
				
				while 1:
					symbol = input('This is text? (if yes press \'y\', else no press \'n\' for continue or \'e\' for exit)').lower()
					if symbol == 'y' or symbol == 'e':
						exit()
					elif symbol == 'n':
						break;
					else:
						input('You written wrong')
except FileNotFoundError:
	print('File is not found')
	exit()