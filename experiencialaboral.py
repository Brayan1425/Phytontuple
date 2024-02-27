work = input("¿Haz tenido experiencia laboral en el mundo de la programacion (S/N)?: ")
oportunidades = input("¿cuales han sido tus puestos a desempeñar: ")
nombres_empresas = input("Nombre las empresas en las que has laburado : ")

info_exp_laboral= tuple((work,oportunidades,nombres_empresas))

print(f"""La experiencia laboral que has tenido es: {info_exp_laboral}""")