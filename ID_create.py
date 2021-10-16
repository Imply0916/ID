from random import shuffle
import pandas as pd
import numpy as np
import random
import uuid


l = list(range(100))
random.shuffle(l)
ID=[]
name=[]
for i in range(len(l)):
       ID.append(str(l[i])+random.choice(('a','b','c','d')))
       name.append(random.choice(('a', 'b', 'c', 'd'))+str(random.choice(range(1,100))))


left=[0]
right=[4]
for i in range(100-1):
       left.append(left[i]+4)
       right.append(right[i]+4)



df=pd.DataFrame({   "ID":ID,
                     "left":left,
                     "right":right,
                    "NAME":name}).to_excel("datos.xlsx")








