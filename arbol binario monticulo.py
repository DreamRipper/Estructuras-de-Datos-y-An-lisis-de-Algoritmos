#arbol binario monticulo
class Nodo:

    def __init__(self, valor):
        self.valor = valor

class Monticulo:

    def __init__(self, tipo):
        self.lista = []
        self.tipo = tipo

    def ingresar(self, valor):
        newNodo = Nodo(valor)
        self.lista.append(newNodo)
        self.organizar()

    def organizar(self):
        i = len(self.lista) - 1
        if(i != 0):
            if(self.tipo == "max"):
                while(self.lista[i].valor > self.lista[int((i-1)/2)].valor):
                    aux = self.lista[i]
                    self.lista[i] = self.lista[int((i-1)/2)]
                    self.lista[int((i-1)/2)] = aux
                    i = int((i-1)/2)
            elif(self.tipo == "min"):
                while(self.lista[i].valor < self.lista[int((i-1)/2)].valor):
                    aux = self.lista[i]
                    self.lista[i] = self.lista[int((i-1)/2)]
                    self.lista[int((i-1)/2)] = aux
                    i = int((i-1)/2)

    def eliminar(self, valor):
        i = 0
        l = len(self.lista)
        while(i < l):
            if(self.lista[i].valor == valor):
                self.lista[i] = self.lista[l-1]
                self.lista.pop(l-1)
                break
            i = i + 1
        if(self.tipo == "max"):
            if(self.lista[i].valor > self.lista[int((i-1)/2)].valor):
                aux = self.lista[i]
                self.lista[i] = self.lista[int((i-1)/2)]
                self.lista[int((i-1)/2)] = aux
            elif(self.lista[i].valor < self.lista[(int((2*i)+1))].valor):
                aux = self.lista[i]
                self.lista[i] = self.lista[int((2*i)+1)]
                self.lista[int((2*i)+1)] = aux               
            elif(self.lista[i].valor < self.lista[(int((2*i)+2))].valor):
                aux = self.lista[i]
                self.lista[i] = self.lista[int((2*i)+2)]
                self.lista[int((2*i)+2)] = aux
        elif(self.tipo == "min"):
            if(self.lista[i].valor < self.lista[int((i-1)/2)].valor):
                aux = self.lista[i]
                self.lista[i] = self.lista[int((i-1)/2)]
                self.lista[int((i-1)/2)] = aux
            elif(self.lista[i].valor > self.lista[(int((2*i)+1))].valor):
                aux = self.lista[i]
                self.lista[i] = self.lista[int((2*i)+1)]
                self.lista[int((2*i)+1)] = aux               
            elif(self.lista[i].valor > self.lista[(int((2*i)+2))].valor):
                aux = self.lista[i]
                self.lista[i] = self.lista[int((2*i)+2)]
                self.lista[int((2*i)+2)] = aux

    def imprimir(self):
        for i in self.lista:
            print(i.valor)

    def preOrden(self, indice):
        if(indice >= (len(self.lista))):
            return
        print(self.lista[indice].valor)
        self.preOrden((2*indice)+1)
        self.preOrden((2*indice)+2)
        
    def porNiveles(self):
        cola1 = Cola()
        cola1.insertar(0)
        while(cola1.vacia() == False):
            nodoCola = cola1.primero.valor
            print(self.lista[nodoCola].valor)
            cola1.eliminar()
            if(((2*nodoCola) + 1) < (len(self.lista))):
                cola1.insertar((2*nodoCola) + 1)
            if(((2*nodoCola) + 2) < (len(self.lista))):
                cola1.insertar((2*nodoCola) + 2)
class Nodocola:
    
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    
    def __init__(self):
        self.ultimo = None
        self.primero = None
        
    def vacia(self):
        empty = False
        if(self.primero == self.ultimo == None):
            empty = True
        
        return empty

    def insertar(self, valor):
        nodo_nuevo = Nodocola(valor)
        if(self.vacia()):
            self.primero = self.ultimo = nodo_nuevo
        else:
            nodo_nuevo.siguiente = None
            self.ultimo.siguiente = nodo_nuevo
            self.ultimo = nodo_nuevo
            
    def eliminar(self):
        if self.vacia():
            print('\nNo es posible eliminar un elemento de una cola vacía.')
            return
        if (self.primero == self.ultimo):
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente

monticulo1 = Monticulo("max")
monticulo2 = Monticulo("min")
#Pruebas Montículo máximo
monticulo1.ingresar(1)
monticulo1.ingresar(8)
monticulo1.ingresar(9)
monticulo1.ingresar(2)
monticulo1.ingresar(3)
monticulo1.ingresar(10)
print("\Recorrido en Pre-Orden Montículo max:")
monticulo1.preOrden(0)
print("Recorrido por niveles Montículo max:")
monticulo1.porNiveles()
print("\nMonticulo máximo:")
monticulo1.imprimir()
monticulo1.eliminar(10)
print("\nMonticulo máximo después de eliminar:")
monticulo1.imprimir()
#Pruebas Montículo mínimo
monticulo2.ingresar(1)
monticulo2.ingresar(8)
monticulo2.ingresar(9)
monticulo2.ingresar(2)
monticulo2.ingresar(3)
monticulo2.ingresar(10)
print("\Recorrido en Pre-Orden Montículo min:")
monticulo2.preOrden(0)
print("Recorrido por niveles Montículo min:")
monticulo2.porNiveles()
print("\nMonticulo mínimo:")
monticulo2.imprimir()   
monticulo2.eliminar(1)
print("\nMonticulo mínimo después de eliminar:") 
monticulo2.imprimir()
   
