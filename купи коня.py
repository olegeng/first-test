logins = ['log123', 'Oleg Pavlish']
Paswords = ['oleg2005', '12345678']
def log1(sign,passw):
	for x in logins:
		numb=-1
		numb+=1
		if sign==x:
			break
			if passw!=Paswords[numb]:
				while z==0:
					numb= -1
					print('Ви провалили авторизацію, спробуйте ще раз!')
					sign=input('Введіть логін:')
					passw=input('Введіть пароль:')
					for x in logins:
						numb=-1
						numb+=1
						if sign==x:
							if passw == Paswords[numb]:
								aut=bool(True)
								z+=5
								continue
			elif passw==Paswords[numb]:
				print('Ви успішно авторизувались')
vibir1=input('Що будемо робити?\n-')
if vibir1=='Авторизація':
	sign=input('Введіть логін:')
	passw=input('Введіть пароль:')
	print(log1(sign,passw))

	