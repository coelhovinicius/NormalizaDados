'''Funções para higienização e adequação LGPD de dados '''

# Rodar venv - venv\Scripts\activate

import re
import pandas as pd

ARQUIVO_CSV = 'CSV_Files/SemStatus_usuarios_nao_ativados_dsop_NOVO_virgula.csv'
ARQUIVO_NOVO = 'CSV_Files/TESTE_SemStatus_usuarios_nao_ativados_dsop_NOVO_virgula.csv'


def format_cpf(value):
    ''' Função para normalizar CPF '''
    # Remove todos os caracteres não numéricos
    value = re.sub(r'\D', '', value)
    # Preenche com zeros à esquerda, caso tenha menos de 11 caracteres
    value = value.zfill(11)
    # if len(value) == 11:  # CPF
    return f"{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:]}"
    # return value  # Mantém CPF como está, se já for válido


def format_phone(value):
    ''' Função para normalizar telefone '''
    # Remove todos os caracteres não-numéricos
    value = re.sub(r'\D', '', value)
    if len(value) == 10:  # Formato fixo
        return f'+55 ({value[:2]}) {value[2:6]}-{value[6:]}'
    if len(value) == 11:  # Formato celular
        return f'+55 ({value[:2]}) {value[2:7]}-{value[7:]}'
    return value  # Retorna sem alterações se o formato não for reconhecido


def main():
    ''' Função principal'''
    # Carregar CSV
    df = pd.read_csv(ARQUIVO_CSV)

    # Aplicar funções nas colunas desejadas
    df['cpf_cnpj'] = df['cpf_cnpj'].astype(str).apply(format_cpf)
    df['phone'] = df['phone'].astype(str).apply(format_phone)

    # Salvar CSV atualizado
    df.to_csv(ARQUIVO_NOVO, index=False)

    print(f'Transformação concluída e salva em "{ARQUIVO_NOVO}"')


if __name__ == "__main__":
    main()
