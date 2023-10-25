import random as rm

n = input("presiona enter para lanzar los dados: ")
while n=="":
    if n == "":
        a,b =rm.randrange(1,6), rm.randrange(1,6)
        c = a+b
        print(f"Los dados dieron: {a}, {b}; la suma de {a} + {b} es: {c}")
        n= input("¿Quieres lanzar otra vez? Sí: Presiona enter, No: Presiona cualquier tecla: ")
    else: 
        print("Fin del Programa")
print("Fin del juego")