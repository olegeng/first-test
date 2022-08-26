def lomka():
	symbols=["a", "b", "c", "d", "e", 'f', 'g', "h", 'i', "j", 'k', 'l', 'm','n','o','p','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
	parol=input('Введіть пароль який потрібно вгадати:')
	x=0
	n=0
	word=''
	while x==0:
		for y in symbols:				
			if y==parol[n]:
					word+=y
					n+=1
			print('Шукаємо: '+word)
			if word==parol:
				print('Пароль:'+word)
				x+=5
vibir2=input('Що робимо?\n-' )
if vibir2=='Взлом':
	lomka()