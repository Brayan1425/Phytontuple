education = input("¿Haz realizado cursos de programacion?:(S/N) ")
cuantos_cursos = input("¿cuantos cursos de programacion he realizado?: ")
cuales_cursos = input("¿cuales son los cursos que he realizado?:")

experiencia = tuple((education,cuantos_cursos,cuales_cursos))
print(f""""la informacion sobre los cursos realizados es :{experiencia}""")