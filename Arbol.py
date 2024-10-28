from collections import deque
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol():
    def es_vacio(self):
        return self._raiz == None
    
    def __init__(self):
        self._raiz = None
    
    def __del__(self):
        self._raiz = None

    def regresaRaiz(self):
        return self._raiz
    
    def insertarNodo(self, valor):
        new_nodo = Nodo(valor)
        if self._raiz is None:
            self._raiz = new_nodo
            return 
        
        nodo_actual = self._raiz
        
        while True:
            if valor < nodo_actual.valor:
                if nodo_actual.izquierda is None:
                    nodo_actual.izquierda = new_nodo
                    return
                nodo_actual = nodo_actual.izquierda

            elif valor > nodo_actual.valor:
                if nodo_actual.derecha is None:
                    nodo_actual.derecha = new_nodo
                    return
                nodo_actual = nodo_actual.derecha
    
    def mostrar_acostado(self, nodo_actual, nivel=0):
        if self._raiz is None:
            print("Arbol vacio")

        if nodo_actual is None:
            return
        
        self.mostrar_acostado(nodo_actual.derecha, nivel+1)
        print(" " * nivel, nodo_actual.valor, sep="")
        self.mostrar_acostado(nodo_actual.izquierda, nivel+1)
        
    def busqueda(self, x, nodo_actual):
        if nodo_actual is None:
            return False
        elif x < nodo_actual.valor:
            return self.busqueda(x, nodo_actual.izquierda)
        elif x > nodo_actual.valor:
            return self.busqueda(x, nodo_actual.derecha)
        else:
            return True

    def Preorder(self, nodo_actual):
        if nodo_actual is None:
            return
        print(" ", nodo_actual.valor, end=" ")
        self.Preorder(nodo_actual.izquierda)
        self.Preorder(nodo_actual.derecha)
   
    def inOrder(self, nodo_actual):
        if nodo_actual is None:
            return
        
        self.inOrder(nodo_actual.izquierda)
        print(" ", nodo_actual.valor, end=" ")
        self.inOrder(nodo_actual.derecha)

    def Posorder(self, nodo_actual):
        if nodo_actual is None:
            return
        self.Posorder(nodo_actual.izquierda)
        self.Posorder(nodo_actual.derecha)
        print(" ", nodo_actual.valor, end=" ")

    def elimPredecesor(self, valor):
        self._raiz = self._eliminarPredecesor(self._raiz, valor)

    def _eliminarPredecesor(self, nodo_actual, valor):
        if nodo_actual is None:
            return
        
        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminarPredecesor(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminarPredecesor(nodo_actual.derecha, valor)
        else:
            if nodo_actual.izquierda is None and nodo_actual.derecha is None:
                return
            
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            if nodo_actual.derecha is None:
                return nodo_actual.izquierda
            
            predecesor = self._encontrarmaximo(nodo_actual.izquierda)
            nodo_actual.valor = predecesor.valor

            nodo_actual.izquierda = self._eliminarPredecesor(nodo_actual.izquierda, predecesor.valor)

        return nodo_actual
    
    def _encontrarmaximo(self, nodo_actual):
        while nodo_actual.derecha is not None:
            nodo_actual = nodo_actual.derecha
        return nodo_actual
    
    def elimSucesor(self, valor):
        self._raiz = self._eliminarSucesor(self._raiz, valor)

    def _eliminarSucesor(self, nodo_actual, valor):
        if nodo_actual is None:
            return
        
        if valor < nodo_actual.valor:
            nodo_actual.izquierda = self._eliminarSucesor(nodo_actual.izquierda, valor)
        elif valor > nodo_actual.valor:
            nodo_actual.derecha = self._eliminarSucesor(nodo_actual.derecha, valor)
        else:
            if nodo_actual.izquierda is None and nodo_actual.derecha is None:
                return
            
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            if nodo_actual.derecha is None:
                return nodo_actual.izquierda

            sucesor = self._encontrarminimo(nodo_actual.derecha)
            nodo_actual.valor = sucesor.valor

            nodo_actual.derecha = self._eliminarSucesor(nodo_actual.derecha, sucesor.valor)

        return nodo_actual         
            
    def _encontrarminimo(self, nodo_actual):
        while nodo_actual.izquierda is not None:
            nodo_actual = nodo_actual.izquierda
        return nodo_actual
        
    def Amplitud(self):
        if self._raiz is None:
            return
        
        cola = deque([self._raiz])

        while cola:
            nodo_actual = cola.popleft()
            print(nodo_actual.valor, end=" ")

            if nodo_actual.izquierda is not None:
                cola.append(nodo_actual.izquierda)
            if nodo_actual.derecha is not None:
                cola.append(nodo_actual.derecha)

    def Altura(self, nodo_actual):
        if nodo_actual is None:
            return 0
        
        return (1 + max(self.Altura(nodo_actual.izquierda), self.Altura(nodo_actual.derecha)))
    
    def contar_hojas(self, nodo_actual):
        if nodo_actual is None:
            return 0
        if nodo_actual.izquierda is None and nodo_actual.derecha is None:
            return 1
        return self.contar_hojas(nodo_actual.izquierda) + self.contar_hojas(nodo_actual.derecha)
        
    def contar_nodos(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return 1 + self.contar_nodos(nodo_actual.izquierda) + self.contar_nodos(nodo_actual.derecha)
    
    def completo(self, nodo_actual):
        if self._raiz is None:
            return
        
        cola = deque([self._raiz])
        end = False

        while cola:
            nodo_actual = cola.popleft()

            if nodo_actual:
                if end:
                    return False
                
                cola.append(nodo_actual.izquierda)
                cola.append(nodo_actual.derecha)
            else:
                end = True
        return True
    
    def Lleno(self, nodo_actual):
        if nodo_actual is None:
            return True
        
        if nodo_actual.izquierda is None and nodo_actual.derecha is None:
            return True
        
        if nodo_actual.izquierda and nodo_actual.derecha:
            return self.Lleno(nodo_actual.izquierda) and self.Lleno(nodo_actual.derecha)
        
        return False
    
    def podarArbol(self, nodo_actual):
        if nodo_actual is None:
            return
        
        self.podarArbol(nodo_actual.izquierda)
        self.podarArbol(nodo_actual.derecha)

        del nodo_actual
        return None

    def graficar_arbol(self):
        if self._raiz is None:
            print("El árbol está vacío.")
            return
        
        plt.figure(figsize=(10, 6))
        self._graficar_nodo(self._raiz, 0, 0, 1, plt.gca())
        plt.axis('off')
        plt.show()

    def _graficar_nodo(self, nodo, x, y, dx, ax):
        if nodo is not None:
            ax.text(x, y, str(nodo.valor), ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))
            if nodo.izquierda is not None:
                ax.plot([x, x - dx], [y - 0.1, y - 0.3], 'k-')
                self._graficar_nodo(nodo.izquierda, x - dx, y - 0.3, dx / 2, ax)
            if nodo.derecha is not None:
                ax.plot([x, x + dx], [y - 0.1, y - 0.3], 'k-')
                self._graficar_nodo(nodo.derecha, x + dx, y - 0.3, dx / 2, ax)

def menu():
    arbol = Arbol()
    listopciones = [
        "---- Menu de Opciones ----",
        "[1] Insertar elemento", 
        "[2] Mostrar arbol completo con raiz en la izquierda",
        "[3] Grafique arbol", 
        "[4] Busque un elemento en el arbol",
        "[5] Recorra el arbol en PreOrder",
        "[6] Recorra el arbol en inOrder",
        "[7] Recorra el arbol en PosOrder",
        "[8] Eliminar un nodo del arbol Predecesor",
        "[9] Eliminar un nodo del arbol Sucesor",
        "[10] Recorrer el arbol por niveles",
        "[11] Altura del arbol",
        "[12] Cantidad de hojas del arbol",
        "[13] Cantidad de nodos del arbol",
        "[14] Revisar si es un arbol binario completo",
        "[15] Revisar si es un arbol binario lleno",
        "[16] Podar el arbol",
        "[0] Salir"
    ]
    
    print("\n".join(listopciones))
    while True:
        opcion = input("\nIngrese la opcion en el menu: ")
        
        match opcion:
            case "1":
                valor = int(input("Ingrese un elemento al arbol: "))
                arbol.insertarNodo(valor)
            case "2":
                arbol.mostrar_acostado(arbol._raiz)
            case "3":
                arbol.graficar_arbol()
            case "4":
                valor = int(input("Ingrese el elemento a buscar: "))
                if arbol.busqueda(valor, arbol._raiz):
                    print(f"El elemento {valor} se encuentra en el árbol.")
                else:
                    print(f"El elemento {valor} no se encuentra en el árbol.")
            case "5":
                print("Recorrido en PreOrder:")
                arbol.Preorder(arbol._raiz)
                print()  
            case "6":
                print("Recorrido en inOrder:")
                arbol.inOrder(arbol._raiz)
                print()  
            case "7":
                print("Recorrido en PosOrder:")
                arbol.Posorder(arbol._raiz)
                print()  
            case "8":
                valor = int(input("Ingrese el nodo a eliminar (Predecesor): "))
                arbol.elimPredecesor(valor)
                print(f"El nodo {valor} ha sido eliminado (si existía).")
            case "9":
                valor = int(input("Ingrese el nodo a eliminar (Sucesor): "))
                arbol.elimSucesor(valor)
                print(f"El nodo {valor} ha sido eliminado (si existía).")
            case "10":
                print("Recorrido por niveles:")
                arbol.Amplitud()
                print() 
            case "11":
                altura = arbol.Altura(arbol._raiz)
                print(f"La altura del árbol es: {altura}")
            case "12":
                cantidad_hojas = arbol.contar_hojas(arbol._raiz)
                print(f"La cantidad de hojas del árbol es: {cantidad_hojas}")
            case "13":
                cantidad_nodos = arbol.contar_nodos(arbol._raiz)
                print(f"La cantidad de nodos del árbol es: {cantidad_nodos}")
            case "14":
                if arbol.completo(arbol._raiz):
                    print("El árbol es completo.")
                else:
                    print("El árbol no es completo.")
            case "15":
                if arbol.Lleno(arbol._raiz):
                    print("El árbol es lleno.")
                else:
                    print("El árbol no es lleno.")
            case "16":
                arbol.podarArbol(arbol._raiz)
                arbol._raiz = None  
                print("El árbol ha sido podado.")
            case "0":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

menu()

