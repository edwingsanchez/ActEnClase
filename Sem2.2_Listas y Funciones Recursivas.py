#6. Pilas y Colas

# Pilas (Stacks)
class Pila:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() if not self.esta_vacia() else None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def tamaño(self):
        return len(self.items)

# Colas (Queues)
class Cola:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop() if not self.esta_vacia() else None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def tamaño(self):
        return len(self.items)




#7. Algoritmos de ordenamiento para listas
#7.1 Metodo por insercion
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#7.2 Metodo por seleccion
# El método de selección es un algoritmo de ordenamiento que divide la lista en dos partes: la parte ordenada y la parte no ordenada. En cada iteración, el algoritmo selecciona el elemento más pequeño de la parte no ordenada y lo intercambia con el primer elemento de esa parte, moviendo así el límite entre las partes ordenada y no ordenada.  
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#7.3 Metdodo Burbuja
# El método de burbuja es un algoritmo de ordenamiento que compara cada par de elementos adyacentes en una lista y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que la lista esté completamente ordenada. El nombre "burbuja" proviene del hecho de que los elementos más grandes "flotan" hacia el final de la lista con cada iteración, similar a las burbujas que suben a la superficie del agua.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


#8. Quick Sort
# El algoritmo de ordenamiento rápido, conocido como Quick Sort, es un método eficiente para ordenar listas. Funciona utilizando la técnica de divide y vencerás, donde se selecciona un elemento llamado "pivote" y se particiona la lista en dos sublistas: una con elementos menores al pivote y otra con elementos mayores. Luego, se aplica recursivamente el mismo proceso a cada sublista hasta que todas las sublistas estén ordenadas, lo que resulta en una lista completamente ordenada.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)





#9. busquedas
#9.1 Busqueda Lineal
# La búsqueda lineal, también conocida como búsqueda secuencial, es un algoritmo de búsqueda que recorre una lista o arreglo de elementos de manera secuencial, comparando cada elemento con el valor objetivo hasta encontrar una coincidencia o llegar al final de la lista. Este método es simple pero puede ser ineficiente para listas grandes, ya que su tiempo de ejecución es proporcional al tamaño de la lista (O(n)).
def busqueda_lineal(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


#9.2 Busqueda Binaria
# La búsqueda binaria es un algoritmo de búsqueda eficiente que se utiliza en listas ordenadas. Funciona dividiendo repetidamente la lista en mitades y comparando el valor objetivo con el elemento del medio. Si el valor objetivo es igual al elemento del medio, se ha encontrado la coincidencia. Si el valor objetivo es menor, se continúa la búsqueda en la mitad inferior de la lista; si es mayor, se busca en la mitad superior. Este proceso se repite hasta encontrar el valor o determinar que no está presente en la lista, con una complejidad de tiempo de O(log n).
def busqueda_binaria(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


#10. Notacion Big O
# La notación Big O es una forma de describir la complejidad algorítmica de un algoritmo, expresando 
# cómo el tiempo de ejecución o el espacio requerido por el algoritmo crece en función del tamaño de la entrada.
# Se utiliza para clasificar algoritmos según su eficiencia, permitiendo comparar diferentes algoritmos y entender su comportamiento a medida que la entrada aumenta. Por ejemplo, un algoritmo con complejidad O(n) se considera lineal, mientras que uno con O(n^2) se considera cuadrático, indicando que el tiempo de ejecución crece más rápidamente a medida que aumenta el tamaño de la entrada.


#11. Funciones interativas y Recursivas
#11.1 Factorial
def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Caso recursivo

print(factorial(5))  # 120


#11.2 Fibonacci
def fibonacci(n):
    if n <= 1:  # Caso base
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Caso recursivo

print(fibonacci(6))  # 8


#11.3 Suma de una lista
def suma_lista(arr):
    if len(arr) == 0:  # Caso base
        return 0
    else:
        return arr[0] + suma_lista(arr[1:])  # Caso recursivo

print(suma_lista([1, 2, 3, 4]))  # 10


#11.4 Busqueda Binaria Recursiva
def busqueda_binaria(arr, objetivo, izq, der):
    if izq > der:  # Caso base
        return -1
    medio = (izq + der) // 2
    if arr[medio] == objetivo:  # Caso base
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria(arr, objetivo, medio + 1, der)  # Recursivo
    else:
        return busqueda_binaria(arr, objetivo, izq, medio - 1)  # Recursivo
    


#12. Torres de Hanoi
def torres_de_hanoi(n, origen, destino, auxiliar):
    if n == 1:  # Caso base
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        torres_de_hanoi(n - 1, origen, auxiliar, destino)  # Mover n-1 discos a la torre auxiliar
        print(f"Mover disco {n} de {origen} a {destino}")  # Mover el disco más grande al destino
        torres_de_hanoi(n - 1, auxiliar, destino, origen)  # Mover los n-1 discos desde la torre auxiliar al destino


#14. Funcion Finbonachi Recursiva
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


#15. Serie de fibonachi
def fibonacci_serie(n):
    serie = []
    for i in range(n):
        serie.append(fibonacci_recursivo(i))
    return serie

print(fibonacci_serie(10))  # Imprime los primeros 10 números de la serie de Fibonacci