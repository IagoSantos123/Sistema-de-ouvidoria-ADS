import mysql.connector
from config import DB_CONFIG

def conectar():
    """Conecta ao banco de dados."""
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar: {err}")
        return None

def listar_manifestacoes():
    """Lista todas as manifestações registradas e retorna como lista de dicionários."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, tipo, descricao FROM manifestacoes")
        manifestacoes = cursor.fetchall()
        cursor.close()
        conexao.close()

        # Convertendo para uma lista de dicionários
        lista_manifestacoes = [{"id": m[0], "tipo": m[1].lower(), "descricao": m[2]} for m in manifestacoes]
        return lista_manifestacoes

def inserir_manifestacao(tipo, descricao):
    """Insere uma nova manifestação no banco de dados."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO manifestacoes (tipo, descricao) VALUES (%s, %s)"
        cursor.execute(sql, (tipo.lower(), descricao))  # Convertendo tipo para minúsculas para padronizar
        conexao.commit()
        print("Manifestação registrada com sucesso!")
        cursor.close()
        conexao.close()

def alterar_manifestacao(id, novo_tipo, nova_descricao):
    """Altera uma manifestação existente no banco de dados."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "UPDATE manifestacoes SET tipo = %s, descricao = %s WHERE id = %s"
        cursor.execute(sql, (novo_tipo.lower(), nova_descricao, id))
        conexao.commit()
        print("Manifestação alterada com sucesso!")
        cursor.close()
        conexao.close()

def excluir_manifestacao(id):
    """Exclui uma manifestação do banco de dados."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "DELETE FROM manifestacoes WHERE id = %s"
        cursor.execute(sql, (id,))
        conexao.commit()
        print("Manifestação excluída com sucesso!")
        cursor.close()
        conexao.close()

def contar_reclamacoes():
    """Conta quantas manifestações do tipo 'reclamação' existem no banco de dados."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT COUNT(*) FROM manifestacoes WHERE LOWER(tipo) = 'reclamação'")
        total = cursor.fetchone()[0]
        cursor.close()
        conexao.close()
        return total
