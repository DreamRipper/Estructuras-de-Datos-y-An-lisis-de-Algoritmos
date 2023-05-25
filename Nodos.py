class Nodo:

    def __init__(self, valor):     
        self.valor = valor
        self.siguiente = None

    def devolver_valor(self):
        print(self.valor)

    def asignar_siguiente(self, nodo):
        self.siguiente = nodo

    def cambiar_valor(self, nuevo_valor):
        self.valor = nuevo_valor

class LinkedList:

    def __init__(self):
        self.tamaño = 0
        self.primerNodo = None
    
    def agregar_nodo_inicio(self, valor):
        newNodo = Nodo(valor)

        if(self.tamaño == 0):
            self.primerNodo = newNodo

        else:
            newNodo.siguiente = self.primerNodo
            self.primerNodo = newNodo
                
        self.tamaño += 1

    def agregar_nodo_final(self, valor):
        newNodo = Nodo(valor)
        actNodo = self.primerNodo

        while(actNodo.siguiente != None):
            actNodo = actNodo.siguiente

        actNodo.siguiente = newNodo
        self.tamaño += 1

    def calcular_tamaño(self):
        self.tamaño
    
    def recorrer_lista(self):
        actNodo = self.primerNodo

        while(actNodo.siguiente != None):
            print(actNodo)
            actNodo = actNodo.siguiente

    def buscar(self, valor):
        actNodo = self.primerNodo

        while(actNodo.siguiente != None):
            actNodo = actNodo.siguiente

            if(actNodo.valor == valor):
                print(actNodo.valor)
                return False

    def eliminar(self, valor):
        
        if(self.tamaño == 0):
            return False
        
        else:
            actNodo = self.primerNodo

            while(actNodo.siguiente.valor != valor):
                if(actNodo.siguiente == None):
                    print('El valor no se encuentra en la lista.')
                    return False

                else:
                    actNodo = actNodo.siguiente
            
            delNodo = actNodo.siguiente
            actNodo.siguiente = delNodo.siguiente

        self.tamaño -= 1

        return delNodo



