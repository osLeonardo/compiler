from service import lexico, sintatico

def menu():
  print("Selecione o arquivo a ser processado:")
  print("- 1. Exemplo For")
  print("- 2. Exemplo Repeat")
  print("- 3. Exemplo While")
  print("- 4. Exemplo Declaração de duplicadas")
  print("- 5. Exemplo Identificador não declarado")
  print("- 6. Exemplo Divisão por zero")
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
  elif choice == '4':
    return '../data/content/04.txt'
  elif choice == '5':
    return '../data/content/05.txt'
  elif choice == '6':
    return '../data/content/06.txt'
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