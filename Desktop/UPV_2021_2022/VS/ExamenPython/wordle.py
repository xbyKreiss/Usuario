import random
def choose_secret(filename):
    """Dado un nombre de fichero, esta funciÃ³n devuelve una palabra aleatoria de este fichero transformada a mayÃºsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayÃºsculas. Ej. "CREMA"
    """
    f = open(filename, mode="rt", encoding="utf-8")

    palabras=[]
    for line in f:
        line = line.upper()
        line = line.split()
        palabras.extend(line)#concatenar listas
    f.close()

    aleatorio=random.choice(palabras)
    print(aleatorio)
    return aleatorio

    
res1=choose_secret("ExamenPython\\palabras_reduced.txt")
print(res1)
    
def compare_words(word, secret):
    """Dadas dos palabras en mayÃºsculas (word y secret), esta funciÃ³n calcula las posiciones de las letras de word que aparecen en la misma posiciÃ³n en secret,
     y las posiciones de las letras de word que aparecen en secret pero en una posiciÃ³n distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posiciÃ³n en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras estÃ¡n en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """

    same_position=[]
    #mustra una posicion que no esta
    for letra1 in word:
        for letra2 in secret:
            if letra1 == letra2 and word.index(letra1) == word.index(letra1):
                same_position.append(secret.index(letra2))
                #print(secret.index(letra2))
                
    #return same_position
    same_letter=[]
    for letra1 in word:
        for letra2 in secret:
            if letra1==letra2:
                same_letter.append(word.index(letra1))

    return same_position, same_letter
    
    


res2=compare_words("CURRO", "CUUMO")
print(res2)

l1=[0]
l2=[1,2]
def print_word(word,same_letter_position,same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta funciÃ³n crearÃ¡ un string donde aparezcan en mayÃºsculas 
    las letras de la palabra que ocupen las posiciones de same_position, en minÃºsculas las letras de la palabra que ocupen las posiciones 
    de same_letter y un guiÃ³n (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    transformed=[]

    for letra in word:
        for poscionIgual in l1:
            if word.index(letra) == poscionIgual:
                transformed.append(letra)

    for letra in word:
        for posicionNoIgual in l2:
            if word.index(letra) == posicionNoIgual:
                transformed.append(letra.lower())

    while len(transformed) < 5:
        transformed.append("-")
    
    return transformed



res3 =print_word("CAMPO", l1, l2)
print(res3)

def choose_secret_advanced(filename):
    """Dado un nombre de fichero, esta funciÃ³n filtra solo las palabras de 5 letras que no tienen acentos (Ã¡,Ã©,Ã­,Ã³,Ãº). 
    De estas palabras, la funciÃ³n devuelve una lista de 15 aleatorias no repetidas y una de estas 15, 
    se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayÃºsculas
    """


    f = open(filename, mode="rt", encoding="utf-8")

    lista=[]
    for line in f:
        line = line.upper()
        line = line.split()
        lista.extend(line)#concatenar listas
    f.close()
    
    

    selected=[]
    listaExcepciones = ["Ã¡","Ã©","Ã­","Ã³","Ãº"]
    while len(selected) < 15:
        aleatorio=random.choice(lista)
        for excepciones in listaExcepciones:
            if excepciones not in aleatorio and aleatorio not in selected:
                selected.append(aleatorio) 
    
    secret = random.choice(selected)

    return selected, secret
                        
                        


res4=choose_secret_advanced("ExamenPython\\palabras_extended.txt")
print(res1)
 
def check_valid_word():
    """Dada una lista de palabras, esta funciÃ³n pregunta al usuario que introduzca una palabra hasta que introduzca una que estÃ© en la lista. Esta palabra es la que devolverÃ¡ la funciÃ³n.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que estÃ¡ en la lista.
    """

if __name__ == "__main__":
    secret=choose_secret("ExamenPython\\palabras_reduced.txt")
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words()
        resultado=print_word()
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   