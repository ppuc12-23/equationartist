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
def diretriz_parabola(p):
    y_d = foco['y'] - p
    return f'y = {0}*x + {y_d}'

def discriminante_parabola(a, b, c):
    delta = b ** 2 - 4 * a * c
    return delta

def dados_fundamentais_parabola():
    print(f'parametro = {parametro}')
    print(f'Vertice ({vertice['x']:.2f}, {vertice['y']:.2f})')
    print(f'Foco ({foco['x']:.2f}, {foco['y']:.2f})')
    print(f'diretriz: {diretriz_parabola(parametro)}')

#pesquisa de raízes
discriminante = discriminante_parabola(a, b, c)
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

dados_fundamentais_parabola()

#lugar geométrico
fig, ax = plt.subplots(1, 1)
l, = plt.plot([], [], 'k-')
l2, = plt.plot([], [], 'r-')
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 10)

metadata = dict(title='Parabola')
writter = animation.PillowWriter(fps=25)

x_p = []
y_p = []
x_d = []
y_d = []

with writter.saving(fig, 'parabola.gif', 100):
    for x in np.linspace(-10, 10, 100):
        x_p.append(x)
        x_d.append(x)
        y_p.append(parabola(a,b,c,x))
        y_d.append(x*0 + foco['y'] - parametro )

        l.set_data(x_p, y_p)
        l2.set_data(x_d, y_d)
        writter.grab_frame()
