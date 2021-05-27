import eel
from random import randint
from pprint import pprint

from pairs import pairs
import example as ex
from config import config as CONFIG

PRODUCTION = True

eel.init('wgui')
eel.start('', block=False, size=CONFIG['WIN_SIZE'])

@eel.expose
def WindowClose():
	exit()

lastSentTest = [None]
name, group = '', ''

@eel.expose
def GetTime():
	return CONFIG['TIME']

def GetTable(clk, b=CONFIG['VARS']):
	X, Y, Z, W = 0, 0, 0, 0
	table = [['XYZW'[i] for i in range(b)]]
	table[0].append('F')

	for i in range(2 ** b):
		X = int(bool(i & 1)) # черная магия масок
		Y = int(bool(i & 2))
		Z = int(bool(i & 4))
		W = int(bool(i & 8))
		row = []
		if b > 0:
			row.append(X)
		if b > 1:
			row.append(Y)
		if b > 2:
			row.append(Z)
		if b > 3:
			row.append(W)
		row.append(int(eval(clk)))
		table.append(row)
	return table

def CAFunc1(clk):
	table = GetTable(clk)
	ca = []
	for i in range(1, len(table)):
		ca.append(str(table[i].pop()))
		table[i].append('?')
	return ' '.join(ca), table

def CAFunc2(clk): #СДНФ
	table = GetTable(clk)
	ca = []
	for row in table:
		if row[len(row) - 1] == 'F' or not int(row[len(row) - 1]):
			continue
		t = []
		for i in range(len(row) - 1):
			t.append(('!' if not row[i] else '') + 'XYZW'[i])
		ca.append(' * '.join(t))
	ca = ' + '.join(ca)
	if not ca:
		ca = '0'
	return ca, table
	
def CAFunc3(clk): #СКНФ
	table = GetTable(clk)
	ca = []
	for row in table:
		if row[len(row) - 1] == 'F' or int(row[len(row) - 1]):
			continue
		t = []
		for i in range(len(row) - 1):
			t.append(('!' if row[i] else '') + 'XYZW'[i])
		ca.append(f'({" + ".join(t)})')
	ca = ' * '.join(ca)
	if not ca:
		ca = '1'
	return ca, table

def CAFunc4(clk, fn):
	table = GetTable(clk, 2)
	return fn.split()[1], table

def GenTask(text, CAFunc, hint=None, noExpr=False):
	fn, clk = BuildExpr(CONFIG['VARS'], CONFIG['CONSTS'])
	ca, table = CAFunc(clk)
	t = {
		'answer': None,
		'text': text,
		'question': {
			'text': text,
			'table': table,
			'expr': fn if not noExpr else '',
			'hint': hint
		}, 
		'correctAnswer': ca
	}
	return t

@eel.expose
def GenTest(_name, _group, train, trainNums=None): # генерируем тесты
	# not not (not ((not W == 1) <= 1) <= 0) or 1 or 1 or Z == Y and X
	global name, group
	name, group = _name, _group
	rs = []

	n1 = int(trainNums and trainNums[0] or CONFIG['TASKS_1'])
	n2 = int(trainNums and trainNums[1] or CONFIG['TASKS_2'])
	n3 = int(trainNums and trainNums[2] or CONFIG['TASKS_3'])
	n4 = int(trainNums and trainNums[3] or CONFIG['TASKS_4'])

	for _ in range(n1):
		rs.append(GenTask('Заполните последний столбец таблицы для выражения', CAFunc1))
	for _ in range(n2):
		rs.append(GenTask('Составьте СДНФ для', CAFunc2, noExpr=True))
	for _ in range(n3):
		rs.append(GenTask('Составьте СКНФ для', CAFunc3, noExpr=True))
	for _ in range(n4):
		fn, clk = BuildExpr(2, 0)
		fn = fn.replace('!', '')
		clk = clk.replace('not ', '')
		ca, table = CAFunc4(clk, fn)
		t = {
			'answer': None,
			'text': f'Введите операцию, соответствующую этой таблице (=>, *, +, =, ^) для выражения {fn.split()[0] + " ? " + fn.split()[2]}',
			'question': {
				'text': f'Введите операцию, соответствующую этой таблице (=>, *, +, =, ^) для выражения {fn.split()[0] + " ? " + fn.split()[2]}',
				'table': table,
				'expr': '',
				'hint': None
			}, 
			'correctAnswer': ca
		}
		rs.append(t)

	global lastSentTest
	lastSentTest = []
	for v in rs:
		lastSentTest.append(dict(v))
	if not train:
		for i in range(len(rs)):
			rs[i]['correctAnswer'] = None
	return rs


@eel.expose
def Judge(test, train):
	global lastSentTest
	total = len(lastSentTest)
	done = 0
	tasks = [] # выходная таблица, для GUI (!)
	for i in range(len(lastSentTest)):
		v = lastSentTest[i]
		ok = isinstance(test[i]['answer'], str) and test[i]['answer'].replace(' ', '') == v['correctAnswer'].replace(' ', '') # верность ответа
		lastSentTest[i]['answer'] = test[i]['answer'] # пишем ответ в выход
		if ok:
			done += 1
		tasks.append({
			'answer': test[i]['answer'],
			'correctAnswer': v['correctAnswer'],
			'correct': ok
		})
	mark = done / total
	if not train:
		ex.SendToServer(CONFIG['IP'], name, group, mark, lastSentTest)
	vmark = 0
	for i, threshold in pairs(CONFIG['VRATES']):
		if mark * 100 >= threshold:
			vmark = 5 - i
			break
	return { 'tasks': tasks, 'mark': mark, 'vmark': vmark }


def BuildExpr(_vars, _consts):
	vars, consts = _vars, _consts
	heap = []
	strCalc, strFinal = '', ''

	for i in range(vars + consts):
		const = vars > 0 and consts > 0
		if const:
			const = bool(randint(0, 1))
		else:
			const = consts > 0
		if const:
			heap.append(str(randint(0, 1)))
			consts -= 1
		else:
			heap.append(str('XYZW'[_vars - vars]))
			vars -= 1
	
	for i in range(len(heap) - 1):
		brackets = len(heap) > 2 and bool(randint(0, 1))
		invToken = bool(randint(0, 1))
		operators = ['=>', '*', '+', '=', '^']
		if invToken:
			heap[0] = '!' + heap[0]
		heap[0] = f'{heap[0]} {operators[randint(0, len(operators) - 1)]} {heap[1]}'
		del heap[1]
		if brackets:
			heap[0] = f'({heap[0]})'
	
	strFinal = heap[0]
	strCalc = strFinal.replace('!', 'not ').replace('0', 'False').replace('1', 'True')
	for k, v in {
		'=>': '<=',
		'*': 'and',
		'+': 'or',
		'=': '==',
		'^': '!='
	}.items():
		strCalc = strCalc.replace(f' {k} ', f' {v} ')

	return strFinal, strCalc
	
while True:
	eel.sleep(10)