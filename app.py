from random import randint


VALOR_MINIMO = 1
VALOR_MAXIMO = 100


def validar_entrada(mensagem: str, opcoes_validas: tuple, tipo_entrada: str | int) -> str | int:
    entrada = input(mensagem).lower().strip()
    while True:

        if tipo_entrada == str:
            if entrada in opcoes_validas: return entrada
            else:
                print('\nOps! Parece que a opção digitada NÃO existe.'\
                    ' Digite apenas opções válidas.\n')

            
        else:
        
            if entrada.isdigit() or (entrada[0] == '-' and entrada[1:].isdigit()):
                if int(entrada) in opcoes_validas: return int(entrada)
                else: 
                    print('\nOps! Parece que o número digitado'\
                        ' está fora do intervalo permitido.\n')
            else:
                print('\nOps! Parece que você digitou uma opção inválida. Digite APENAS números.\n')

       
        entrada = input(mensagem).lower().strip()


            
       

input("Aperte qualquer ENTER para começar... ")


continuar_programa = 's'
while continuar_programa in ('s','sim'):
    numero_aleatorio = randint(VALOR_MINIMO,VALOR_MAXIMO)
    print(F'foi gerado um número entre {VALOR_MINIMO} e {VALOR_MAXIMO}.')

    escolha_usuario = ''
    while escolha_usuario != numero_aleatorio:

        escolha_usuario = validar_entrada(f'Chute um número de {VALOR_MINIMO} a {VALOR_MAXIMO}: ', 
            tuple(range(VALOR_MINIMO, VALOR_MAXIMO)), int)

        if escolha_usuario < numero_aleatorio:
            print("Chute um numéro maior:")

        elif escolha_usuario > numero_aleatorio:
            print("Chute um numéro menor:")

        else: 
            print(f"PARABÉNS! VOCÊ CHUTOU O VALOR CERTO: {numero_aleatorio}")

        continuar_programa = validar_entrada('Jogo encerrado, gostaria de jogar novamente?(s/n): ',
        ('sim', 'não', 's', 'n'), str)


print(30 * '-')
print('Encerrando o jogo...')
print(30 * '-')
input('Aperte ENTER para finalizar...')


