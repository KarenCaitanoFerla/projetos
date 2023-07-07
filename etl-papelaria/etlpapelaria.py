import csv
import sqlite3

def remove_ponto(valor):
    return int(round(float(valor.replace('.', '')), 0))

with open('papelaria.csv', 'r') as file:

    reader = csv.reader(file)

    #pula a primeira linha
    next(reader)

    # Conecta ao banco de dados
    conn = sqlite3.connect('papelariadb.db')

    # Deleta a tabela existente, se houver
    conn.execute('DROP TABLE IF EXISTS producao')

    conn = sqlite3.connect('papelariadb.db')
    #Cria a tabela
    conn.execute('''CREATE TABLE producao (
                    produto TEXT,
                    quantidade INTEGER,
                    preco_medio_produto REAL,
                    receita_total REAL,
                    margem_lucro REAL
                )''')
    
    for row in reader:
        if int(row[1]) > 10:
            # Remove o ponto do valor da última coluna e converte para inteiro
            row[2] = remove_ponto(row[2])
            row[3] = remove_ponto(row[3])

            # Calcula a margem de lucro bruta com base no valor médio de venda e na receita total e arredonda para duas casas decimais
            margem_lucro = round((row[3] / float(row[1])) - float(row[2]), 2)
            print("margem lucro --------- ", margem_lucro)

            # Insere a linha com a nova coluna 'margem_lucro' na tabela do banco de dados
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio_produto, receita_total, margem_lucro) VALUES (?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], margem_lucro))

    conn.commit()
    conn.close()

print("Job Concluído com Sucesso!")