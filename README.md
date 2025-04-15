# 🎧 Spotify BI Dashboard

Um projeto de Business Intelligence utilizando **Power BI** para análise de músicas populares do Spotify com visual interativo, dados de streaming, e integração com a **API do Spotify**.

---

## 📊 Visão Geral

O projeto visa analisar o desempenho de músicas populares no Spotify através de um dashboard com:

- Número de streams por faixa
- Análise de características musicais (danceabilidade, valência, etc.)
- Comparação com média de streams anuais
- Visualização da evolução temporal de faixas
- Capas dos álbuns e imagens dos artistas via API

---

## 🛠️ Tecnologias Utilizadas

- Power BI
- Python (para integração com a API do Spotify)
- Pandas
- Requests
- TQDM
- CSV como fonte de dados
- Spotify Web API

---

## 📂 Estrutura de Pastas

Spotify - BI/ ├── Data_script/ # Scripts de tratamento e coleta de dados
              │ └── Spotify_script1.py ├── imgs/ # Logos, fundo e assets visuais do dashboard 
              ├── .idea/ # Configurações do projeto (PyCharm, opcional) 
              ├── SpotifyBI.pptx # Relatório ou apresentação
              └── updated_file1.csv # Arquivo final com URLs das imagens


---

## 🔁 Fluxo do Projeto

1. 📥 Carregamento dos dados de streaming do Spotify em CSV
2. 🎯 Consulta à API para buscar imagens dos álbuns
3. 🐍 Script Python (`Spotify_script1.py`) adiciona URLs ao dataset
4. 📈 Dados tratados são carregados no Power BI para criação do dashboard
5. 🎨 Personalização com imagens, logos e tema visual

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/lucas-wall/API-Spotify-BI.git

2. Execute o script para gerar o dataset com imagens:
   python Spotify_script1.py

3. Abra o Power BI e carregue o arquivo .pbix com o CSV atualizado
updated_file1.csv

Crie suas próprias credenciais em: Spotify Developer Dashboard