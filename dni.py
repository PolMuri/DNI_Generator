# CODI EN ANGLÈS COMENTARIS EN CATALÀ: els comentaris per explicar al detall el codi els faig en la meva llengua materna
# i el codi el faig en anglès per poder ser transportat o reutilitzat a tot arreu eliminant només els comentaris 

# Importa la funció tqdm de la llibreria tqdm per generar la barra de progrés
# al generar el fitxer/llista de DNIs
from tqdm import tqdm 

# Funció per calcular la lletra del DNI basada en un número donat
def calculate_dni_letter(number):
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letters[number % 23]

def generate_all_dnies():
    # Nombre total de combinacions a generar per els DNI(8 dígits)
    total_combinations = 90000000  
    
    try:
        # Obre un fitxer 'all_dnies.txt' per escriure (o crea si no existeix)
        with open('all_dnies.txt', 'w') as file:
            # Utilitzem la llibreria tqdm per mostrar una barra de progrés mentre generem els DNIs, 
            # la funció tqdm() envolta el bucle for i crea una barra de progrés que s'actualitza mentre el bucle avança.
            # total=total_combinations: nombre total de combinacions que es generarà. Aquest valor es passa com a paràmetre a tqdm per indicar la quantitat total d'iteracions.
            # desc="Generant DNIs": posa una descripció de la barra de progrés, que apareixerà quan s'executi el codi
            for number in tqdm(range(10000000, 100000000), total=total_combinations, desc="Generant DNIs"):
                # Crea un DNI amb 8 dígits i la lletra corresponent: crea un string (dni) que és una concatenació 
                # de: la part {number_part:08d} formatarà la part numèrica del DNI com una cadena de 8 dígits, afegint zeros a l'esquerra si cal. 
                # per complir amb el format DNI, la part dreta afegeix la lletra-
                dni = f"{number:08d}{calculate_dni_letter(number)}"
                # Escriu el DNI al fitxer, afegeixent un salt de línia al final
                file.write(f"{dni}\n")
    except Exception as e:
        # Capturem qualsevol excepció que es pugui produir i imprimim el missatge d'error
        print(f"S'ha produït un error: {e}")
    else:
        # Si no hi ha hagut errors, imprimim un missatge d'èxit
        print("Fitxer generat amb èxit.")

# Crida la funció per generar tots els DNIs, és la que inicia l'execució del programa
generate_all_dnies()  





