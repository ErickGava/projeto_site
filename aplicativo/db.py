import mysql.connector

def conectar_banco():
    conexao = mysql.connector.connect(host = "paparella.com.br",
                                      database = "paparell_python",
                                      user = "paparell_aluno_1",
                                      password = "Senai2025",
                                      )
    return conexao