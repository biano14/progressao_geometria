def progressao_geometrica(a1, razao, n):
    for i in range(n):
        termo = a1 * (razao ** i)
        print(termo, end=' - ')
    print('Fim')

# Exemplo de uso:
while True:
    primeiro_termo = float(input('Informe o primeiro termo (a1): '))
    razao = float(input('Informe a razão da PG: '))
    quantidade_termos = int(input('Informe a quantidade de termos que deseja ver: '))
    
    progressao_geometrica(primeiro_termo, razao, quantidade_termos)
    
    opcao = input('Deseja calcular outra progressão (s/n): ').lower()
    if opcao == 's':
        continue
    else:
        break  