from service import lexico, sintatico

def menu():
  print("Selecione o arquivo a ser processado:")
  print("1. Exemplo 01.txt")
  print("2. Exemplo 02.txt")
  print("3. Exemplo 03.txt")
  print("9. Sair")
  choice = input("Enter your choice: ")

  if choice == '1':
    return '../data/content/01.txt'
  elif choice == '2':
    return '../data/content/02.txt'
  elif choice == '3':
    return '../data/content/03.txt'
  elif choice == '9':
    exit()
  else:
    print("Input inváido.")
    exit()

file_path = menu()

tokens = lexico.lexico(file_path)
print(tokens)

sintatico.sintatico(tokens)