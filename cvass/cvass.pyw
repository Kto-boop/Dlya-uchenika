#-*- coding: UTF-8 -*-
import tkinter, random, sys
import questions

class Enigmas:
	def __init__(self):
		self.list_of_questions = questions.questions #Переменная в которой хранятся все вопросы и ответы
		self.list_of_victorine = [] #В этой переменной будем хранить список вопросов и ответов тукущей игры.
		self.list_of_ansvers = [] #Переменная с ответами на вопросы
		self.ink = 0 #Номер текущего вопроса
		self.points = 0 #Количество очков, набранных игроком.
		
	def get_questions(self):
		self.list_of_ansvers = list(self.list_of_questions.keys())
		for i in range(0, 10):
			num = random.randint(0, len(self.list_of_ansvers)-1)
			quest = self.list_of_ansvers.pop(num)
			self.list_of_victorine.append(self.list_of_questions[quest])
		self.print_questions()
		
	def print_questions(self):
		numbers = 'Первый Второй Третий Четвертый Пятый Шестой Седьмой Восьмой Девятый Десятый'.split()
		disp.insert(1.0, '>>> '+numbers[self.ink]+' вопрос:\n')
		disp.insert(1.0, '>>> '+self.list_of_victorine[self.ink]+'\n')
		self.ink += 1	
	
	def check_ansver(self, event):
		usr_ansver = ansver.get().lower()
		if self.ink == 0:
			disp.insert(1.0, '>>> Начните игру\n')
		elif len(usr_ansver) == 0:
			disp.insert(1.0, '>>> Пустая строка не может быть ответом\n')
		else: #Если все хорошо, получаем правильный ответ
			for k, v in self.list_of_questions.items():
				if v == self.list_of_victorine[self.ink -1]:
					true_ansver = k
			#Проверяем праильность ответа игрока			
			if usr_ansver == true_ansver:
				disp.insert(1.0,'>>> И это правильный ответ! Вам начисляется 1 балл!\n')
				self.points = +1
				self.check_questions()
				ansver.delete(0, tkinter.END)
		
			else:
				disp.insert(1.0, '>>> Ошибка! Правильный ответ "'+true_ansver+'"\n')
				self.check_questions()
				ansver.delete(0, tkinter.END)
			
	def check_questions(self):
		if self.ink < 10:
			disp.insert(1.0,'\n')
			self.print_questions()
		else:
			disp.insert(1.0, '>>> Вопросы закончились. Подведем итог: \n')
			disp.insert(1.0, '>>> Вы набрали '+str(self.points)+ ' баллов.')
			if self.points < 5:
				disp.insert(1.0, '>>> Плохо! Очень плохо! Учитесь лучше и больше!\n')
			elif self.points < 8:
				disp.insert(1.0, '>>> Неплохо! Но, я уверен, Вы можете улучшить результат!\n')
			else:
				disp.insert(1.0, '>>> Превосходный результат!!! Попробуешь еще раз?\n')
			self.ink = 0
			self.points = 0

#О программе
def about_us():
	win = tkinter.Toplevel(root)
	win.title("О программе...")
	win.minsize(width=230,height=100)
	win.maxsize(width=230,height=100)
	lab = tkinter.Label(win, text = 'тестирование ученика. v.0.1a\n\n\nПрограмма создана \nв процессе изучения Python 3', font = 'Tahoma 12')
	lab.pack(expand=1)
	
#Правила игры
def rules_of_the_game():
	rules = '''Правила игры очень просты.
Программа задаст ряд вопросов и, на
основе ваших ответов попытается
оценить уровень знаний игрока.

Размер букв в ответе игрока не
имеет значения. Ответы типа "ответ",
"Ответ" и "ОТВЕТ" являются идентичными.

Никого не хотел обидеть. Не серчайте,
ежели что ;) 

Можно добавлять свои вопросы и ответы
путем редактирования файла questions.py.
Ответы обязательно нужно писать маленькими
буквами. '''
	win = tkinter.Toplevel(root)
	win.title("Правила игры.")
	win.minsize(width=400,height=400)
	win.maxsize(width=400,height=400)
	lab = tkinter.Label(win, text = rules, font = 'Tahoma 12', justify = tkinter.LEFT)
	lab.pack(expand=1)

#Функция выхода
def go_out():
	sys.exit()

#Основной код программы
c = Enigmas()
#Создаем окно программы
root = tkinter.Tk()
root.geometry('500x500')
root.title('тестирование')

#Добавляем меню
m = tkinter.Menu(root) #создается объект Меню на главном окне
root.config(menu=m) #окно конфигурируется с указанием меню для него
fm = tkinter.Menu(m) #создается пункт меню с размещением на основном меню (m)
m.add_cascade(label="Файл",menu=fm) #пункту располагается на основном меню (m)
fm.add_command(label="Играть", command = c.get_questions) #формируется список команд пункта меню
fm.add_command(label="Справка", command = rules_of_the_game)
fm.add_command(label="О программе", command = about_us)
fm.add_command(label="Выход", command = go_out)

#Создаем основное окно для вывода текста, переносим текст по словам
disp = tkinter.Text(root, width=55, height = 25, font = 'Arial 12', wrap = tkinter.WORD)

#Форма для ответа
frame = tkinter.Frame(root, width=500,height=50)
ansver = tkinter.Entry(frame, width = 39, font = 'Arial 12')
ans_but = tkinter.Button(frame, text = 'Ответить', width = 14)

#Производим упаковку виджетов
disp.place(x = 0, y = 0)
frame.place(x = 0, y = 450)
ansver.place(x = 10, y = 15)
ans_but.place(x = 380, y = 13)
#Привязываем действие к кнопке "Ответить"
ans_but.bind("<Button-1>", c.check_ansver)

root.mainloop()
