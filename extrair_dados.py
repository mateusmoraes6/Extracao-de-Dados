import requests 

dados = requests.get('https://servicodados.ibge.gov.br/api/v2/cnae/classes').json()

# Onde os dados extraídos estão guardados
dados[0]

# Lista de todos os grupos
qtde_atividades_distintas = len(dados)

grupos = []
for registro in dados:
    grupos.append(registro['grupo']['descricao'])

grupos[:10]

# Axtrair a quantidade de grupos de atividades
qtde_grupos_distintos = len(set(grupos))

# Contar quantas atividades estão cadastradas em cada grupo
grupos_count = [(grupo, grupos.count(grupo)) for grupo in set(grupos)]
grupos_count[:5]

# Quais grupos possuem o maior número de atividades vinculadas
grupos_count = dict(grupos_count)

# Descobrir qual (ou quais) grupos possuem mais atividades
valor_maximo = max(grupos_count.values())
grupos_mais_atividades = [chave for (chave, valor) in grupos_count.items() if valor == valor_maximo]

grupos_mais_atividades

