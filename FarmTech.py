# FARMTECH SOLUTIONS - FASE 1 CAP 1
# Integrante: André Frederick Abreu Lima
# RM: 576424
#
# Este programa trabalha com duas culturas: Soja e Milho.
# Os dados são guardados em listas, que serão usadas como vetores.

# Criamos os vetores vazios para guardar os dados cadastrados.
culturas = []
areas = []
insumos = []
doses = []
quantidades = []

# Criamos a variável opcao para controlar o menu.
opcao = 0

# O while mantém o programa funcionando até o usuário escolher a opção 5.
while opcao != 5:

    # Mostramos o menu na tela.
    print("\nFARMTECH SOLUTIONS")
    print("1 - Entrada de dados")
    print("2 - Saída de dados")
    print("3 - Atualizar dados")
    print("4 - Deletar dados")
    print("5 - Sair do programa")

    # Recebemos a opção escolhida pelo usuário.
    opcao = int(input("Escolha uma opção: "))

    # Se a opção for 1, o usuário poderá cadastrar uma cultura.
    if opcao == 1:

        # Mostramos as duas culturas disponíveis.
        print("\nEscolha a cultura:")
        print("1 - Soja")
        print("2 - Milho")

        # Recebemos a cultura escolhida.
        tipo_cultura = int(input("Digite 1 ou 2: "))

        # Se o usuário escolher 1, trabalhamos com Soja.
        if tipo_cultura == 1:

            # Guardamos o nome da cultura em uma variável.
            cultura = "Soja"

            # Para a Soja, consideramos uma área retangular.
            comprimento = float(input("Digite o comprimento do terreno em metros: "))
            largura = float(input("Digite a largura do terreno em metros: "))

            # Calculamos a área em metros quadrados.
            area_m2 = comprimento * largura

            # Convertemos metros quadrados para hectares.
            area_ha = area_m2 / 10000

            # Definimos o insumo utilizado na Soja.
            insumo = "Fertilizante NPK"

            # O usuário informa quantos quilos do produto são usados por hectare.
            dose = float(input("Digite a dose de fertilizante em kg por hectare: "))

            # Calculamos a quantidade total de fertilizante necessária.
            quantidade = area_ha * dose

            # Adicionamos os dados nos vetores.
            culturas.append(cultura)
            areas.append(area_ha)
            insumos.append(insumo)
            doses.append(dose)
            quantidades.append(quantidade)

            # Mostramos o resultado do cadastro.
            print("\nCadastro realizado com sucesso.")
            print("Cultura:", cultura)
            print("Área em hectares:", area_ha)
            print("Insumo:", insumo)
            print("Quantidade necessária:", quantidade, "kg")

        # Se o usuário escolher 2, trabalhamos com Milho.
        elif tipo_cultura == 2:

            # Guardamos o nome da cultura em uma variável.
            cultura = "Milho"

            # Para o Milho, consideramos uma área triangular.
            base = float(input("Digite a base do terreno em metros: "))
            altura = float(input("Digite a altura do terreno em metros: "))

            # Calculamos a área do triângulo em metros quadrados.
            area_m2 = (base * altura) / 2

            # Convertemos metros quadrados para hectares.
            area_ha = area_m2 / 10000

            # Definimos o insumo utilizado no Milho.
            insumo = "Fertilizante NPK"

            # O usuário informa quantos quilos do produto são usados por hectare.
            dose = float(input("Digite a dose de fertilizante em kg por hectare: "))

            # Calculamos a quantidade total de fertilizante necessária.
            quantidade = area_ha * dose

            # Adicionamos os dados nos vetores.
            culturas.append(cultura)
            areas.append(area_ha)
            insumos.append(insumo)
            doses.append(dose)
            quantidades.append(quantidade)

            # Mostramos o resultado do cadastro.
            print("\nCadastro realizado com sucesso.")
            print("Cultura:", cultura)
            print("Área em hectares:", area_ha)
            print("Insumo:", insumo)
            print("Quantidade necessária:", quantidade, "kg")

        # Se o usuário digitar outra opção, mostramos uma mensagem de erro.
        else:
            print("Opção de cultura inválida.")

    # Se a opção for 2, mostramos os dados cadastrados.
    elif opcao == 2:

        # Verificamos se existe algum dado cadastrado.
        if len(culturas) == 0:
            print("\nNenhum dado cadastrado.")

        # Se existirem dados, usamos for para percorrer os vetores.
        else:
            print("\nDADOS CADASTRADOS")

            # O for percorre todas as posições dos vetores.
            for i in range(len(culturas)):
                print("\nPosição:", i)
                print("Cultura:", culturas[i])
                print("Área em hectares:", areas[i])
                print("Insumo:", insumos[i])
                print("Dose por hectare:", doses[i])
                print("Quantidade total:", quantidades[i], "kg")

    # Se a opção for 3, atualizamos um registro existente.
    elif opcao == 3:

        # Verificamos se existem dados para atualizar.
        if len(culturas) == 0:
            print("\nNenhum dado cadastrado para atualizar.")

        # Se existirem dados, mostramos as posições disponíveis.
        else:
            for i in range(len(culturas)):
                print(i, "-", culturas[i], "-", areas[i], "hectares")

            # O usuário escolhe a posição que deseja alterar.
            posicao = int(input("Digite a posição que deseja atualizar: "))

            # Verificamos se a posição existe no vetor.
            if posicao >= 0 and posicao < len(culturas):

                # Recebemos os novos valores.
                nova_area = float(input("Digite a nova área em hectares: "))
                novo_insumo = input("Digite o novo nome do insumo: ")
                nova_dose = float(input("Digite a nova dose por hectare: "))

                # Atualizamos os dados na posição escolhida.
                areas[posicao] = nova_area
                insumos[posicao] = novo_insumo
                doses[posicao] = nova_dose

                # Recalculamos a quantidade total do insumo.
                quantidades[posicao] = nova_area * nova_dose

                print("Dados atualizados com sucesso.")

            # Se a posição não existir, mostramos uma mensagem.
            else:
                print("Posição inválida.")

    # Se a opção for 4, deletamos um registro dos vetores.
    elif opcao == 4:

        # Verificamos se existem dados para deletar.
        if len(culturas) == 0:
            print("\nNenhum dado cadastrado para deletar.")

        # Se existirem dados, mostramos as posições disponíveis.
        else:
            for i in range(len(culturas)):
                print(i, "-", culturas[i], "-", areas[i], "hectares")

            # O usuário escolhe a posição que deseja apagar.
            posicao = int(input("Digite a posição que deseja deletar: "))

            # Verificamos se a posição existe.
            if posicao >= 0 and posicao < len(culturas):

                # Apagamos a mesma posição em todos os vetores.
                del culturas[posicao]
                del areas[posicao]
                del insumos[posicao]
                del doses[posicao]
                del quantidades[posicao]

                print("Dados deletados com sucesso.")

            # Se a posição não existir, mostramos uma mensagem.
            else:
                print("Posição inválida.")

    # Se a opção for 5, encerramos o programa.
    elif opcao == 5:
        print("\nPrograma encerrado.")

    # Se o usuário digitar uma opção diferente de 1 a 5, mostramos um aviso.
    else:
        print("\nOpção inválida. Digite um número de 1 a 5.")
