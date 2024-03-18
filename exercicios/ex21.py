name = 'Ayrton Polegario'
print(name[0:1:2])
print(name.count('o'))
print(len(name))
print(name.find('rio'))
print(name.replace('Polegario','Pacheco'))#Faz a troca de algo por outra coisa.
print(name.lower())#A string toda fica em minusculo.
print(name.upper())#A string toda fica em maiusculo.
print(name.capitalize())#A primeira palavra da string fica em CAPSLOCK (maiusculo) e o resto minusculo.
print(name.title())#Deixa toda primeira palavra em maiusculo, sempre a primeira. ex: (Dia De Abril)
print(name.strip())#Remove todo espaço a mais na string, ou seja, desnecessário.
print(name.rstrip())#Remove apenas o espaço a mais do lado direito. (USANDO a letra r no começo do strip)
print(name.lstrip())#Remove apenas o espaço a mais do lado esquerdo. (USANDO a letra l no começo do strip)
print(name.split())#Ele cria uma lista para cada palavra na sua string. (Ayrton = vai de 0 ate 5) (Polegario = vai de 0 ate 8)
print('-'.join(name))#Ele junta todas as strings, separando apenas por -
