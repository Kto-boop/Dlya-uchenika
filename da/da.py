#import eel
#eel.init("web")
#eel.start("main.html,size=(700,700)")
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
