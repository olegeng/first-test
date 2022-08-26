logins = ['log123', 'Oleg Pavlish']
Paswords = ['oleg2005', '12345678']
login=input('Введіть логін:')
password=input('Введіть пароль:')
def authorizate():
	a=0
	number=-1
	while a==0:
		login=input('Введіть логін:')
		password=input('Введіть пароль:')
		for log in logins:
			number+=1
			if login==log:
				break
				if password==Paswords[number]:
					a+=10
					global auth
					auth=True
					return auth
print(authorizate)
dia=input('ffff:')
if dia=='Авторизація':
	authorizate
