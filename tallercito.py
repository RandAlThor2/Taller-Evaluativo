import numpy as np
import pandas as pt
import matplotlib.pyplot as plt
import scipy.io as sio

#1 aquí se creó una matriz que tuviera size 1,200,000 y se verificó

array4D=np.random.rand(10,100,30,40)
print(np.size(array4D))

#2 Se crea la copia de la matriz, pero en 3 dimensiones eliminando la cuarta y se verifica el size tanto de la copia como del copiado

array3D=array4D.copy()[:,:,:,0]
print(np.size(array3D))
print(np.size(array4D))

