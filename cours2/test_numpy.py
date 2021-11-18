'''
numpy permet de manipuler efficacement de grandes quantités
de données numériques

'''
import numpy as np 

#l'objet de bas de numpy est l'array
#c'est un tableau qui peut avoir plusieur dimensions

a= np.array([5,3,8,1,0])
print(a)
print()

array2d= np.array([[3,2,1,],[6,5,4]])
print(array2d)
print("dimension : ",array2d.ndim)
