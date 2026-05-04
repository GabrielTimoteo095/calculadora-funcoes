import cmath

def formatar_resultado(valor):
    if isinstance(valor, complex):
        real = valor.real
        imag = valor.imag
        sinal = " + " if imag >= 0 else " - "
        return f"({real:.2f}{sinal}{abs(imag):.2f}j)"
    else:
        return f"{valor:.2f}"

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def divisao(n1, n2):
    if n2 == 0:
        return 'Erro: Divisão por zero não é permitido'
    return n1 / n2

def multiplicacao(n1, n2):
    return n1 * n2

def potenciacao(n1, n2):
    return n1 ** n2

def raiz_quadrada(n1):
    if n1 < 0:
        return cmath.sqrt(n1)
    return n1 ** 0.5

def raiz_cubica(n1):
    return n1 ** (1/3)

def calculadora():

    equacao = input('''Digite o tipo de equação desejada, lembre-se de colocar os sinais: 
                    -, +, /, *, **, raiz_q, raiz_c, baskara, tabuada ''')

    if equacao == 'baskara':

        print('\nEx: ±a.X² ±b.X ±c = 0')
        n1 = int(input('Digite o valor de A: '))
        n2 = int(input('Digite o valor de B: '))
        n3 = int(input('Digite o vlaor de C: '))

        parte1 = potenciacao(n2, 2)
        multi1 = multiplicacao(4, n1)
        parte2 = multiplicacao(multi1, n3)

        delta = parte1 - parte2

        print('\nΔ = b2 - 4.a.c')
        print(f'Δ = {n2}² - 4.{n1}.{n3} ')
        print(f'Δ = {parte1} - {parte2}')
        print(f'Δ = {delta}\n')
        print('(-b ± ²√Δ) ÷ 2.a')

        resul_delta = raiz_quadrada(delta)
        print(f'(-{n2} ± ²√{delta}) ÷ 2.{n1} = 0 ')
        resul_div = 2 * n1
        print(f'(-{n2} ± {formatar_resultado(resul_delta)}) ÷ {resul_div} = 0\n')
             
        x1 = subtracao(-n2, resul_delta)
        print(f'(-{n2} - {formatar_resultado(resul_delta)}) ÷ {resul_div}')
        resultado_x1 = divisao(x1, resul_div)
        print(f'Resultado do x1: {formatar_resultado(resultado_x1)}\n')

        x2 = soma(-n2, resul_delta)
        print(f'(-{n2} + {resul_delta:.2f}) ÷ {resul_div}')
        resultado_x2 = divisao(x2, resul_div)
        print(f'Resultado de x2: {formatar_resultado(resultado_x2)}\n')
    
    elif equacao == 'tabuada':
        limite = int(input('Até que número vai sua tabuada? '))
        numero_base = float(input('Qual o número que irá ser feito a tabuada?'))

        for i in range(limite + 1):
            resultado = multiplicacao(numero_base, i)
            print(f'{numero_base} x {limite} = {resultado}')

    elif equacao in ['+', '-', '/', '*', '**']:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))

        if equacao == '+':
            resultado = soma(n1, n2)
            print(f'{n1} + {n2} =')
            print(f"Resultado: {resultado}")

        elif equacao == '-':
            resultado = subtracao(n1, n2)
            print(f'{n1} - {n2} =')
            print(f"Resultado: {resultado}")

        elif equacao == '/':
            resultado = divisao(n1, n2)
            print(f'{n1} / {n2} =')
            print(f"Resultado: {resultado}")

        elif equacao == '*':
            resultado = multiplicacao(n1, n2)
            print(f'{n1} * {n2} =')
            print(f"Resultado: {resultado}")

        elif equacao == '**':
            resultado = potenciacao(n1, n2)
            print(f'{n1} ** {n2} =')
            print(f"Resultado: {resultado}")

    elif equacao == 'raiz_q':
        n1 = float(input('Digite o primeiro número: '))
        resultado = raiz_quadrada(n1)
        print(f'²√{n1} = {resultado}')

    elif equacao == 'raiz_c':
        n1 = float(input('Digite o primeiro número: '))
        resultado = raiz_cubica(n1)
        print(f"³√{n1}: {resultado}")

    else:
        print('Digite um número válido!')

calculadora()