integrantes = [
    {"nombre": "Diego", "apellido": "Escobar"},
    {"nombre": "Sebastian", "apellido": "Espinoza"},
    {"nombre": "Alfredo", "apellido": "Hernandez"}

]

# Imprimir lista de nombres y apellidos
for integrante in integrantes:
    nombre_completo = integrante["nombre"] + " " + integrante["apellido"]
    print(nombre_completo)
