import cmath

# ==========================================
# FUNÇÕES DE FORMATAÇÃO E MATEMÁTICA BÁSICA
# ==========================================
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
        return 'Erro: Divisão por zero não é permitida'
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

# ==========================================
# FUNÇÕES DE GESTÃO FINANCEIRA
# ==========================================
def calcular_lucro(receitas, despesas):
    return receitas - despesas

def calcular_receita_necessaria(lucro_desejado, despesas):
    return lucro_desejado + despesas

def calcular_despesa_maxima(receitas, lucro_desejado):
    return receitas - lucro_desejado

def calcular_margem_lucro(lucro_liquido, receitas):
    if receitas == 0:
        return 0
    return (lucro_liquido / receitas) * 100

def calcular_roi(ganho_investimento, custo_investimento):
    if custo_investimento == 0:
        return 0
    return ((ganho_investimento - custo_investimento) / custo_investimento) * 100

# ==========================================
# CORPO PRINCIPAL DA CALCULADORA
# ==========================================
def calculadora():
    # Adicionada a opção 'financeiro'
    equacao = input('''Digite o tipo de operação desejada, lembre-se de colocar os sinais: 
(-, +, /, *, **, raiz_q, raiz_c, baskara, tabuada, financeiro) = ''').lower()

    if equacao == 'baskara':
        print('\nEx: ±a.X² ±b.X ±c = 0')
        n1 = int(input('Digite o valor de A: '))
        n2 = int(input('Digite o valor de B: '))
        n3 = int(input('Digite o valor de C: '))

        parte1 = potenciacao(n2, 2)
        multi1 = multiplicacao(4, n1)
        parte2 = multiplicacao(multi1, n3)

        delta = parte1 - parte2

        print('\nΔ = b² - 4.a.c')
        print(f'Δ = {n2}² - 4.{n1}.{n3}')
        print(f'Δ = {parte1} - {parte2}')
        print(f'Δ = {delta}\n')
        print('(-b ± ²√Δ) ÷ 2.a')

        resul_delta = raiz_quadrada(delta)
        print(f'(-{n2} ± ²√{delta}) ÷ 2.{n1} = 0')
        resul_div = 2 * n1
        print(f'(-{n2} ± {formatar_resultado(resul_delta)}) ÷ {resul_div} = 0\n')
             
        x1 = subtracao(-n2, resul_delta)
        print(f'(-{n2} - {formatar_resultado(resul_delta)}) ÷ {resul_div}')
        resultado_x1 = divisao(x1, resul_div)
        print(f'Resultado do x1: {formatar_resultado(resultado_x1)}\n')

        x2 = soma(-n2, resul_delta)
        # Correção aqui: usando formatar_resultado para evitar erro com números complexos
        print(f'(-{n2} + {formatar_resultado(resul_delta)}) ÷ {resul_div}')
        resultado_x2 = divisao(x2, resul_div)
        print(f'Resultado de x2: {formatar_resultado(resultado_x2)}\n')
    
    elif equacao == 'tabuada':
        limite = int(input('Qual o limite da tabuada? '))
        numero_base = float(input('Qual o valor base para a tabuada? '))

        for i in range(limite + 1):
            resultado = multiplicacao(numero_base, i)
            # Correção aqui: substituído 'limite' por 'i' no print
            print(f'{numero_base} x {i} = {resultado}')

    elif equacao in ['+', '-', '/', '*', '**']:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))

        if equacao == '+':
            resultado = soma(n1, n2)
            print(f'{n1} + {n2} = \nResultado: {resultado}')

        elif equacao == '-':
            resultado = subtracao(n1, n2)
            print(f'{n1} - {n2} = \nResultado: {resultado}')

        elif equacao == '/':
            resultado = divisao(n1, n2)
            print(f'{n1} / {n2} = \nResultado: {resultado}')

        elif equacao == '*':
            resultado = multiplicacao(n1, n2)
            print(f'{n1} * {n2} = \nResultado: {resultado}')

        elif equacao == '**':
            resultado = potenciacao(n1, n2)
            print(f'{n1} ** {n2} = \nResultado: {resultado}')

    elif equacao == 'raiz_q':
        n1 = float(input('Digite o número: '))
        resultado = raiz_quadrada(n1)
        print(f'²√{n1} = {formatar_resultado(resultado)}')

    elif equacao == 'raiz_c':
        n1 = float(input('Digite o número: '))
        resultado = raiz_cubica(n1)
        print(f'³√{n1} = {resultado:.2f}')

    # ==========================================
    # NOVO BLOCO: GESTÃO FINANCEIRA
    # ==========================================
    elif equacao == 'financeiro':
        print("\n---  MENU DE GESTÃO FINANCEIRA ---")
        print("1. Análise de Lucro/Receita/Despesa (Álgebra)")
        print("2. Calcular Margem de Lucro")
        print("3. Calcular ROI (Retorno sobre Investimento)")
        
        opcao_fin = input("Escolha uma opção financeira (1-3): ")
        
        try:
            if opcao_fin == '1':
                print("\nO que você quer descobrir?")
                print("A. O Lucro Líquido")
                print("B. A Receita Necessária")
                print("C. A Despesa Máxima")
                
                sub_opcao = input("Escolha (A, B ou C): ").upper()
                
                if sub_opcao == 'A':
                    receita = float(input("Digite a Receita (R$): "))
                    despesa = float(input("Digite a Despesa (R$): "))
                    print(f"Seu Lucro é: R$ {calcular_lucro(receita, despesa):.2f}")
                elif sub_opcao == 'B':
                    lucro = float(input("Digite o Lucro desejado (R$): "))
                    despesa = float(input("Digite a Despesa atual (R$): "))
                    print(f"Sua Receita precisa ser de: R$ {calcular_receita_necessaria(lucro, despesa):.2f}")
                elif sub_opcao == 'C':
                    receita = float(input("Digite a Receita atual (R$): "))
                    lucro = float(input("Digite o Lucro desejado (R$): "))
                    print(f"Sua Despesa máxima deve ser: R$ {calcular_despesa_maxima(receita, lucro):.2f}")
                else:
                    print("Opção inválida.")
                    
            elif opcao_fin == '2':
                receita = float(input("Digite a receita total (R$): "))
                lucro = float(input("Digite o lucro líquido (R$): "))
                print(f"Sua Margem de Lucro é: {calcular_margem_lucro(lucro, receita):.2f}%")
                
            elif opcao_fin == '3':
                ganho = float(input("Ganho obtido com o investimento (R$): "))
                custo = float(input("Custo inicial do investimento (R$): "))
                print(f"O ROI foi de: {calcular_roi(ganho, custo):.2f}%")
            else:
                print("Opção inválida no menu financeiro.")
                
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos para contas financeiras.")

    else:
        print('Digite uma operação válida!')

# Inicia o programa
calculadora()