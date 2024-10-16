print("Arzaba Diaz April")
print("3W")
print("1173")
#esta linea slicitara información al usuario
nombre = input("introduce tu nombre: ")
edad = input("introduce tu edad: ")
direccion = input("introduce tu dirección: ")
telefono = input("introduce tu número de teléfono: ")

#esta linea gardara la información en un diccionario
usuario = {
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
}

#esta linea mstrara la información
mensaje = f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}"
print(mensaje)
