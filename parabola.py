import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# Estudo de parábolas
print("equação da parábola com a diretriz paralela ao eixo x")
print("Forma da equação: ax²+bx+c")
a = int(input("Defina a: "))
b = int(input("Defina b: "))
c = int(input("Defina c: "))

def parabola(a,b,c,x):
    y = a*(x**2) + b*x + c
    return y
def animacao(i):
    line.set_data(xPonto, ((xPonto+i - foco['x'])**2/(2*parametro)) + yVertice)
    return line,
def dados_fundamentais_parabola():
    print(f'parametro = {parametro}')
    print(f'Vertice ({vertice['x']:.2f}, {vertice['y']:.2f})')
    print(f'Foco ({foco['x']:.2f}, {foco['y']:.2f})')
    print(f'diretriz: y = {diretriz}')

#pesquisa de raízes
discriminante = b**2-4*a*c
print(f'o valor do discriminante é: {discriminante}')
if discriminante < 0:
    print("a equação não possui raízes reais")
    moduloDiscriminante = -1*discriminante
    parteImaginaria = math.sqrt(moduloDiscriminante)/(2*a)
    parteReal = -b/(2*a)
    x1 = {'Real': parteReal, 'imaginaria': + parteImaginaria}
    x2 = {'Real': parteReal, 'imaginaria': - parteImaginaria}
    print(f'x1 = {x1["Real"]:.2f} + {x1["imaginaria"]:.2f}i')
    print(f'x2 = {x2["Real"]:.2f} + {x2["imaginaria"]:.2f}i')
else:
    print(f'a raiz quadrada do discriminante é: {math.sqrt(discriminante)}')
    x1 = (-b + math.sqrt(discriminante))/(2*a)
    x2 = (-b - math.sqrt(discriminante))/(2*a)
    print("x1 =", x1)
    print("x2 =", x2)

#pontos notáveis
parametro = 1/(2*a)
xVertice = -b / (2 * a)
yVertice = -discriminante / (4 * a)
vertice = {'x': xVertice, 'y': yVertice}
xFoco = -b/(2*a)
yFoco = yVertice + parametro/2
foco = {'x': xFoco, 'y': yFoco}
diretriz = yFoco - parametro

dados_fundamentais_parabola()

#lugar geométrico
fig, ax = plt.subplots(1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
xPonto = np.arange(-100, 100, 0.1)
yPonto = []
y_d=[]

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
line, = ax.plot(xPonto, parabola(a,b,c,xPonto), color='red')
#lined, = ax.plot(xPonto, y_d, color='blue', label='Diretriz')
ani = animation.FuncAnimation(fig, animacao, frames=np.arange(0,10,0.01), interval=10)
plt.show()

