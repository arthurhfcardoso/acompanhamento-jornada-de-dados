import sys


def ex01():
    # Soma dois numeros inteiros inseridos pelo usuario.
    tentativas = 0

    while tentativas < 3:
        try:
            Numero1 = int(input("Digite o primeiro numero inteiro: "))
            Numero2 = int(input("Digite o segundo numero inteiro: "))
            print("A soma dos numeros e", Numero1 + Numero2)
            break  # sai quando deu certo
        except ValueError:
            print("Erro: Por favor, insira apenas numeros inteiros.")
            tentativas += 1
    else:
        print("Numero maximo de tentativas atingido.")


def ex02():
    # Recebe um numero e calcula o resto da divisao desse numero por 5.
    numero = int(input("Digite um numero inteiro: "))
    resto = numero % 5
    print("O resto da divisao de", numero, "por 5 e", resto)


def ex03():
    # Multiplica dois numeros fornecidos pelo usuario e mostra o resultado.
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    resultado = numero1 * numero2
    print("O resultado da multiplicacao e", f"{resultado:.2f}")


def ex04():
    # Pede dois numeros inteiros e imprime a divisao inteira
    # do primeiro pelo segundo.
    n1 = int(input("Digite o primeiro numero inteiro: "))
    n2 = int(input("Digite o segundo numero inteiro: "))
    divisao_inteira = n1 // n2
    print("A divisao inteira de", n1, "por", n2, "e", divisao_inteira)


def ex05():
    # Calcula o quadrado de um numero fornecido pelo usuario.
    n = float(input("Digite um numero: "))
    quadrado = n**2
    print("O quadrado de", n, "e", quadrado)


def ex06():
    # Recebe dois numeros flutuantes e realiza a adicao.
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))
    soma = n1 + n2
    print("A soma de", n1, "e", n2, "e", soma)


def ex07():
    # Calcula a media de dois numeros flutuantes fornecidos pelo usuario.
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))
    media = (n1 + n2) / 2
    print("A media de", n1, "e", n2, "e", media)


def ex08():
    # Calcula a potencia de um numero (base e expoente fornecidos
    # pelo usuario).
    base = float(input("Digite o numero base: "))
    expoente = float(input("Digite o expoente: "))
    potencia = base**expoente
    print("A potencia de", base, "elevado a", expoente, "e", potencia)


def ex09():
    # Converte a temperatura de Celsius para Fahrenheit.
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("A temperatura em Fahrenheit e", fahrenheit)


def ex10():
    # Calcula a area de um circulo, recebendo o raio como entrada.
    import math

    raio = float(input("Digite o raio do circulo: "))
    area = math.pi * (raio**2)
    print("A area do circulo e", area)


def ex11():
    # Recebe uma string e a converte para maiusculas.
    frase = input("Digite uma frase: ")
    print(frase.upper())


def ex12():
    # Recebe o nome completo do usuario e imprime tudo em minusculas.
    nome_completo = input("Digite seu nome completo: ")
    print(nome_completo.lower())


def ex13():
    # Recebe uma frase e imprime sem espacos no inicio e no fim.
    frase = input("Digite uma frase: ")
    print(frase.strip())


def ex14():
    # Recebe uma data "dd/mm/aaaa" e imprime dia, mes e ano separadamente.
    data = input("Digite uma data no formato dd/mm/aaaa: ")
    dia, mes, ano = data.split("/")
    print("Dia:", dia)
    print("Mes:", mes)
    print("Ano:", ano)


def ex15():
    # Concatena duas strings fornecidas pelo usuario.
    nome = input("Digite o seu nome: ")
    sobrenome = input("Digite o seu sobrenome: ")
    print(f"Nome completo: {nome} {sobrenome}")


def ex16():
    # Avalia duas expressoes booleanas e retorna o resultado do AND.
    exp1 = input("Digite true ou false: ").strip().lower()
    bool1 = exp1 == "true"
    exp2 = input("Digite true ou false: ").strip().lower()
    bool2 = exp2 == "true"

    resultado = bool1 and bool2
    print("O resultado do AND e:", resultado)


def ex17():
    # Recebe dois valores booleanos e retorna o resultado do OR.
    exp1 = input("Digite o primeiro booleano: ").strip().lower()
    bool1 = exp1 == "true"
    exp2 = input("Digite o segundo booleano: ").strip().lower()
    bool2 = exp2 == "true"
    resultado = bool1 or bool2
    print("O resultado do OR e:", resultado)


