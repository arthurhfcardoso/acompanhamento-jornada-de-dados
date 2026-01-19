# Desafio: Cálculo de Bônus com Entrada do Usuário

# Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# Para resolver os bugs identificados — tratamento de entradas inválidas
# que não podem ser convertidas para um número de ponto flutuante e
# prevenção de valores negativos para salário e bônus, você pode modificar
# o código diretamente.
# Isso envolve adicionar verificações adicionais após a tentativa de conversão
# para garantir que os valores sejam positivos.

# Pseudocódigo

# BASE_KPI = 1000

# repete:
#     pedir nome
#     se nome invalido:
#         avisar e repetir nome
#     senao:
#         sair do loop do nome

# repete:
#     pedir salario
#     tentar converter para numero
#     se erro ou salario < 0:
#         avisar e repetir salario
#     senao:
#         sair do loop do salario

# repete:
#     pedir bonus_percentual (ex: 1.5)
#     tentar converter para numero
#     se erro ou bonus_percentual < 0:
#         avisar e repetir bonus_percentual
#     senao:
#         bonus = bonus_percentual / 100
#         sair do loop do bonus

# kpi_bonus = BASE_KPI + salario * bonus
# imprimir mensagem final (com bonus_percentual e kpi_bonus)

BASE_KPI = 1000


def brl(valor):
    formatted = f"R$ {valor:,.2f}"
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


while True:
    nome = input("Digite seu nome: ").strip()
    if nome:
        break
    else:
        print("Nome invalido. Por favor, tente novamente.")
while True:
    try:
        salario = float(input("Digite o valor do seu salário mensal: "))
        if salario < 0:
            print("Salário não pode ser negativo. Por favor, tente novamente.")
        else:
            break
    except ValueError:
        print(
            "Entrada inválida. Por favor, insira um número válido "
            "para o salário."
        )
while True:
    try:
        bonus_percentual = float(
            input(
                "Digite o valor do bônus recebido (em percentual, ex: 1.5 "
                "para 1.5%): "
            )
        )
        if bonus_percentual < 0:
            print("Bônus não pode ser negativo. Por favor, tente novamente.")
        else:
            bonus = bonus_percentual / 100
            break
    except ValueError:
        print(
            "Entrada inválida. Por favor, insira um número válido "
            "para o bônus."
        )
kpi_bonus = BASE_KPI + salario * bonus
mensagem = (
    f"Olá {nome}, o seu valor bônus foi de {brl(kpi_bonus)} "
    f"(com bônus de {bonus_percentual:.1f}%)."
)
print(mensagem)
