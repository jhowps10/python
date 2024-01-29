import csv
import mysql.connector

# Configurações do MySQL
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'd3whpact'
MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'sistema'
MYSQL_TABLE = 'app_interacao'

# Caminho do arquivo CSV
CAMINHO_ARQUIVO_CSV = 'C:/Users/reds_/OneDrive/Área de Trabalho/programacao/contatos.csv'


def importar_csv_para_mysql():
    # Conectar ao MySQL
    conn = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, database=MYSQL_DATABASE)
    cursor = conn.cursor()

    try:
        # Abrir o arquivo CSV
        with open(CAMINHO_ARQUIVO_CSV, 'r') as file:
            # Criar um leitor CSV
            csv_reader = csv.reader(file)

            # Ignorar o cabeçalho se existir
            next(csv_reader, None)

            # Iterar pelas linhas e inserir dados no MySQL
            for row in csv_reader:
                # Preencher com valores padrão se o número de valores for menor que 12
                while len(row) < 12:
                    row.append('')

                # Desempacotar os valores
                data_contato, canal, contato, detalhes, ocasiao, data_evento, primeira_cor, segunda_cor, tamanho, locacao, motivo, motivo2 = row
                query = f"INSERT INTO {MYSQL_TABLE} (data_contato, canal, contato, detalhes, ocasiao, data_evento, primeira_cor, segunda_cor, tamanho, locacao, motivo, motivo2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (
                data_contato, canal, contato, detalhes, ocasiao, data_evento, primeira_cor, segunda_cor, tamanho,
                locacao, motivo, motivo2)
                cursor.execute(query, values)

        # Commit para salvar as alterações
        conn.commit()
        print("Importação concluída com sucesso.")
    except Exception as e:
        print(f"Erro durante a importação: {e}")
    finally:
        # Fechar conexão
        cursor.close()
        conn.close()


if __name__ == "__main__":
    importar_csv_para_mysql()
