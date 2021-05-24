#import eel
#eel.init("web")
#eel.start("main.html,size=(700,700)")
from config import config as CONFIG

def get_sdnf(table):
    result = []
    for inputs, row_result in table.items():
        if row_result:
            row = []
            for value, letter in zip(inputs, 'XYZIJK'):
                row.append(('' if value else 'не ') + letter)
            
            result.append('({})'.format(' и '.join(row)))
    return ' или '.join(result)
table = {
    (0, 0): 0,
    (0, 1): 0,
    (1, 0): 1,
    (1, 1): 1
}

print(get_sdnf(table))


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
