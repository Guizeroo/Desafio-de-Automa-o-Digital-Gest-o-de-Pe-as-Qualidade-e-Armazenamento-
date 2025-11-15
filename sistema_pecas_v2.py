# Sistema de Gestão de Peças - Controle de Qualidade e Armazenamento
# Disciplina: Algoritmos e Lógica de Programação
# Desafio de Automação Digital

# Listas para guardar as peças
pecas_aprovadas = []
pecas_reprovadas = []
caixas_fechadas = []
caixa_atual = []
numero_caixa = 1

def cadastrar_peca():
    print("\n=== CADASTRAR NOVA PEÇA ===")
    
    # Pega o ID da peça
    id_peca = input("Digite o ID da peça: ")
    
    # Pega o peso e valida
    while True:
        try:
            peso = float(input("Digite o peso da peça (em gramas): "))
            if peso <= 0:
                print("Erro: O peso deve ser maior que zero!")
            else:
                break
        except:
            print("Erro: Digite um número válido para o peso!")
    
    # Pega a cor e valida
    while True:
        cor = input("Digite a cor da peça (azul ou verde): ")
        cor = cor.lower()
        if cor == "azul" or cor == "verde":
            break
        else:
            print("Erro: A cor deve ser 'azul' ou 'verde'!")
    
    # Pega o comprimento e valida
    while True:
        try:
            comprimento = float(input("Digite o comprimento da peça (em cm): "))
            if comprimento <= 0:
                print("Erro: O comprimento deve ser maior que zero!")
            else:
                break
        except:
            print("Erro: Digite um número válido para o comprimento!")
    
    # Agora vou verificar se a peça está aprovada ou não
    aprovada = True
    motivos = []
    
    # Verifica o peso (tem que estar entre 95 e 105)
    if peso < 95 or peso > 105:
        aprovada = False
        motivos.append(f"Peso fora do padrão ({peso}g - deve estar entre 95g e 105g)")
    
    # Verifica a cor (só pode ser azul ou verde)
    if cor != "azul" and cor != "verde":
        aprovada = False
        motivos.append("Cor inválida (deve ser azul ou verde)")
    
    # Verifica o comprimento (tem que estar entre 10 e 20)
    if comprimento < 10 or comprimento > 20:
        aprovada = False
        motivos.append(f"Comprimento fora do padrão ({comprimento}cm - deve estar entre 10cm e 20cm)")
    
    # Cria um dicionário com os dados da peça
    peca = {
        'id': id_peca,
        'peso': peso,
        'cor': cor,
        'comprimento': comprimento
    }
    
    # Se aprovada, adiciona na lista de aprovadas e na caixa
    if aprovada:
        pecas_aprovadas.append(peca)
        adicionar_na_caixa(peca)
        print(f"\nPeça {id_peca} APROVADA e adicionada à caixa {numero_caixa}!")
    else:
        # Se reprovada, adiciona os motivos e coloca na lista de reprovadas
        peca['motivos_reprovacao'] = motivos
        pecas_reprovadas.append(peca)
        print(f"\nPeça {id_peca} REPROVADA!")
        print("Motivos da reprovação:")
        for motivo in motivos:
            print(f" - {motivo}")

def adicionar_na_caixa(peca):
    global caixa_atual, numero_caixa
    
    # Adiciona a peça na caixa atual
    caixa_atual.append(peca)
    
    # Verifica se a caixa já tem 10 peças
    if len(caixa_atual) == 10:
        print(f"\nCAIXA {numero_caixa} CHEIA! Fechando caixa...")
        
        # Cria uma nova caixa fechada com as peças
        caixa_fechada = {
            'numero': numero_caixa,
            'pecas': []
        }
        
        # Copia as peças para a caixa fechada
        for p in caixa_atual:
            caixa_fechada['pecas'].append(p)
        
        caixas_fechadas.append(caixa_fechada)
        
        # Limpa a caixa atual e aumenta o número
        caixa_atual = []
        numero_caixa += 1
        print(f"Nova caixa {numero_caixa} iniciada.")

