def validar_codigo(codigo):
    if codigo.strip() == "":
        return False
    return True

def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    return True

def validar_genero(genero):
    if genero.strip() == "":
        return False
    return True

def validar_duracion(duracion):
    try:
        val = int(duracion)
        return val > 0
    except ValueError:
        return False

def validar_clasificacion(clasificacion):
    return clasificacion.upper() in ['A', 'B', 'C']

def validar_idioma(idioma):
    if idioma.strip() == "":
        return False
    return True

def validar_es_3d(es_3d):
    return es_3d.lower() in ['s', 'n']

def validar_precio(precio):
    try:
        val = int(precio)
        return val > 0
    except ValueError:
        return False

def validar_cupos(cupos):
    try:
        val = int(cupos)
        return val >= 0
    except ValueError:
        return False

def leer_opcion():
    """Solicita y tambien valida la opcion seleccionada en el menu principal"""
    try:
        opc_str = input("Ingrese una opcion: ")
        opc = int(opc_str)
        if 1 <= opc <= 6:
            return opc
        else:
            print("Debe seleccionar una opcion que sea valida")
            return None
    except ValueError:
        print("Tiene que seleccionar una opcion valida")
        return None

def buscar_codigo(codigo, cartelera):
    """Verifica si un codigo ya existe en el diccionario (insensible a mayusculas)"""
    for cod in cartelera.keys():
        if cod.upper() == codigo.upper():
            return True
    return False

def cupos_genero(genero, peliculas, cartelera):
    """Opcion 1: La Muestra el total de cupos ya acumulados para un genero especifico"""
    total_cupos = 0
    for cod, datos in peliculas.items():
        if datos[1].lower() == genero.lower():
            if cod in cartelera:
                total_cupos += cartelera[cod][1]  
    print(f"El total de cupos disponibles es de: {total_cupos}")

def busqueda_precio(p_min, p_max, cartelera, peliculas):
    """Opcion 2: Busca peliculas que esten dentro de un rango de precio con cupos > 0"""
    resultados = []
    for cod, datos_cart in cartelera.items():
        precio = datos_cart[0]
        cupos = datos_cart[1]
        
        if p_min <= precio <= p_max and cupos > 0:
            if cod in peliculas:
                titulo = peliculas[cod][0]
                resultados.append(f"{titulo}--{cod}")
                
    if resultados:
        resultados.sort()  
        print(f"Las peliculas que fueron encontradas son: {resultados}")
    else:
        print("No hay peliculas en ese tal rango de precios")


def actualizar_precio(codigo, nuevo_precio, cartelera):
    """Opcion 3: Actualiza el precio si el codigo existe"""
    if buscar_codigo(codigo, cartelera):
        for cod in cartelera.keys():
            if cod.upper() == codigo.upper():
                cartelera[cod][0] = nuevo_precio
                return True
    return False

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
    """Opcion 4: Registra una nueva pelicula en ambos diccionarios si el codigo no existe"""
    if buscar_codigo(codigo, cartelera):
        return False
    
    cod_upper = codigo.upper()
    duracion_int = int(duracion)
    precio_int = int(precio)
    cupos_int = int(cupos)
    es_3d_bool = True if es_3d.lower() == 's' else False
    
    peliculas[cod_upper] = [titulo, genero, duracion_int, clasificacion.upper(), idioma, es_3d_bool]
    cartelera[cod_upper] = [precio_int, cupos_int]
    return True

def eliminar_pelicula(codigo, peliculas, cartelera):
    """Opcion 5: Elimina los registros de una película de en ambos diccionarios"""
    if buscar_codigo(codigo, cartelera):
        key_to_delete = None
        for cod in cartelera.keys():
            if cod.upper() == codigo.upper():
                key_to_delete = cod
                break
        if key_to_delete:
            del peliculas[key_to_delete]
            del cartelera[key_to_delete]
            return True
    return False

def main():
    peliculas = {
        'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
        'P102': ['Noche Neon', 'acción', 125, 'C', 'Ingles', True],
        'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
        'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
        'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
        'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
    }

    cartelera = {
        'P101': [5990, 40],
        'P102': [7990, 0],
        'P103': [4990, 25],
        'P104': [6990, 12],
        'P105': [8990, 8],
        'P106': [7490, 3],
    }

    while True:
        print("========== MENU PRINCIPAL ==========")
        print("1. Cupos por genero")
        print("2. Busqueda de peliculas por el rango de precio")
        print("3. Actualizar el precio de pelicula")
        print("4. Agregar pelicula")
        print("5. Eliminar pelicula")
        print("6. Salir")
        print("===================================")
        
        opcion = leer_opcion()
        if opcion is None:
            continue
            
        if opcion == 1:
            gen = input("Ingrese el genero a consultar: ")
            cupos_genero(gen, peliculas, cartelera)
            
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, cartelera, peliculas)
            
        elif opcion == 3:
            while True:
                cod = input("Ingrese el codigo de pelicula: ")
                while True:
                    try:
                        n_precio = int(input("Ingrese el nuevo precio: "))
                        if n_precio > 0:
                            break
                        else:
                            print("El precio debe ser un valor de entero positivo")
                    except ValueError:
                        print("Debe ingresar un valor entero")
                
                if actualizar_precio(cod, n_precio, cartelera):
                    print("El Precio fue actualizado")
                else:
                    print("El codigo no existe")
                    
                resp = input("¿Desea actualizar el otro precio (s/n)?: ").lower()
              
        elif opcion == 4:
            cod = input("Ingrese el codigo de pelicula: ")
            tit = input("Ingrese titulo: ")
            gen = input("Ingrese el genero: ")
            dur = input("Ingrese la duración (minutos): ")
            cla = input("Ingrese la clasificacion: ")
            idi = input("Ingrese el idioma: ")
            _3d = input("¿Es 3D? (s/n): ")
            pre = input("Ingrese el precio: ")
            cup = input("Ingrese los cupos: ")
            
            if not validar_codigo(cod):
                print("Error: El codigo no puede estar vacio")
            elif not validar_titulo(tit):
                print("Error: El titulo no puede estar vacio")
            elif not validar_genero(gen):
                print("Error: El genero no puede estar vacio")
            elif not validar_duracion(dur):
                print("Errorr: La duracion tiene que ser un numero entero mayor que cero")
            elif not validar_clasificacion(cla):
                print("Error: La clasificacion debe ser exactamente 'A', 'B' o 'C'")
            elif not validar_idioma(idi):
                print("Error: El idioma no puede estar vacio")
            elif not validar_es_3d(_3d):
                print("Error: Debe ingresar 's' o 'n' para indicar si es 3D")
            elif not validar_precio(pre):
                print("Error: El precio debe ser un numero entero mayor que cero")
            elif not validar_cupos(cup):
                print("Error: Los cupos deben ser un numero entero mayor o igual a cero")
            else:
                if agregar_pelicula(cod, tit, gen, dur, cla, idi, _3d, pre, cup, peliculas, cartelera):
                    print("La Pelicula fue agregada")
                else:
                    print("El codigo si ya existe")
                    
        elif opcion == 5:
            cod = input("Ingresa el codigo de la pelicula en eliminar: ")
            if eliminar_pelicula(cod, peliculas, cartelera):
                print("La Pelicula ya fue eliminada")
            else:
                print("El codigo ya no existe")
                
        elif opcion == 6:
            print("El Programa ha sido finalizado")
            break

if __name__ == "__main__":
    main()