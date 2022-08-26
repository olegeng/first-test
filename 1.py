ids = 0
xxy=0
aut=bool(True)
xy=0
x = 0
y=0
z=0
numb=-1
logins = ['log123', 'Oleg Pavlish']
Paswords = ['oleg2005', '12345678']
vibir1=input('Регістрація/Авторизація:')
if vibir1 == "Регістрація":
	while xy==0:
		new_log=input('Введіть логін:')
		for x in logins:
			if x==new_log:
				print('Такий логін вже є, придумайте новий.')
			elif x != new_log:
				new_pass=input('Введіть пароль:')
				perevirka_pass=input('Повторіть пароль:')
				if new_pass==perevirka_pass:
					aut=bool(True)
					logins.append(new_log)
					Paswords.append(new_pass)
					xy=xy+5
					break
if vibir1=='Авторизація':
	sign=input('Введіть логін:')
	passw=input('Введіть пароль:')
	for x in logins:
	    numb+=1
	    if sign==x:
	    	break
	    	if passw!=Paswords[numb]:
		        while z==0:
			        numb=-1
			        print('Ви провалили авторизацію, спробуйте ще раз!')
			        sign=input('Введіть логін:')
			        passw=input('Введіть пароль:')
			        for x in logins:
			            numb+=1
			            if sign==x:
				            if passw == Paswords[numb]:
				            	aut=bool(True)
				            	z+=5
				            	continue
print(logins)
print(Paswords)
if aut==bool(True):
	robit=input('Що будемо робити? \n- ')
elif aut==bool(True):
		print('F')

