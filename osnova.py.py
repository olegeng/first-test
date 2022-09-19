logins=['log123', 'log111', 'loger']
passwords=['oleg2005', '12345678', '1111']
def log_in(log,pas,paski=passwords,logi=logins):
	for num, loga in enumerate(logi):
		if log==loga:
			if pas==paski[num]:
				print("Успішна авторизація")
				return True
			else:
				return False
		else: return False
def sign_in(sign_log,sign_pas,paski=passwords,logi=logins):
	global logins
	global passwords
	if sign_log in logi==False:
		logins.append(sign_log)
		passwords.append(sign_pas)
		return True
	elif sign_log in logi==True:
		while sign_log in logi:
			print('Такий логін вже існує, спробуйте інший:\n- ')
			log=input('Введіть логін:')
			pas=input('Введите пароль:')
		logins.append(sign_log)
		passwords.append(sign_pas)
		print(logins)
		return True
def rivn(fx):
	spisok=range(-10000,10000)	
	for z in spisok:
		fx1=fx.replace('x', str(z))
		fx2=fx1.replace('=', '==')		
		numb=fx2.find('==')
		if eval(fx2[0:numb])==eval(fx2[numb+2::]):
			print(z)
			return z
vibir1=input('Авторизація/Регістрація:\n- ')
if vibir1=='Авторизація':
	log=input('Введите логин:')
	pas=input('Введите пароль:')
	log_in(log,pas,passwords,logins)
elif vibir1=='Регістрація':
	log=input('Введіть логін:')
	pas=input('Введіть пароль:')
	sign_in(log,pas)
	
if log_in(log,pas,paski=passwords,logi=logins)==False:
		while log_in(loga,pas,paski=passwords,logi=logins)==False:
			print('Ви ввели неправильний логін або пароль!')
			loga=input('Введите логин:')
			pas=input('Введите пароль:')
			log_in(loga,pas,paski=passwords,logi=logins)
if log_in(log,pas,passwords,logins) or sign_in(log,pas,paski=passwords,logi=logins)==True:
		vibir2=input('Що робимо?\n-' )