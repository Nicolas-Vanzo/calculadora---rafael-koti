import math
import time 



while True:
    metodo = input('''\nEscolha a operação: 
        [1] Soma (+)
        [2] Subtração (-) 
        [3] Multiplicação (x)
        [4] Divisão (÷)
        [5] Raiz quadrada (√)
        [6] Porcentagem (%)
        [7] Potência (^)
        [8] Seno (sen(x))
        [9] Cosseno (cos(x))
        [10] Tangente (tg(x))
        [11] Hipotenusa (C)
        [0] Sair
        Escolha uma das opções acima: ''')

    if metodo == '0':
        print('Encerrando a calculadora.')
        
        break
        
    match metodo:
        case '1' | '2' | '3' | '4':
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))

            match metodo:
                case '1':
                    print(f'A soma de {n1} + {n2} é {n1 + n2}')
                case '2':
                    print(f'A subtração de {n1} - {n2} é {n1 - n2}')
                case '3':
                    print(f'A multiplicação de {n1} * {n2} é {n1 * n2}')
                case '4':
                    if n2 == 0:
                        print('Divisão por zero não é permitida.')
                    else:
                        print(f'A divisão de {n1} ÷ {n2} é {n1 / n2}')

        case '5':
            numero = float(input('Digite um número: '))
            if numero < 0:
                print('Não é possível calcular a raiz de número negativo.')
            else:
                print(f'A raiz quadrada de {numero} é {math.sqrt(numero):.2f}')

        case '6':
            numero = float(input('Digite o número base: '))
            porcentagem = float(input('Digite a porcentagem (%): '))
            print(f'{porcentagem}% de {numero} é {numero * porcentagem / 100:.2f}')

        case '7':
            base = float(input('Digite a base: '))
            expoente = float(input('Digite o expoente: '))
            print(f'{base} elevado a {expoente} é {math.pow(base, expoente):.2f}')

       
        case '8':
                    ang = int(input('Digite o ângulo: '))
                    rad = math.radians(ang)
                    seno = math.sin(rad)
                    print('O seno do ângulo de {} é de {}.'.format(ang, seno))


        case '9':
                    ang = int(input('Digite o ângulo: '))
                    rad = math.radians(ang)
                    cos = math.cos(rad)

        case '10':
                    ang = int(input('Digite o ângulo: '))
                    rad = math.radians(ang)
                    tg = math.tan(rad)
                    print('A tângente do ângulo de {} é de {}.'.format(ang, tg))

        case '11':
                    co = int(input('Digite o valor do cateto oposto: '))
                    ca = int(input('Digite o valor do cateto adjacente: '))
                    hip = (ca ** 2 + co ** 2) ** (1/2)
                    print('*'*25 + '\n')

                    print('O valor da hipotenusa é: {}'.format(hip))
       
    print('Aguarde...') 
    time.sleep(3)
    print('tmj pae')
       
    