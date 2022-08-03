x = 0
A = ["Oleg Pavlish", "Petro Grigorenko", "Василь Петрович", "olegpa2005", 'user1212']
B = ["Simon Petlura", "Mirage", "Ivan", "Petro Grigorenko", "user1212"]
while x==0:
	work= input('Що будемо робити:')
    if work == 'Додати інформацію':
	    spisok = input('Введіть в який список додаємо інформацію (A/B):')
	    if spisok == 'A'or 'А' or 'a' or 'а':
		    dobavka = input('Введіть те, що будемо додавати до списку:')
		    A.append(dobavka)
		    print('Ваш список А:',A)
	    elif spisok == 'B' or 'b' or 'В':
		    dobavka = input('Введіть те, що будемо додавати до списку:')
		    B.append(dobavka)
		    print('Ваш список B:',B)
if work == 'Знайти збіги в списках':
	for k in A:
	    for c in B:
	        if k==c:
	        	i=0
		        i+=1
		        print(str(i) + '-й елемент:' + str(c))
    