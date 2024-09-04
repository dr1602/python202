# para usar matplotlib hay que instalarlo

import matplotlib.pyplot

# es un modulo que no viene incroproado en paito, viene en la comunidad pero debemos isntalarlo en nuestro proyecto
# hay que isntalarlo con packagerge
'''
otra forma de importarlo es:
 pip install matplotlib
'''
# le pondremos un alias para usarlo de forma mas facilr

# %%
import matplotlib.pyplot as plt

# %%
def generate_bar_char():
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
    
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    
    plt.show()

# %%
if __name__ == '__main__':
    generate_bar_char()
    
# with variables

# %%
import matplotlib.pyplot as plt

'''
def generate_bar_char(labels, values):    
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()
'''
    
def generate_pie_chart(labes, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
    generate_pie_chart(labels, values)
    
    
# %%
import matplotlib.pylab as plt
import numpy as np

# %% 
plt.figure()
plt.plot(np.sin(np.linspace(-np.pi, np.pi, 1001)))
plt.show()