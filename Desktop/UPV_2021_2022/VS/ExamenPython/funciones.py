import random

#Hecho
def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta funciÃ³n devuelve la lista de palabras que empiezan por una letra que 
    alfabÃ©ticamente estÃ¡ antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    resultado=[]
    for clave in diccionario:
        for palabra in diccionario[clave]:
            if palabra[0] < letra:
                resultado.append(palabra)
    return resultado


#hecho
def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta funciÃ³n inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    clients_list.update ( {
        nif: {'name': name,
              'address': address,
              'phone': phone,
              'email': email
        }
    } )


#hecho
def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un nÃºmero de repeticiones, esta funciÃ³n selecciona 5 cartas aleatorias de esta baraja y las mete 
    en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    
    combinaciones={}
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales 
        combinaciones["repeticion"+str(i)]=[]
        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            combinaciones["repeticion"+str(i)].append(carta)

    return combinaciones

