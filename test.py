
def f_cuadratica(A,B,C):
 x1 = (-B + (B**2 - 4*A*C)**(1/2))/(2*A)
 x2 = (-B - (B**2 - 4*A*C)**(1/2))/(2*A) 
 return print('Las raices son x1=',x1,',   x2=',x2)

print('Solucion de la ecuación A*x^2 + B*x + C= 0\n','Ingrese los coeficientes')
n=float(input('Ingrese coeficiente A: '))
m=float(input('Ingrese coeficiente B: '))
o=float(input('Ingrese coeficiente C: '))
x=f_cuadratica(n,m,o)
