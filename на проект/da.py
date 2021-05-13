def f(w,x,y,z):
    return (x and y) and (w or z)

import pandas as pd
from itertools import product

def truth_table(f):
    values = [list(x) + [f(*x)] for x in product([False,True], repeat=f.func_code.co_argcount)]
    return pd.DataFrame(values,columns=(list(f.func_code.co_varnames) + [f.func_name]))