def ex18():
    # Recebe um valor booleano e inverte esse valor.
    exp1 = input("Digite um booleano: ").strip().lower()
    bool1 = exp1 == "true"
    resultado = not bool1
    print("O valor invertido e:", resultado)


def ex19():
    # Compara se dois numeros fornecidos pelo usuario sao iguais.
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))
    iguais = n1 == n2
    print("A comparacao dos numeros e", iguais)


def ex20():
    # Verifica se dois numeros fornecidos pelo usuario sao diferentes.
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))
    diferentes = n1 != n2
    if diferentes:
        print("Os numeros sao diferentes.")
    else:
        print("Os numeros sao iguais.")


def ex21():
    # Conversor de temperatura.

    input_temperature = input(
        "Digite '1' para converter Celsius para Fahrenheit ou '2' "
        "para converter Fahrenheit para Celsius: "
    )
    if input_temperature == "1":
        celsius_para_fahrenheit = float(
            input("Digite a temperatura em Celsius: ")
        )
        fahrenheit = (celsius_para_fahrenheit * 9 / 5) + 32
        print(
            f"{celsius_para_fahrenheit:.0f} Celsius e "
            f"{fahrenheit:.0f} Fahrenheit"
        )

    elif input_temperature == "2":
        fahrenheit_para_celsius = float(
            input("Digite a temperatura em Fahrenheit ")
        )
        celsius = (fahrenheit_para_celsius - 32) * 5 / 9
        print(
            f"{fahrenheit_para_celsius:.0f} Fahrenheit e "
            f"{celsius:.0f} Celsius"
        )


def ex22():
    # Verificador de palindromo.
    texto = input("Digite uma palavra ou frase: ")
    texto_limpo = "".join(filter(str.isalnum, texto)).lower()
    texto_invertido = texto_limpo[::-1]

    if texto_limpo == texto_invertido:
        print("A palavra/frase e um palindromo.")
    else:
        print("A palavra/frase nao e um palindromo.")


def ex23():
    # Calculadora simples.
    n1 = float(input("Digite o primeiro numero: "))
    n2 = float(input("Digite o segundo numero: "))
    operacao = input("Digite a operacao (+, -, *, /): ")

    if operacao == "+":
        print("Resultado:", n1 + n2)
    elif operacao == "-":
        print("Resultado:", n1 - n2)
    elif operacao == "*":
        print("Resultado:", n1 * n2)
    elif operacao == "/":
        print("Resultado:", n1 / n2)
    else:
        print("Operacao invalida.")


def ex24():
    # Classificador de numeros.
    numero = float(input("Digite um numero: "))
    if numero > 0:
        print("O numero e positivo.")
    elif numero < 0:
        print("O numero e negativo.")
    else:
        print("O numero e zero.")


def ex25():
    # Conversao de tipo com validacao.
    entrada = input("Digite um numero inteiro: ")
    try:
        numero_inteiro = int(entrada)
        print("Voce digitou o numero inteiro:", numero_inteiro)
    except ValueError:
        print("Erro: Entrada invalida. Por favor, insira um numero inteiro.")


EXERCICIOS = {
    "ex01": ex01,
    "ex02": ex02,
    "ex03": ex03,
    "ex04": ex04,
    "ex05": ex05,
    "ex06": ex06,
    "ex07": ex07,
    "ex08": ex08,
    "ex09": ex09,
    "ex10": ex10,
    "ex11": ex11,
    "ex12": ex12,
    "ex13": ex13,
    "ex14": ex14,
    "ex15": ex15,
    "ex16": ex16,
    "ex17": ex17,
    "ex18": ex18,
    "ex19": ex19,
    "ex20": ex20,
    "ex21": ex21,
    "ex22": ex22,
    "ex23": ex23,
    "ex24": ex24,
    "ex25": ex25,
}


def main():
    if len(sys.argv) < 2:
        print("Uso: python exercicios.py ex01")
        print("Opcoes:", ", ".join(EXERCICIOS.keys()))
        return

    nome = sys.argv[1]
    func = EXERCICIOS.get(nome)
    if func is None:
        print(f"Exercicio invalido: {nome}")
        print("Opcoes:", ", ".join(EXERCICIOS.keys()))
        return

    func()


if __name__ == "__main__":
    main()
