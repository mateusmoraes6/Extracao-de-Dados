import requests
from datetime import datetime 

class ETL:
    def __init__(self):
        self.url = None

    def extract_cnae_data(self, url):
        self.url = url
        data_extracao = datetime.today().strftime("%Y/%m/%d - %H:%M:%S")
        # Faz a extração
        dados = requests.get(self.url).json()

        # Extrai os grupos de registro
        grupos = []
        for registro in dados:
            grupos.append(registro['grupo']['descricao'])

        # Cria uma lista de tuplas (grupo, quantidade_atividades)
        grupos_count = [(grupo, grupos.count(grupo)) for grupo in set(grupos)]
        grupos_count = dict(grupos_count)

        # Capturar o valor máximo de atividades
        valor_maximo = max(grupos_count.values())
        # Gera uma lista com os grupos que possuem a quantidade máxima de atividades
        grupos_mais_atividades = [chave for (chave, valor) in grupos_count.items() if valor == valor_maximo]

        # Informações
        qtde_atividades_distintas = len(dados)
        qtde_grupos_distintos = len(set(grupos))

        print(f"\n{'-' * 74} Extrato {'-' * 74}")
        print(f"Dados extraídos em: {data_extracao}")
        print(f"Quantidade de atividades distintas = {qtde_atividades_distintas}")
        print(f"Quantidade de grupos distintos = {qtde_grupos_distintos}")
        print(f"Grupos com o maior número de atividades = {grupos_mais_atividades}, atividades = {valor_maximo}")
        print('-' * 157)
            
        return None

# Usando a classe ETL
ETL().extract_cnae_data('https://servicodados.ibge.gov.br/api/v2/cnae/classes')
