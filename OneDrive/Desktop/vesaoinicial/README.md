📊 Script de filtragem de dados em planilha e envio de emails automático

Este projeto demonstra a criação de um script completo e automatizado que filtra dados de uma planilha Excel com base em colunas definidas pelo usuário, gera novas planilhas personalizadas e envia automaticamente os links de acesso a essas planilhas via e-mail utilizando a API do Gmail.

🎯 Objetivo

Mostrar minha capacitação na criação de scripts automatizados utilizando Python, Google Drive API, Gmail API e manipulação de planilhas com Pandas.

⚙️ Tecnologias Utilizadas

Python

Pandas

OpenPyXL

Gmail API

Google Drive API

OAuth2 (Autenticação Google)

Google Auth

Googleapiclient

dotenv (para segurança e variáveis de ambiente)

🚀 Instalação

1. Clone o repositório

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Crie um ambiente virtual (opcional, mas recomendado)

python -m venv venv
venv\Scripts\activate   # Windows
# ou
source venv/bin/activate   # macOS/Linux

3. Instale as dependências

pip install -r requirements.txt

4. Adicione suas credenciais do Google

Coloque o arquivo credentials.json (obtido no Google Cloud Console) na pasta raiz do projeto.

⚠️ Esse arquivo não deve ser incluído no GitHub. Ele já está listado no .gitignore.

💡 Como usar

Tenha uma planilha base (.xlsx) contendo os dados que deseja filtrar.

Ao rodar o script, ele pedirá:

O nome da planilha.

As colunas que deseja filtrar (pode informar mais de uma separando por vírgula).

A coluna que contém os e-mails.

O script irá:

Filtrar a planilha automaticamente com base nos valores únicos dessas colunas.

Gerar novas planilhas com os dados filtrados.

Subir essas planilhas para o seu Google Drive.

Enviar os links para os respectivos e-mails automaticamente.

🧳 Exemplo prático



📁 Estrutura do Projeto

📆 projeto
 ├── script.py
 ├── credentials.json          # ← NÃO subir para o GitHub
 ├── token.json                # ← Gerado após o login OAuth2
 ├── README.md
 ├── requirements.txt
 ├── planilhas_geradas         # ← Planilhas filtradas geradas automaticamente
 └── .gitignore

📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

🤝 Contato

Fique à vontade para me chamar no LinkedIn para trocar uma ideia ou se quiser saber mais sobre o projeto!

