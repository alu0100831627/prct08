#! usr/bin/python
#! encoding UTF-8
def aproxpi (n):
  s = 0.0
  for i in range(1,n+1):
    xi= float((i-0.5)/n)
    f_xi= float(4/(1+xi**2))
    s = s + f_xi
    r = s / n    
  return r
if __name__=="__main__":  
 import sys
 if(len(sys.argv)==3):
   p1=int(sys.argv[1])
   p2=int(sys.argv[2])
   l=[ ]
   for i in range(1,p2+1):
    x=aproxpi(p1*i)
    l=l+[x] 
    print x
   print l 
 else:
   print('Debe introducir el numero de intervalos y veces que desea que se repita en la linea de comando, por defecto saldra 10 intervalos y 10 veces')
   p1=10
   p2=10
   l=[ ]
   for i in range(1,p2+1):
    x=aproxpi(p1*i)
    l=l+[x] 
    print x
   print l 
 
 
