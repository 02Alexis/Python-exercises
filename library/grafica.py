#------ importa librerias pip install matplotlib
import matplotlib
import matplotlib.pyplot as plot

data = { 'apple':30, 'Huawey':100, 'Samsung':40}

# #------- cordenadas x
# brands = ['Apple', 'Huawey', 'Samsung'] 

# #------- cordenadas y
# sold = [30, 100, 40]

# #------- cordenadas x
brands = list(data.keys())

#------- cordenadas y
sold = list(data.values())

#------ inicializacion de la grafica
fig, ax = plot.subplots()

#------ se agrega titulo al eje x
ax.set_xlabel = 'Marcas'

#------ se agrega titulo al eje y
ax.set_ylabel = 'Ventas'


#------ se crea la grafica utlizando las variables brands ejex y sold para el ejey
plot.bar(brands, sold)

#------ al tener la grafica con este metodo se puede guardar y se le asigna un nombre
plot.savefig('grafica.png')

#------ para mostrar
plot.show()