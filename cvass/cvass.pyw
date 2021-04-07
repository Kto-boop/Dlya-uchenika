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
	
