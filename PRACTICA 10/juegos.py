
info_tienda = ("¡Game On!", 2010)
inventario = {
    "god of war": {"precio": 800, "stock": 5},
    "mortal kombat": {"precio": 1200, "stock": 3},
    "resident evil": {"precio": 600, "stock": 10}
}

print("Precio del segundo juego:", inventario["mortal kombat"]["precio"])

inventario["mortal kombat"]["stock"] -= 1
print("Vendiste una copia de Mortal kombat. Stock actual:", inventario["mortal kombat"]["stock"])













