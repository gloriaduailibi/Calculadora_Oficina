# Menu principal da calculadora

try:
    import calc_basico
except ImportError:
    calc_basico = None
    print("Módulo calc_basico não encontrado.")

while True:
    print("\n====== CALCULADORA ======")
    print("1 - Operações Básicas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # ---------------- BÁSICO ----------------
    if opcao == "1":

        if calc_basico is None:
            print("Módulo não disponível.")
            continue

        print("\n--- Operações Básicas ---")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Potência")

        escolha = input("Escolha a operação: ")

        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if escolha == "1":
            resultado = calc_basico.somar(a, b)
            operador = "+"

        elif escolha == "2":
            resultado = calc_basico.subtrair(a, b)
            operador = "-"

        elif escolha == "3":
            resultado = calc_basico.multiplicar(a, b)
            operador = "*"

        elif escolha == "4":
            resultado = calc_basico.dividir(a, b)
            operador = "/"

        elif escolha == "5":
            resultado = calc_basico.potencia(a, b)
            operador = "^"

        else:
            print("Opção inválida.")
            continue

        print(f"Resultado: {a} {operador} {b} = {resultado}")

    # ---------------- SAIR ----------------
    elif opcao == "0":
        print("Calculadora encerrada.")
        break

    else:
        print("Opção inválida.")
