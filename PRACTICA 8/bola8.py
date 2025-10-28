import random
nombre=input("ingrese su nombre: ")
print("hola", nombre)

pregunta=input("pregunta lo que quieras saber a la bola: ")

respuestas = [
    "si",
    "no",
    "quizas",
    "no estoy seguro",
    "es probable que si",
    "definitivamente no",
    "posiblemente",
    "no lo creo",
    "es probable que no",
    "definitivamente si",
    "algun dia",
    "es decididamente asi",
    "sin lugar a dudas",
    "puedes confiar en ello",
    "las señales apuntan a que si",
    "vuelve a preguntar mas tarde",
    "no cuentes con ello",
    "concentrate y vuelve a preguntar",
    "muy dudoso",
    "mi respuesta es definitivamente no"
]

print(random.choice(respuestas))

while True:
    respuesta=input("desea seguir preguntando a la bola 8: ")
    if respuesta=='no' or respuesta=='NO':
        break











