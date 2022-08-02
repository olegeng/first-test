vvod1 = input('Введіть логін:')
vvod2 = input('Введіть пароль:')
my_login="Oleg Pavlish"
my_password='12345678'
while vvod1!= my_login and vvod2 != my_password:
	print('Ви ввели невірний логін або пароль, спробуйте ще раз')
	vvod1 =input('Введіть логін:')
	vvod2 =input('Введіть пароль:')
print('Вітаю вас ' + my_login)
