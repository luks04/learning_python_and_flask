def foo_example():
    file = None
    file_path = ""

    if file is not None:
        # If the file exists, close it
        file.close()
    elif file_path is None:
        # If the file path not exists, define it
        file_path = './new_path'

def files():
    # 'r' antes de definir una cadena de texto indica que esta debe interpretarse como un texto crudo
    with open(r'/Users/lucaspatino/Documents/Luks_Learning/Learning_Projects/example_file.txt', 'w') as file:
        file.write("Primera linea")
        file.write("\nSegunda linea")
        file.write("\nTercera linea")
    with open(r'/Users/lucaspatino/Documents/Luks_Learning/Learning_Projects/example_file.txt', 'r') as file:
        print(file.read())
    with open(r'/Users/lucaspatino/Documents/Luks_Learning/Learning_Projects/example_file.txt', 'r') as file:
        print(file.readlines())
    with open(r'/Users/lucaspatino/Documents/Luks_Learning/Learning_Projects/example_file.txt', 'rb') as file:
        for linea in file:
            print(linea)
    with open(r'/Users/lucaspatino/Documents/Luks_Learning/Learning_Projects/example_file.txt', 'r') as file:
        palabras = list()
        for linea in file:
            palabras_linea = linea.split()
            palabras.extend(palabras_linea[:])
        print(palabras)

'''
'r' -> Open a file for reading (default)
'w' -> Open a file for writing
'x' -> Open a file for exclusive creation. If the file already exists, the operation fails
'a' -> Open a file for appending at the end of the file. Creates a new file if it does not exist
'+' -> Open a file for updating (reading and writing)
't' -> Open file in text mode (default)
'b' -> Open file in binary mode
'''

if __name__ == "__main__":
    files()
