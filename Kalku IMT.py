sign=input('Введіть логін:')
passw=input('Введіть пароль:')
for x in logins:
	numb+=1
	if sign==x:
		break
if passw!= Paswords[numb]:
	while z==0:
		numb=-1
		print('Ви провалили авторизацію, спробуйте ще раз!')
		sign=input('Введіть логін:')
		passw=input('Введіть пароль:')
		for x in logins:
			numb+=1
			if sign==x:
				if passw == Paswords[numb]:
					z+=5
					print('Ви успішно авторизувались')
					break
elif passw==Paswords[numb]:
	print('Ви успішно авторизувались')
print('fff')
