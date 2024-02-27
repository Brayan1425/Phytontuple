direccion = input(" Confirma la direccion donde tu vives: ")
dire_papas= input("cual es la direccion de tus padres: ")
dire_abuelos= input("cual es la direccion de tus abuelos: ")
pareja_dire= input("cual es la direccion de tu pareja: ")

informacion= tuple((dire_abuelos,dire_papas,direccion,pareja_dire))

print(f"""Estas son las direcciones de tu familia: {informacion}""")