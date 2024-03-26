# Automação de Extração de Dados

### Descrição do Projeto

Este projeto visa automatizar a extração de dados do CNAE (Classificação Nacional de Atividades Econômicas) e gerar um relatório com as seguintes informações:

- **Quantidade de atividades distintas registradas**
- **Quantidade de grupos de atividades existentes**
- **Quantidade de atividades cadastradas em cada grupo**
- **Grupo(s) com o maior número de atividades vinculadas**

### Ferramentas Utilizadas

- **Biblioteca requests:** para extrair os dados do CNAE da API do IBGE.
- **Manipulação de listas e dicionários:** para organizar e analisar os dados extraídos.

### Etapas do Projeto

**1. Extração dos Dados**

A primeira etapa consiste em extrair os dados do CNAE da API do IBGE utilizando a biblioteca requests. A API fornece acesso a informações sobre as classes, divisões, grupos e seções do CNAE.

**2. Manipulação dos Dados**

Após a extração, os dados serão armazenados em listas e dicionários para facilitar a manipulação e análise.

**3. Geração do Relatório**

Com base nos dados manipulados, o relatório será gerado com as informações mencionadas na seção "Descrição do Projeto".

##

## Sobre estruturar e atualizar o código

1. **Abordagem procedural:** Um script Python simples que realiza a extração e análise dos dados.
2. **Abordagem orientada a objetos:** Uma classe Python encapsula a lógica de extração e análise, permitindo reutilização e melhor organização do código.

**Abordagem procedural:**

O código original utiliza funções e variáveis ​​globais para realizar a extração e análise dos dados:

- **Extração dos dados:** A API do IBGE é utilizada para obter os dados do CNAE em formato JSON.
- **Análise dos dados:** O código calcula a quantidade de atividades e grupos distintos, identifica os grupos com o maior número de atividades e imprime os resultados.

**Limitações da abordagem procedural:**

- **Falta de organização:** O código pode se tornar difícil de entender e manter à medida que cresce.
- **Reutilização limitada:** A lógica de extração e análise está embutida no script, dificultando a reutilização em outros projetos.
- **Dificuldade de teste:** Testar o código pode ser complicado devido à sua estrutura procedural.

**Abordagem orientada a objetos:**

A classe `ETL` encapsula a lógica de extração e análise dos dados:

- **Encapsulamento:** A classe armazena dados e métodos relacionados à extração e análise do CNAE.
- **Reutilização:** A classe pode ser facilmente reutilizada em outros projetos.
- **Teste:** A estrutura modular facilita o teste da classe.

**Atualização do código:**

O código foi atualizado para utilizar a classe `ETL`:

- **Criação da classe:** A classe `ETL` foi criada com os métodos `extract_cnae_data` e `__init__`.
- **Extração dos dados:** O método `extract_cnae_data` extrai os dados do CNAE da API do IBGE e realiza a análise.
- **Execução da classe:** A classe `ETL` é instanciada e o método `extract_cnae_data` é chamado com a URL da API.

**Vantagens da abordagem orientada a objetos:**

- **Organização:** O código é mais organizado e fácil de entender.
- **Reutilização:** A lógica de extração e análise pode ser facilmente reutilizada.
- **Teste:** O código é mais fácil de testar.

**Para testar o código:**

1. Instale a biblioteca requests:

```
pip install requests
```

2. Salve o código em um arquivo Python `(nome_arquivo.py)`.
3. Execute o código no Python interpreter.
