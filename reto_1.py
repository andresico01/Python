PreciosDias = [3500,3400,3800,3200,3100,4000]
DiasSemana = ['lunes','marter','miercoles','jueves','viernes','sabado']
## uso varios metodos que aun no han sido explicado pero aja
print("La empresa X fija el precio para sus productos de la siguiente forma:\n")
#uso el metodo len para conocer el tamaño de mi lista 
cont = 0 
while cont < len(PreciosDias):
    print(DiasSemana[cont]+': ',PreciosDias[cont])
    cont+=1
cont = 0 
#como ve uso varias listas esto lo hago por dos razones primero la comprencion del codigo segundo la escalabilidad del mismo
UnidadesVendidas = []
auxiliar = 0
## en vez de tener las valores de las unidades vendidas por dias, algo mas real es desconocer estos valores durante el dia de trabajo 
# y agregarlos cuando ya sean conocidos al fianl del dia. 
##por esa razon uso un metodo como input que digamos captura los caracteres enviados por teclado y de segundo uso int para pasar los valores de estos
## caracteres a numeros enteros, ademas uso el metodo append que pide espacio de memoria para agregar un nuevo valor al final de la lista
while cont < len(PreciosDias):
    auxiliar = int (input('introdusca las unidades que se vendiereon en el dia '+DiasSemana[cont]+':\t')) 
    UnidadesVendidas.append(auxiliar)
    cont+=1
auxiliar = 0
GananciasDias = []
cont = 0 
while cont < len(PreciosDias):
    auxiliar = UnidadesVendidas[cont] * PreciosDias[cont] * 0.1 #multiplico por 0.1 para conocer la ganacia del 10%
    GananciasDias.append(auxiliar) 
    cont += 1
cont = 0
## como soy nuevo en python no se bn como interactua los print cuando meto caracteres y valores numericos
# me dio problema asi que pase todo a string con el metodo join no sin antes decirle que los separe con una ',' y un espacio
# map es otro metodo que uso primero para decir a que tipo de variable quiero me cambie los elementos de mi lista y segundo pasando la lista 
# a la cual quiero acceder para hacer su cambio de variable 
GananciasDias = ", ".join(map(str,GananciasDias))
UnidadesVendidas = ", ".join(map(str,UnidadesVendidas))
while cont < len(PreciosDias):
    print('Las unidades vendidas el dia '+DiasSemana[cont]+'fueron: '+UnidadesVendidas[cont]+' su ganancia fue de '+GananciasDias[cont]) 
    cont+=1

# por ultimo disculpe por tanto texto pero querian que supiera que si se lo que hice y las razones por las que la hice  