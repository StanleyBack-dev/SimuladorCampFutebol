import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Lista de clubes
clubes = ['Flamengo', 'Palmeiras', 'Santos', 'Corinthians', 'São Paulo', 'Grêmio', 'Internacional', 'Cruzeiro',
          'Goiás', 'Curitiba', 'Cuiabá', 'Athletico Paranaense', 'Atlético Mineiro', 'Vasco da Gama',
          'América Mineiro', 'Red Bull Bragantino', 'Fluminense', 'Fortaleza', 'Botafogo', 'Bahia']

# Dicionário para armazenar os resultados
resultados = {}

# Inicializa os resultados dos clubes
for clube in clubes:
    resultados[clube] = {'pontos': 0, 'vitorias': 0, 'empates': 0, 'derrotas': 0, 'gols_feitos': 0, 'gols_sofridos': 0, 'saldo_gols': 0}

# Função para simular os placares automaticamente
def simular_placares_aleatorios():
    # Simulação dos confrontos
    for i, clube1 in enumerate(clubes):
        for j, clube2 in enumerate(clubes):
            if i != j:
                gols_clube1 = random.randint(0, 5)
                gols_clube2 = random.randint(0, 5)

                resultados[clube1]['gols_feitos'] += gols_clube1
                resultados[clube1]['gols_sofridos'] += gols_clube2

                resultados[clube2]['gols_feitos'] += gols_clube2
                resultados[clube2]['gols_sofridos'] += gols_clube1

                if gols_clube1 > gols_clube2:
                    resultados[clube1]['pontos'] += 3
                    resultados[clube1]['vitorias'] += 1
                    resultados[clube2]['derrotas'] += 1
                elif gols_clube1 == gols_clube2:
                    resultados[clube1]['pontos'] += 1
                    resultados[clube1]['empates'] += 1
                    resultados[clube2]['pontos'] += 1
                    resultados[clube2]['empates'] += 1
                else:
                    resultados[clube2]['pontos'] += 3
                    resultados[clube2]['vitorias'] += 1
                    resultados[clube1]['derrotas'] += 1

    # Calcula o saldo de gols e atualiza a classificação final
    classificacao_final = sorted(resultados.items(), key=lambda x: (x[1]['pontos'], x[1]['vitorias'], x[1]['saldo_gols']), reverse=True)
    for clube, info in classificacao_final:
        info['saldo_gols'] = info['gols_feitos'] - info['gols_sofridos']

    # Exibição da classificação geral
    clear_screen()
    print('\nClassificação Geral:')
    print("-------------------------------------------------------------------------------------------------")
    for i, (clube, info) in enumerate(classificacao_final):
        print(f'{i+1}. {clube}: Pontos {info["pontos"]} | Vitórias {info["vitorias"]} | Empates {info["empates"]} | Derrotas {info["derrotas"]} | Saldo de Gols {info["saldo_gols"]}')
    print("-------------------------------------------------------------------------------------------------")
    input('\nPressione Enter para voltar ao menu principal.')

# Função para permitir que o usuário digite os placares manualmente
def simular_placares_manualmente():
    # Simulação dos confrontos
    for i, clube1 in enumerate(clubes):
        for j, clube2 in enumerate(clubes):
            if i != j:
                placar_valido = False
                while not placar_valido:
                    clear_screen()
                    placar = input(f'Digite o placar do confronto {clube1} vs {clube2} (ou "V" para voltar ao menu principal): ')
                    if placar.lower() == 'v':
                        return  # Voltar ao menu principal
                    if len(placar.split('x')) == 2:
                        try:
                            gols_clube1, gols_clube2 = map(int, placar.split('x'))
                            if gols_clube1 >= 0 and gols_clube2 >= 0:
                                placar_valido = True
                            else:
                                print('Placar inválido. Os gols devem ser valores não negativos.')
                        except ValueError:
                            print('Placar inválido. Digite dois números separados por "x".')
                    else:
                        print('Placar inválido. Digite dois números separados por "x".')

                resultados[clube1]['gols_feitos'] += gols_clube1
                resultados[clube1]['gols_sofridos'] += gols_clube2

                resultados[clube2]['gols_feitos'] += gols_clube2
                resultados[clube2]['gols_sofridos'] += gols_clube1

                if gols_clube1 > gols_clube2:
                    resultados[clube1]['pontos'] += 3
                    resultados[clube1]['vitorias'] += 1
                    resultados[clube2]['derrotas'] += 1
                elif gols_clube1 == gols_clube2:
                    resultados[clube1]['pontos'] += 1
                    resultados[clube1]['empates'] += 1
                    resultados[clube2]['pontos'] += 1
                    resultados[clube2]['empates'] += 1
                else:
                    resultados[clube2]['pontos'] += 3
                    resultados[clube2]['vitorias'] += 1
                    resultados[clube1]['derrotas'] += 1

    # Calcula o saldo de gols e atualiza a classificação final
    classificacao_final = sorted(resultados.items(), key=lambda x: (x[1]['pontos'], x[1]['vitorias'], x[1]['saldo_gols']), reverse=True)
    for clube, info in classificacao_final:
        info['saldo_gols'] = info['gols_feitos'] - info['gols_sofridos']

    # Exibição da classificação geral
    clear_screen()
    print('\nClassificação Geral:')
    print("-------------------------------------------------------------------------------------------------")
    for i, (clube, info) in enumerate(classificacao_final):
        print(f'{i+1}. {clube}: Pontos {info["pontos"]} | Vitórias {info["vitorias"]} | Empates {info["empates"]} | Derrotas {info["derrotas"]} | Saldo de Gols {info["saldo_gols"]}')
    print("-------------------------------------------------------------------------------------------------")
    input('\nPressione Enter para voltar ao menu principal.')

# Menu inicial
while True:
    clear_screen()
    print('Bem-vindo ao sistema de sorteio de clubes de futebol!')
    print("-------------------------------------------------------")
    print('1. Simular placares automaticamente')
    print('2. Digitar placares manualmente')
    print('3. Sair do programa')
    print("-------------------------------------------------------")
    opcao = input('Opção: ')

    if opcao == '1':
        simular_placares_aleatorios()
    elif opcao == '2':
        simular_placares_manualmente()
    elif opcao == '3':
        clear_screen()
        print('\nPrograma Encerrado !')
        break
    else:
        clear_screen()
        print('Opção inválida. Pressione Enter para tentar novamente.')
        input()
