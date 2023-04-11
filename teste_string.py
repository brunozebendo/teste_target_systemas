"""o código pede que o usuário digite uma string, depois usa a função fatiamento :: por toda a palavra
 usando o -1 para inverter a palavra e guardá-la na variável que depois é impressa"""

string = input("Digite uma palavra: ")
string_invertida = string[::-1]
print( f'aqui está sua palavra ao contrário:' " " + string_invertida)