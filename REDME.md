# 🤖 Automação de Cadastro de Produtos com PyAutoGUI e Pandas

Este projeto é uma automação em Python (RPA) desenvolvida para realizar o preenchimento e cadastro automático de uma lista de produtos em um sistema web.

## 📌 Sobre o Projeto
A aplicação lê uma base de dados em formato CSV e utiliza automação de interface de usuário para simular a digitação e os cliques necessários para cadastrar cada item no sistema.

> *Projeto desenvolvido durante o Intensivão de Python da Hashtag Treinamentos.*

## 🚀 Tecnologias Utilizadas
* **Python 3**
* **Pandas**: Leitura e manipulação da base de dados (`produtos.csv`).
* **PyAutoGUI**: Automação de comandos de mouse e teclado.

## 🛠️ Como Executar o Projeto

1. Instale as bibliotecas necessárias no terminal:
   pip install pyautogui pandas

2. Certifique-se de que o arquivo `produtos.csv` está na mesma pasta do script Python.

3. Execute o script principal.

> **Atenção:** Como o PyAutoGUI utiliza coordenadas fixas de tela (`x` e `y`), certifique-se de ajustar as coordenadas no código para a resolução do seu monitor antes de rodar.

## 🛠️ Código Auxiliar: Mapeamento de Coordenadas
Como o **PyAutoGUI** funciona com cliques em posições fixas da tela, o script auxiliar é utilizado para identificar a posição exata (coordenadas X e Y) do mouse em cada elemento do sistema (campos de login, botões e formulários):

