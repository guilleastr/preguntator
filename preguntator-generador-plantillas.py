num_preguntas=int(input("Numero de preguntas que va a haber: "))
num_respuestas=int(input("Numero de respuestas por pregunta: "))
nombre=str(input("Nombre del fichero: "))

plantilla= open(nombre, "w")
opciones=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z"]
plantilla.write(num_preguntas+";\n")
for i in range(0, num_preguntas):
    plantilla.write(str(i)+". \n")
    for j in range(0, num_respuestas):
        plantilla.write(opciones[j]+") \n")

plantilla.close()
