#-*- coding: UTF-8 -*-2
import tkinter, random, sys
import questions

class cvass:
	def __init__(self):
		self.list_of_questions=questions.questions 
		self.list_of_test=[] 
		self.list_of_ansvers=[] 
		self.ink=0 
		self.points=0
		
	def get_questions(self):
		self.list_of_ansvers=list(self.list_of_questions.keys())
		for i in range(0,10):
			num=random.randint(0,len(self.list_of_ansvers)-1)
			quest=self.list_of_ansvers.pop(num)
			self.list_of_test.append(self.list_of_questions[quest])
		self.print_questions()
		
	def print_questions(self):
		numbers = 'Первый Второй Третий Четвертый Пятый Шестой Седьмой Восьмой Девятый Десятый'.split()
		disp.insert(1.0, '>>> '+numbers[self.ink]+' вопрос:\n')
		disp.insert(1.0, '>>> '+self.list_of_test[self.ink]+'\n')
		self.ink += 1	
	
	def check_ansver(self, event):
		usr_ansver = ansver.get().lower()
		if self.ink == 0:
			disp.insert(1.0, '>>> Начните игру\n')
		elif len(usr_ansver) == 0:
			disp.insert(1.0, '>>> Пустая строка не может быть ответом\n')
		else: 
			for k, v in self.list_of_questions.items():
				if v == self.list_of_test[self.ink -1]:
					true_ansver = k			
			if usr_ansver == true_ansver:
				disp.insert(1.0,'>>> И это правильный ответ! Вам начисляется 1 балл!\n')
				self.points = +1
				self.check_questions()
				ansver.delete(0, tkinter.END)
		
			else:
				disp.insert(1.0, '>>> Ошибка! Правильный ответ "'+true_ansver+'"\n')
				self.check_questions()
				ansver.delete(0, tkinter.END)

#Здесь будет подвод итогов



c =cvass()
#Создаем окно программы
root = tkinter.Tk()
root.geometry('500x500')
root.title('Загадки')

#меню
m = tkinter.Menu(root) 
root.config(menu=m) 
fm = tkinter.Menu(m) 
m.add_cascade(label="Файл",menu=fm) 
fm.add_command(label="Играть", command = c.get_questions) #формируется список команд пункта меню
fm.add_command(label="Справка", command = rules_of_the_game)
fm.add_command(label="О программе", command = about_us)
fm.add_command(label="Выход", command = go_out)

disp = tkinter.Text(root, width=55, height = 25, font = 'Arial 12', wrap = tkinter.WORD)

#Форма для ответа
frame = tkinter.Frame(root, width=500,height=50)
ansver = tkinter.Entry(frame, width = 39, font = 'Arial 12')
ans_but = tkinter.Button(frame, text = 'Ответить', width = 14)

disp.place(x = 0, y = 0)
frame.place(x = 0, y = 450)
ansver.place(x = 10, y = 15)
ans_but.place(x = 380, y = 13)
ans_but.bind("<Button-1>", c.check_ansver)

root.mainloop()


