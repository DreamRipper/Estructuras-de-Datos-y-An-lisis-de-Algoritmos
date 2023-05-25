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
    
    def agregar_nodo(self, valor):
        newNodo = Nodo(valor)

        if(self.tamaño == 0):
            self.primerNodo = newNodo

        else:
            actNodo = self.primerNodo

            while(actNodo.siguiente != None):
                actNodo = actNodo.siguiente

            actNodo.siguiente = newNodo
        self.tamaño += 1

    def agregar_nodo_eve(self, valor, posicion):
        actNodo = self.primerNodo

        i = 1
        while(i < posicion):
            actNodo = actNodo.siguiente
            i += 1

        actNodo.valor = valor

    def calcular_tamaño(self):
        return self.tamaño
    
    def recorrer_lista(self):
        actNodo = self.primerNodo

        while(actNodo.siguiente != None):
            actNodo = actNodo.siguiente
        return actNodo

    def buscar(self, valor):
        actNodo = self.primerNodo
        apar = 0

        while(actNodo.siguiente != None):
            actNodo = actNodo.siguiente

            if(actNodo.valor == valor):
                apar += 1
            
        print(apar)

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

Lista = LinkedList()

print('\t\t\tMenú\n1.Añadir número a la lista.\n2.Añadir número de la lista en una posición.\n3.Mostrar longitud de la lista.\n4.Eliminar ultimo elemento.\n5.Eliminar elemento en una posición.\n6.Contar número.\n7.Conocer las posiciones de un número.\n8.Mostrar números.\n9.Salir.')

a = True
while(a == True):
     
    menu = input('Digite el número del menú correspondiente a la acción que desea realizar, ¿Qué desea hacer querido usuario?\n')
    menu = (int(menu))

    if(menu == 1):
        valor = input('\nIngrese el valor que desea agregar: ')
        valor = (int(valor))
        Lista.agregar_nodo(valor)

    elif (menu == 2):
        valor = input('\nIngrese el valor que desea agregar: ')
        valor = (int(valor))
            
        posicion = 0
        while(posicion < 1):
            posicion = int(input('\nIngrese la posición en que lo desea agregar:'))

        Lista.agregar_nodo_eve(valor, posicion)

    elif (menu == 3):
        b = Lista.calcular_tamaño()
        print(b)

    elif (menu == 4):
        
        actNodo = Lista.primerNodo
        actNodo2 = Lista.primerNodo.siguiente
        i = 1
        while(actNodo2.siguiente != None):
            actNodo = actNodo.siguiente
            actNodo2 = actNodo2.siguiente
            
        actNodo.siguiente = actNodo2.siguiente
        Lista.tamaño -= 1

    elif (menu == 5):

        posicion = 0
        while(posicion < 1):
            posicion = input('\nIngrese la posición que desea eliminar:')
            posicion = (int(posicion))

            actNodo = Lista.primerNodo
            actNodo2 = Lista.primerNodo.siguiente
            i = 1
            while(i < posicion - 1):
                actNodo = actNodo.siguiente
                actNodo2 =  actNodo2.siguiente
                i += 1 

            actNodo.siguiente = actNodo2.siguiente
            Lista.tamaño -= 1

    elif (menu == 6):

        valor = input('\nIngrese el valor que desea buscar: ')
        valor = (int(valor))

        Lista.buscar(valor)

    elif (menu == 7):
        
        valor = int(input("\nIngrese el número para el cual le indicaré las posiciones: "))
        actNodo = Lista.primerNodo
        pos = 1

        while(actNodo.siguiente != None):

            if(actNodo.valor == valor):
                    
                print(f"El elemento se encuentra en la posición #{pos}")

            actNodo = actNodo.siguiente
            pos += 1
                
    elif (menu == 8):

        actNodo = Lista.primerNodo

        x = "[" + str(actNodo.valor)

        while(actNodo.siguiente != None):
            actNodo = actNodo.siguiente
            x = x + "," + str(actNodo.valor)
            
        x = x + "]"
        print(x)
        
    elif (menu == 9):

        print('¡Gracias por usar el programa!')
        a = False

    else:

        print('error')




           




            


