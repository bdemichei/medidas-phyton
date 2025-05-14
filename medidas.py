def descobrir_tamanho():
    nome = input("Digite seu nome: ")

    try:
        busto = float(input("Digite sua medida de busto em cm: "))
        cintura = float(input("Digite sua medida de cintura em cm: "))
        quadril = float(input("Digite sua medida de quadril em cm: "))

        # tamanho do busto
        if 82 <= busto <= 88:
            tamanho_busto = "P"
        elif 88 <= busto <= 94:
            tamanho_busto = "M"
        elif 94 <= busto <= 100:
            tamanho_busto = "G"
        else:
            tamanho_busto = "fora do padrão"

        # tamanho da cintura
        if 62 <= cintura <= 68:
            tamanho_cintura = "P"
        elif 68 <= cintura <= 74:
            tamanho_cintura = "M"
        elif 74 <= cintura <= 80:
            tamanho_cintura = "G"
        else:
            tamanho_cintura = "fora do padrão"

        # tamanho do quadril
        if 90 <= quadril <= 96:
            tamanho_quadril = "P"
        elif 96 <= quadril <= 100:
            tamanho_quadril = "M"
        elif 100 <= quadril <= 106:
            tamanho_quadril = "G"
        else:
            tamanho_quadril = "fora do padrão"

        print(f"\nOlá, {nome}!")

        # Verifica se todas as medidas estão dentro dos padrões
        if "fora do padrão" in (tamanho_busto, tamanho_cintura, tamanho_quadril):
            print("Algumas medidas estão fora dos padrões. Por favor, entre em contato para um ajuste personalizado.")
        else:
            print(f"Seu tamanho ideal é:")
            print(f"- Busto: {tamanho_busto}")
            print(f"- Cintura: {tamanho_cintura}")
            print(f"- Quadril: {tamanho_quadril}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos para as medidas.")

# Executar o programa
descobrir_tamanho()
