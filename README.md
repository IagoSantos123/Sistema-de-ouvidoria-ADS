📌 Sistema de Ouvidoria
Este é um sistema de Ouvidoria desenvolvido em Python para a disciplina de Programação em Linguagem Estruturada, no curso de Análise e Desenvolvimento de Sistemas da UNIFACISA.

Equipe:

Iago Edson Santos Lucena

Gustavo Paula Cabral

Daniel Almeida Diniz

Professor :

Daniel Abella

O sistema permite registrar, listar, editar e excluir manifestações de usuários (sugestões, elogios e reclamações), além de se conectar a um banco de dados MySQL para gerenciar essas manifestações.

🛠 Tecnologias Utilizadas
Python 3.x

MySQL

mysql-connector-python

📂 Estrutura do Projeto
bash
Copy
Edit
Sistemadeouvidoria/
│── config.py            # Configurações do banco de dados
│── database.py          # Conexão com o banco e operações SQL
│── main.py              # Interface do usuário e lógica principal
│── requirements.txt     # Dependências do projeto
│── README.md            # Documentação do projeto
⚙️ Configuração do Banco de Dados
Antes de rodar o projeto, crie a tabela no MySQL com o seguinte comando:

sql
Copy
Edit
CREATE TABLE manifestacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50),
    descricao TEXT,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
🚀 Como Instalar e Executar
Siga os passos abaixo para configurar e executar o projeto:

Clone o repositório:

bash
Copy
Edit
git clone https://github.com/IagoSantos123/Sistema-de-ouvidoria-ADS.git
Entre na pasta do projeto:

bash
Copy
Edit
cd Sistemadeouvidoria
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copy
Edit
python -m venv venv
Para Linux/Mac:

bash
Copy
Edit
source venv/bin/activate
Para Windows:

bash
Copy
Edit
venv\Scripts\activate
Instale as dependências:

bash
Copy
Edit
pip install mysql-connector-python
Configure o banco de dados no arquivo config.py.

Execute o sistema:

bash
Copy
Edit
python main.py
🖥 Como Usar
Após executar o sistema, você verá o menu principal com as seguintes opções:

1️⃣ Listar manifestações
2️⃣ Inserir nova manifestação
3️⃣ Alterar uma manifestação existente
4️⃣ Excluir uma manifestação
5️⃣ Contar reclamações
6️⃣ Sair

Escolha a opção desejada digitando o número correspondente.