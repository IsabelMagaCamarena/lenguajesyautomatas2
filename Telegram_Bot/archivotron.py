def busca_arreglo(busca):
    print(f"Buscando arreglo:{busca}")
    arreglo_palabras=["husky","pug","labrador","poddle"]

    for item in arreglo_palabras:
        print(f"Palabra:{item}")
        if busca == item:
            print("palabra encontrada")
            return"Encontrada en el arreglo"
    return "No se encontro en el arreglo"
        
def busca_in_file(busca):
    file = open('palabras.txt','r')
    if busca in file.read():
        print("lo encontre con file read")
        return "Se encontro en el archivo de palabras"
    file = open('groserias.txt','r')
    if busca in file.read():
        print("lo encontre con file read")
        return "Dijiste una mala palabra,se encontro en el archivo de groserias"
    file = open('especiales.txt','r')
    if busca in file.read():
        print("lo encontre con file read")
        return "Dijiste una palabra especial,se encontro en el archivo de especiales"
    file.close()
    return "No se encuentra esa palabra,porfavor digame otra"

def busca_with_file(busca):
    with open('palabras.txt')as file:
        data = True
        while data:
            data - file.readline()
            print(data)
