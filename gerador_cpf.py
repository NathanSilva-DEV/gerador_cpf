import random
import os

# Dicionário com as regiões fiscais
REGIOES_FISCAIS = {
    '1': 'Distrito Federal (DF), Goiás (GO), Mato Grosso do Sul (MS), Mato Grosso (MT), Tocantins (TO)',
    '2': 'Pará (PA), Amazonas (AM), Acre (AC), Amapá (AP), Rondônia (RO), Roraima (RR)',
    '3': 'Ceará (CE), Maranhão (MA), Piauí (PI)',
    '4': 'Pernambuco (PE), Rio Grande do Norte (RN), Paraíba (PB), Alagoas (AL)',
    '5': 'Bahia (BA), Sergipe (SE)',
    '6': 'Minas Gerais (MG)',
    '7': 'Rio de Janeiro (RJ), Espírito Santo (ES)',
    '8': 'São Paulo (SP)',
    '9': 'Paraná (PR), Santa Catarina (SC)',
    '0': 'Rio Grande do Sul (RS)'
}    

# Configurando a limpeza de console
def limpar_tela():
    if os.name == 'nt': # Windows 
        os.system('cls')   
    else: # Linux/macOS
        os.system('clear')

# Configurando a saída no terminal
def saida_terminal(largura):
    print('-' * largura)
    print('GERADOR DE CPF VÁLIDO'.center(largura))
    print('-' * largura)   


contador = 0
# Saída no terminal
while True:   
    saida_terminal(35) # Formatação de saída

    try:
        formatacao_saida_int = int(input('Deseja Gerar quantos CPFs: '))
    except ValueError:
        limpar_tela()
        continue
    
    while True:
        formatacao_saida = input('Deseja gerar o CPF com caracteres de pontuação? [S]im [N]não: ').upper()

        if formatacao_saida == 'S' or formatacao_saida == 'N':
            break
        else:
            
            print('Entrada inválida! Digite apenas S ou N. ')
        

    limpar_tela() # Limpa a tela
    saida_terminal(35) # Formatação de saída

    for i in range(formatacao_saida_int):
        digitos_cpf = [random.randint(0, 9) for _ in range(9)] # Gerando os nove primeiros digitos do CPF (aleatórios)

        # Calculando os dois digitos validadores
        for i in range(2):
            soma_digitos = 0
            contador_regressivo = len(digitos_cpf) + 1

            for digito in digitos_cpf:
                soma_digitos += digito * contador_regressivo
                contador_regressivo -= 1

            resto = (soma_digitos * 10) % 11

            digito_validado = 0 if resto > 9 else resto
            digitos_cpf.append(digito_validado)

        # Formatando CPF
        cpf_str_sem_ponto = ''.join([str(digitos) for digitos in digitos_cpf])
        cpf_formatado = f'{cpf_str_sem_ponto[0:3]}.{cpf_str_sem_ponto[3:6]}.{cpf_str_sem_ponto[6:9]}-{cpf_str_sem_ponto[9:11]}'

        nono_digito = cpf_str_sem_ponto[8]# Define o nono dígito

        print(f'CPF {contador+1}')
        if formatacao_saida == 'S':
            print('CPF gerado:', cpf_formatado)
            print('Região fiscal:', REGIOES_FISCAIS[nono_digito]) 
        elif formatacao_saida == 'N':
            print('CPF gerado:', cpf_str_sem_ponto)     
            print('Região fiscal:', REGIOES_FISCAIS[nono_digito])  
     
        contador += 1
    break     