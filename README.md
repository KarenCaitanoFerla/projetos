# projetos
Repositório para projetos que faço, além da pós-graduação.


# etl-papeladia
Projeto básico de ETL, onde:
1. Carrego dados de um arquivo csv
2. Crio uma tabela para armazenar essas informações
3. Trato os dados de valores
4. Faço um cálculo da margem de lucro
5. Insiro uma nova coluna na tabela
6. Finalizo inserindo os dados dentro do Banco de Dados

# web-scraping
Projeto onde faço a captura de anuncios, de uma página web de vendas de canecas.
Utilizo o scrapy, onde:
1. Capturo os links dos anuncios.
2. Entro no anúncio e capturo informações de:
  - titulo
  - valor
  - descrição
  - imagens do produto
  - url do anuncio

# awslambdafunction
Projeto de introdução as tecnologias da AWS. Utilizo no projeto os serviços de:
1. S3 - Onde armazenei o arquivo csv.
3. SQS - Tecnologia utilizada para orquestramento do processamento de dados. A fila servia de gatinho para a função Lambda.
4. Lambda - Ferramenta usada para executar a função de transformação e carregamento dos dados.
5. RDS - Serviço de hospedagem do banco de dados.
