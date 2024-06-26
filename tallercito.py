import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io as sio

#1 aquí se creó una matriz que tuviera size 1,200,000 y se verificó

array4D=np.random.rand(10,100,30,40)
print(np.size(array4D))

#2 Se crea la copia de la matriz, pero en 3 dimensiones eliminando la cuarta y se verifica el size tanto de la copia como del copiado

array3D=array4D.copy()[:,:,:,0]
print(np.size(array3D))
print(np.size(array4D))

#3 muestro las características de la matriz con las siguientes funciones:
print("Dimensiones array3D: ",array3D.ndim)
print("Size del array3D: ",array3D.size)
print("Shape del array3D: ",array3D.shape)
print("dtype del array3D: ",array3D.dtype)

#4
array2D = np.reshape(array3D,(300,100))
print(np.shape(array2D))
print(np.shape(array3D))

#5

def array_to_dataframe(array):
    DataFrame = pd.DataFrame(array)
    print(DataFrame)
    return DataFrame

array_to_dataframe(array2D)

#6 

def Cargar_Archivo(url):
    if url.endswith(".mat"):
        data = sio.loadmat(url)

    elif url.endswith(".csv"):
        data = pd.read_csv(url)

    else:
        raise ValueError("Formato de archivo no soportado")
    
    return data

#7
def suma(array,eje):
    return np.sum(array,axis=eje)
    
def resta(array,eje):
    return np.subtract(array,axis=eje)
    
def producto(array,eje):
    return np.product(array,axis=eje)

def division(array,eje):
    return np.divide(array,eje)

def logaritmo(array):
    return np.log(array)

def promedio(array,eje):
    return np.mean(array,axis=eje)

def desviacion_est(array,eje):
    return np.std(array,axis=eje)







