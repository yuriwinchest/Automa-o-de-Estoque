# Automa-o-de-Estoque
Automação de Estoque Este projeto é uma solução para a automação da extração, processamento e comparação de dados de estoque entre diferentes marketplaces (como Mercado Livre e Bling). A aplicação permite realizar a conferência diária de estoque e gerar logs das diferenças, salvando os resultados em planilhas do Google Sheets.
Automação de Estoque
Este projeto é uma solução para a automação da extração, processamento e comparação de dados de estoque entre diferentes marketplaces (como Mercado Livre e Bling). A aplicação permite realizar a conferência diária de estoque e gerar logs das diferenças, salvando os resultados em planilhas do Google Sheets.

Índice
Introdução
Funcionalidades
Pré-requisitos
Instalação
Estrutura do Projeto
Configuração das APIs
Execução
Log de Processamento
Contribuição
Licença
Introdução
O objetivo deste projeto é automatizar o processo de extração e comparação de estoques entre os marketplaces Mercado Livre e Bling, gerando logs com as diferenças e disponibilizando gráficos e tabelas para acompanhamento. O projeto foi desenvolvido em Python, utilizando o framework Streamlit para a interface gráfica e integração com Google Sheets para armazenamento de dados.

Funcionalidades
Extrair informações de estoque do Mercado Livre e Bling.
Comparar as informações de estoque e gerar logs com as diferenças.
Armazenar os dados em planilhas do Google Sheets.
Visualizar os dados em gráficos e tabelas através de uma interface web com Streamlit.
Gerar rotinas diárias para o Mercado Livre e mensais para os outros marketplaces.
Pré-requisitos
Antes de começar, certifique-se de que sua máquina possui:

Python 3.8+ instalado.
Pip (gerenciador de pacotes Python).
Credenciais de API para:
Google Sheets API.
API do Mercado Livre.
API do Bling.
Instalação
Siga as instruções abaixo para instalar e configurar o projeto:

1. Clonar o Repositório
bash
Copiar código
git clone https://github.com/Yuriwinchester/automacao-de-estoque.git
cd automacao-de-estoque
2. Criar e Ativar o Ambiente Virtual
No Windows:
bash
Copiar código
python -m venv venv
.\venv\Scripts\activate
No Linux/Mac:
bash
Copiar código
python3 -m venv venv
source venv/bin/activate
3. Instalar as Dependências
Com o ambiente virtual ativado, execute o seguinte comando:

bash
Copiar código
pip install -r requirements.txt
4. Configuração das APIs
Google Sheets API
Siga as instruções para configurar o acesso à Google Sheets API aqui. Salve o arquivo credentials.json dentro da pasta api/.

API do Mercado Livre e Bling
Obtenha suas credenciais da API do Mercado Livre e Bling e configure-as nos arquivos correspondentes em api/mercado_livre_api.py e api/bling_api.py.
Estrutura do Projeto
bash
Copiar código
automacao-de-estoque/
│
├── api/                   # Scripts para integração com APIs
│   ├── google_sheets_api.py
│   ├── mercado_livre_api.py
│   └── bling_api.py
│
├── data/                  # Pasta para armazenamento de dados
│
├── logs/                  # Logs de processamento
│   └── estoque_automacao.log
│
├── routes/                # Endpoints e rotas
│
├── scripts/               # Scripts de extração e processamento de dados
│   └── extrair_estoque.py
│
├── utils/                 # Funções utilitárias
│
├── venv/                  # Ambiente virtual
│
├── app.py                 # Interface principal com Streamlit
├── main.py                # Script principal para processamento
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
Configuração das APIs
Google Sheets API
Para utilizar a Google Sheets API, siga as etapas abaixo:

Acesse o console do Google Cloud e crie um novo projeto.
Ative a Google Sheets API para o projeto.
Crie credenciais de OAuth 2.0 e baixe o arquivo credentials.json.
Coloque o arquivo credentials.json na pasta api/ do projeto.
API do Mercado Livre e Bling
Certifique-se de que você possui as credenciais corretas de acesso para essas APIs e as configure nos respectivos scripts:

Mercado Livre: api/mercado_livre_api.py
Bling: api/bling_api.py
Execução
Executar a Aplicação com Streamlit
Para rodar a aplicação principal:

bash
Copiar código
streamlit run app.py
Isso abrirá a interface no seu navegador, onde você poderá visualizar os dados e realizar as comparações de estoque.

Executar o Processamento de Estoque
Para rodar o script de extração e comparação de estoques manualmente, execute:

bash
Copiar código
python main.py
Log de Processamento
Após a execução do processamento de estoques, o log será gerado no arquivo logs/estoque_automacao.log. Verifique este arquivo para obter detalhes sobre o processamento e as diferenças de estoque encontradas.

Contribuição
Se você deseja contribuir para este projeto, sinta-se à vontade para fazer um fork do repositório, criar um branch e submeter um pull request.

Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
![Captura de tela 2024-09-11 165039](https://github.com/user-attachments/assets/62a87f38-382d-4df6-b8d3-3853d18f5689)
![Captura de tela 2024-09-11 163337](https://github.com/user-attachments/assets/cec88a4b-07b5-4be7-a0c2-ba314896ff72)
![Captura de tela 2024-09-11 163319](https://github.com/user-attachments/assets/5087ca81-fc7e-4393-94e8-5d5a646429d7)
![Captura de tela 2024-09-11 163302](https://github.com/user-attachments/assets/53684953-f6f9-49c0-b01c-c226fc70c6e0)
![Captura de tela 2024-09-11 163231](https://github.com/user-attachments/assets/2080d6ca-da76-47de-a65f-886d642eb60b)
