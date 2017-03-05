# Este programa prueba las funciones de la libreria dinamica que creamos lib.so

import ctypes as C           # Importamos Ctypes para comunicar C con Python
import numpy as np
lib=C.CDLL('./lib.so')       # Le decimos que vamos a usar nuestra libreria

# Definimos los tipos de los argumentos y el tipo del return de las funciones
# para que C entienda que queremos decirle con Python

###############################################################################
# Probamos la parte de sumar 'add_two.c'
###############################################################################

# Suma de enteros y floats

lib.add_float.restype=C.c_float
lib.add_int.restype=C.c_int

lib.add_float.argtypes=[C.c_float,C.c_float]
lib.add_int.argtypes=[C.c_int,C.c_int]

suma_floats=lib.add_float (3,4)
suma_enteros=lib.add_int(3,4)

print 'Suma_floats={}'.format(suma_floats)
print 'Suma_enteros={}'.format(suma_enteros)

# Suma de enteros y floats por referencia

tres_f=C.c_float(3)
cuatro_f=C.c_float(4)
resultado_f=C.c_float()

lib.add_float_ref(C.byref(tres_f),C.byref(cuatro_f),C.byref(resultado_f))
suma_floats_ref=resultado_f.value

print 'Suma_porRef_floats=',suma_floats_ref

tres_i=C.c_int(3)
cuatro_i=C.c_int(4)
resultado_i=C.c_int()

lib.add_int_ref(C.byref(tres_i),C.byref(cuatro_i),C.byref(resultado_i))
suma_int_ref=resultado_i.value

print 'Suma_porRef_int=',suma_int_ref

###############################################################################
# Probamos la parte de sumar 'arrays.c'
###############################################################################

# Forma 1 (sin Numpy)

array1_i=(C.c_int* 4)(1,2,3,-6)    # Es un puntero entero de 4 lugares
array2_i=(C.c_int* 4)(3,-7,8,-1)
sum_array_i=(C.c_int* 4)()
leng_i=C.c_int(4)

lib.add_int_array(C.byref(array1_i),C.byref(array2_i),C.byref(sum_array_i),leng_i)

print 'El vector suma es: (',sum_array_i[0],sum_array_i[1],sum_array_i[2],sum_array_i[3],')'

array1_f=(C.c_float* 4)(1,2,3,-6)  # Es un puntero float de 4 lugares
array2_f=(C.c_float* 4)(3,-7,8,-1)
lib.dot_product.restype=C.c_float

resultado=lib.dot_product(C.byref(array1_f),C.byref(array2_f),leng_i)

print 'El producto punto es:',resultado

# Forma 2 (con Numpy)

pointer_int=C.POINTER(C.c_int)  # Defino un pointer entero
arr1_i=np.array([1,2,3,-6],dtype=C.c_int)
arr2_i=np.array([3,-7,8,-1],dtype=C.c_int)
out_i=np.zeros(4,dtype=C.c_int)

lib.add_int_array(arr1_i.ctypes.data_as(pointer_int),arr2_i.ctypes.data_as(pointer_int),out_i.ctypes.data_as(pointer_int),leng_i)

print 'El vector suma es:(',out_i[0],out_i[1],out_i[2],out_i[3],')'

pointer_f=C.POINTER(C.c_float)
arr1_f=np.array([1,2,3,-6],dtype=C.c_float)
arr2_f=np.array([3,-7,8,-1],dtype=C.c_float)

out_f=lib.dot_product(arr1_f.ctypes.data_as(pointer_f),arr2_f.ctypes.data_as(pointer_f),leng_i)

print 'El producto punto es:',out_f