def listar_pecas():
    print("\n=== LISTAGEM DE PEÇAS ===")
    
    # Lista as peças aprovadas
    print(f"\n--- PEÇAS APROVADAS ({len(pecas_aprovadas)}) ---")
    if len(pecas_aprovadas) == 0:
        print("Nenhuma peça aprovada ainda.")
    else:
        for peca in pecas_aprovadas:
            print(f"ID: {peca['id']} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
    
    # Lista as peças reprovadas
    print(f"\n--- PEÇAS REPROVADAS ({len(pecas_reprovadas)}) ---")
    if len(pecas_reprovadas) == 0:
        print("Nenhuma peça reprovada ainda.")
    else:
        for peca in pecas_reprovadas:
            print(f"ID: {peca['id']} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
            # Mostra os motivos da reprovação
            print(f" Motivos: ", end="")
            for i in range(len(peca['motivos_reprovacao'])):
                if i > 0:
                    print(", ", end="")
                print(peca['motivos_reprovacao'][i], end="")
            print()

def remover_peca():
    print("\n=== REMOVER PEÇA ===")
    id_remover = input("Digite o ID da peça que deseja remover: ")
    
    # Procura primeiro nas peças aprovadas
    encontrou = False
    for i in range(len(pecas_aprovadas)):
        if pecas_aprovadas[i]['id'] == id_remover:
            pecas_aprovadas.pop(i)
            print(f"Peça {id_remover} removida da lista de aprovadas!")
            encontrou = True
            break
    
    # Se não encontrou, procura nas reprovadas
    if not encontrou:
        for i in range(len(pecas_reprovadas)):
            if pecas_reprovadas[i]['id'] == id_remover:
                pecas_reprovadas.pop(i)
                print(f"Peça {id_remover} removida da lista de reprovadas!")
                encontrou = True
                break
    
    if not encontrou:
        print(f"Peça com ID {id_remover} não encontrada!")

def listar_caixas():
    print("\n=== LISTAGEM DE CAIXAS ===")
    
    # Mostra as caixas que já foram fechadas
    print(f"\n--- CAIXAS FECHADAS ({len(caixas_fechadas)}) ---")
    if len(caixas_fechadas) == 0:
        print("Nenhuma caixa fechada ainda.")
    else:
        for caixa in caixas_fechadas:
            print(f"\nCaixa {caixa['numero']} - {len(caixa['pecas'])} peças")
            for peca in caixa['pecas']:
                print(f" - ID: {peca['id']}")
    
    # Mostra a caixa atual (que ainda está aberta)
    print(f"\n--- CAIXA ATUAL (Caixa {numero_caixa}) ---")
    if len(caixa_atual) == 0:
        print("Caixa vazia.")
    else:
        faltam = 10 - len(caixa_atual)
        print(f"{len(caixa_atual)} peças na caixa atual (faltam {faltam} para fechar)")
        for peca in caixa_atual:
            print(f" - ID: {peca['id']}")

def gerar_relatorio():
    print("\n" + "="*50)
    print(" RELATÓRIO FINAL DO SISTEMA")
    print("="*50)
    
    # Calcula os totais
    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)
    total_pecas = total_aprovadas + total_reprovadas
    
    print(f"\nRESUMO GERAL:")
    print(f" - Total de peças processadas: {total_pecas}")
    print(f" - Total de peças aprovadas: {total_aprovadas}")
    print(f" - Total de peças reprovadas: {total_reprovadas}")
    
    # Calcula a taxa de aprovação
    if total_pecas > 0:
        taxa = (total_aprovadas / total_pecas) * 100
        print(f" - Taxa de aprovação: {taxa:.1f}%")
    
    print(f"\nARMAZENAMENTO:")
    print(f" - Caixas fechadas: {len(caixas_fechadas)}")
    print(f" - Peças na caixa atual: {len(caixa_atual)}")
    
    print(f"\nMOTIVOS DE REPROVAÇÃO:")
    if len(pecas_reprovadas) == 0:
        print(" Nenhuma peça reprovada!")
    else:
        # Conta quantas vezes cada motivo apareceu
        peso_count = 0
        cor_count = 0
        comp_count = 0
        
        for peca in pecas_reprovadas:
            for motivo in peca['motivos_reprovacao']:
                if "Peso" in motivo:
                    peso_count = peso_count + 1
                elif "Cor" in motivo:
                    cor_count = cor_count + 1
                elif "Comprimento" in motivo:
                    comp_count = comp_count + 1
        
        if peso_count > 0:
            print(f" - Peso fora do padrão: {peso_count} peça(s)")
        if cor_count > 0:
            print(f" - Cor inválida: {cor_count} peça(s)")
        if comp_count > 0:
            print(f" - Comprimento fora do padrão: {comp_count} peça(s)")
    
    print("\n" + "="*50)

def menu_principal():
    while True:
        print("\n" + "="*50)
        print(" SISTEMA DE GESTÃO DE PEÇAS")
        print(" Controle de Qualidade e Armazenamento")
        print("="*50)
        print("\n[1] Cadastrar nova peça")
        print("[2] Listar peças aprovadas/reprovadas")
        print("[3] Remover peça cadastrada")
        print("[4] Listar caixas fechadas")
        print("[5] Gerar relatório final")
        print("[0] Sair do sistema")
        print("-"*50)
        
        opcao = input("Escolha uma opção: ")
        
        # Verifica qual opção foi escolhida
        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("\nEncerrando o sistema...")
            print("Obrigado por usar o Sistema de Gestão de Peças!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

# Programa principal
print("="*50)
print(" BEM-VINDO AO SISTEMA DE GESTÃO DE PEÇAS")
print("="*50)
menu_principal()