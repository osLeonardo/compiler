from service import lexico, sintatico

def menu():
  print("Selecione o arquivo a ser processado:")
  print("- 1. Exemplo 01.txt")
  print("- 2. Exemplo 02.txt")
  print("- 3. Exemplo 03.txt")  
  print("- 9. Tudo.txt")
  print("- 0. Sair")
  choice = input("> ")

  if choice == '0':
    exit()
  elif choice == '1':
    return '../data/content/01.txt'
  elif choice == '2':
    return '../data/content/02.txt'
  elif choice == '3':
    return '../data/content/03.txt'
  elif choice == '9':
    return '../data/content/tudo.txt'
  else:
    print("Input inváido.")
    exit()

print('===== MENU =====')
file_path = menu()

print('\n')
print('===== LÉXICO =====')
tokens, lines, lexemas = lexico.lexico(file_path)

print('\n')
print('===== SINTÁTICO =====')
sintatico.sintatico(tokens, lines, lexemas)