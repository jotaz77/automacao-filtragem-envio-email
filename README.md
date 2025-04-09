📊 Script de Filtragem de Dados em Planilha e Envio Automático de E-mails
Este projeto demonstra um script automatizado em Python capaz de filtrar dados de uma planilha Excel com base em colunas definidas pelo usuário, gerar novas planilhas personalizadas e enviar automaticamente os links de acesso via e-mail utilizando a API do Gmail e o Google Drive.

🎯 Objetivo
Mostrar minha capacidade na criação de scripts automatizados para otimizar processos repetitivos, utilizando ferramentas robustas como:

Python

Google Drive API

Gmail API

Pandas

⚙️ Tecnologias Utilizadas
🐍 Python

🧠 Pandas

📊 OpenPyXL

📧 Gmail API

☁️ Google Drive API

🔐 OAuth2 (Autenticação Google)

🌎 Googleapiclient

🔒 dotenv (para variáveis de ambiente seguras)

🚀 Instalação
bash
Copiar
Editar
# Clone o repositório
git clone https://github.com/jotaz77/automacao-filtragem-envio-email.git
cd automacao-filtragem-envio-email

# Crie e ative o ambiente virtual (opcional, mas recomendado)
python -m venv venv
venv\Scripts\activate  # Windows

# ou no macOS/Linux
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
Adicione suas credenciais do Google:

Coloque o arquivo credentials.json (obtido no Google Cloud Console) na raiz do projeto.

⚠️ Esse arquivo está listado no .gitignore e não deve ser enviado para o GitHub.

💡 Como Usar
Tenha uma planilha base .xlsx com os dados que deseja filtrar.

Execute o script script.py.

Informe:

Nome da planilha

Colunas para filtragem (separadas por vírgula, se mais de uma)

Coluna que contém os e-mails

O script irá:

Filtrar os dados automaticamente

Gerar novas planilhas com os dados filtrados

Fazer upload para o Google Drive

Enviar os links das planilhas por e-mail para os destinatários

🧳 Estrutura do Projeto
bash
Copiar
Editar
📁 projeto
├── script.py
├── credentials.json       # ← NÃO subir para o GitHub
├── token.json             # ← Gerado após login OAuth2
├── README.md
├── requirements.txt
├── .env                   # Variáveis de ambiente (opcional)
├── planilhas_geradas/     # Planilhas filtradas geradas automaticamente
└── .gitignore
📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

🤝 Contato
Curtiu o projeto? Quer trocar uma ideia ou fazer sugestões?

Me chama no LinkedIn [https://www.linkedin.com/in/almir-cavalcante/] — sempre bom conversar sobre automações e tecnologia!
