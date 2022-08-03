x=0
A = ["Oleg Pavlish", "Petro Grigorenko", "Василь Петрович", "olegpa2005", 'user1212']
B = ["Simon Petlura", "Mirage", "Ivan", "Petro Grigorenko", "user1212"]
while x==0:
work= input('Що будемо робити:')
    if work == 'Додати інформацію':
	    yak = input('В який список будемо добавляти? (A/B)')
	    if yak == 'A':
		    simv= input('Введіть символ який хочете добавити:')
		    A.append(simv)
		    print('Ваш список(А):',A)
	    if yak == 'B':
		    simv= input('Введіть символ який хочете добавити:')
		    B.append(simv)
		    print("Ваш список:",B)
    if work == 'Знайти спільні елементи':
	    i=0
	    for k in A:
	        for c in B:
		        if k==c:
			        i+=1
			        print(str(i) + '-й елемент:' + str(c))
    
    







