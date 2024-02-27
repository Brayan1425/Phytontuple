nombre = input("Ingresa tu nombre :")
edad = input("Ingresa tu edad :")
altura = input ("Ingresa tu altura :")
hermanos =input("cuantos hermanos tienes:")

informacion = tuple((nombre,edad,altura,hermanos))
print(f"""La informacion general del usuario es la siguiente : {informacion}""")

education = input("Haz realizado cursos de programacion: (S/N)")
cuantos_cursos = input("Cuantos cursos de programacion he realizado:")
cuales_cursos = input("Cuales son los cursos que he realizado:")

experiencia = tuple((education,cuantos_cursos,cuales_cursos))
 
print(f"""La experiencia laboral que ha tenido es : {experiencia}""")
