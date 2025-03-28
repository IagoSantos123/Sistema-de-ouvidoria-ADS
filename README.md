📌 Sistema de Ouvidoria

Este é um sistema de Ouvidoria em Python para displina de programar em linguagem estruturada no curso de  Análise e Desenvolvimento de sistemas na unifacisa, que permite registrar, listar, editar e excluir manifestações de usuários. O sistema se conecta a um banco de dados MySQL e pode ser usado para gerenciar sugestões, elogios e reclamações.

🛠 Tecnologias Utilizadas

    Python 3.x

    MySQL

    mysql-connector-python

📂 Estrutura do Projeto

Sistemadeouvidoria/
│── config.py          # Configurações do banco de dados
│── database.py        # Conexão com o banco e operações SQL
│── main.py            # Interface do usuário e lógica principal
│── requirements.txt   # Dependências do projeto
│── README.md          # Documentação do projeto


⚙️ Configuração do Banco de Dados

Antes de rodar o projeto, crie a tabela no MySQL:

CREATE TABLE manifestacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50),
    descricao TEXT,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


🚀 Como Instalar e Executar

    Clone o repositório :

        git clone https://github.com/IagoSantos123/Sistema-de-ouvidoria-ADS.git
    
    Entre na pasta:

        cd Sistemadeouvidoria
        
    Crie um ambiente virtual (opcional, recomendado):

        python -m venv venv
        source venv/bin/activate  # Linux/Mac
        venv\Scripts\activate     # Windows


    Instale as dependências:
    
        pip install mysql-connector-python


    Configure o banco de dados no config.py
    
    Execute o sistema :
        python main.py
    
    
    🖥 Como Usar

        No menu principal, escolha uma das opções: 
            1️⃣ Listar manifestações
            2️⃣ Inserir nova manifestação
            3️⃣ Alterar uma manifestação existente
            4️⃣ Excluir uma manifestação
            5️⃣ Sair


