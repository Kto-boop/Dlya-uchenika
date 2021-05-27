import requests
from template import export
from random import randint as rnd
from time import time
from json import dumps as jd

TASKNAME = 'My task name' # имя вашего задания. Номер там, или еще что-то

# генератор записей
def NewRecord(username, group, mark):
	cp = export.copy()
	# далее настраиваем новую запись об учинике
	cp['subTasks'].clear()
	cp['datetime'] = time()
	cp['class'] = '11В' # класс
	cp['taskName'] = TASKNAME
	cp['student'] = username
	cp['mark'] = mark
	return cp
def NewSubTask(q, i):
	return {
		'name': str(i),
		'text': q['question'],
		'correctAnswer': q['correctAnswer'],
		'answer': q['answer']
	}

def SendToServer(ip, username, group, mark, tasks):
	sdata = NewRecord(username, group, mark)
	sdata['subTasks'] = [NewSubTask(tasks[i], i) for i in range(len(tasks))]

	# ip = 'localhost' # ip хоста
	try:
		requests.post(f'http://{ip}:1338/dbappend', json=[sdata]) # шлем на сервер
	except:
		print('Сервер \x1b[31mмёртв\x1b[0m внутри')