x = 1
A = ["Oleg Pavlish", "Petro Grigorenko", "Василь Петрович", "olegpa2005", 'user1212']
B = ["Simon Petlura", "Mirage", "Ivan", "Petro Grigorenko", "user1212"]
while x>=0:
	if x>=1:
		wor = input('Що будемо робити? ')
		if wor == 'Додати інформацію':
			wo= input('Введіть те, що будемо добавляти: ')
			spisok = input('В який список будемо додавати? ')
			if spisok == 'A':
				A.append(wo)
				print(str(wo) + ' успішно добавлено до списку А! \nСписок А: '+str(A))
			elif spisok == 'B':
				B.append(wo)
				print(str(wo), 'успішно добавлено до списку В! \nСписок В: '+ str(B))
				print(B)
		elif wor == 'Знайти спільні':
			for k in A:
				for s in B:
					if k==s:
						print(s)
		elif wor == 'Закінчимо':
			break