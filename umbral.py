#! usr/bin/python
#! encoding UTF-8
import modulopi
import math
PI=3.1415926535897931159979634685441852
def error(nro_intervalos, nro_test, umbral):
 fallos=0
 for i in range(nro_test):
   s=modulopi.aproxpi(nro_intervalos)
   valor=abs(s-PI)
   if valor>=umbral:
     fallos+=1
 p_error=(fallos/nro_test)*100
 return p_error
nro_intervalos=int(raw_input('Introduzca el numero de intervalos'))
nro_test=int(raw_input('Introduzca el numero de test'))
umbral=float(raw_input('Introduzca el error que considera minimo'))
pr=error(nro_intervalos,nro_test,umbral)
print pr
  