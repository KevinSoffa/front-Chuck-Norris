# 😂CHUCK NORRIS PIADAS

<div align="center">
  <img height="180em" src="https://raw.githubusercontent.com/KevinSoffa/API-previdencia-KevinSoffa/refs/heads/develop/img/Kevin%20Soffa%20(2).png"/>
</div>

## Sumário 🔄
1. [Descrição](#descrição-)
2. [Tecnologias](#tecnologias-️)
3. [Funcionalidades](#funcionalidades-️)
4. [Diretório](#diretório-️)
5. [Configuração do Ambiente](#-configuração-do-ambiente)
6. [Processos](#processos-)
7. [Link GitHub API's](#link-github-apis)

## Descrição 📝
#### Microsserviço Piadas Chuck Norris

Este projeto é uma arquitetura baseada em microsserviços desenvolvida com foco em escalabilidade e integração de tecnologias modernas. O sistema tem como objetivo gerar, exibir e armazenar piadas do Chuck Norris utilizando diversas ferramentas e serviços independentes, que se comunicam entre si.

## Tecnologias 🛠️
<div align="left">
    <img src="https://skillicons.dev/icons?i=py" height="40" alt="python logo"/>
    <img src="https://skillicons.dev/icons?i=django" height="40" alt="fastapi logo"/>
    <img src="https://skillicons.dev/icons?i=fastapi" height="40" alt="fastapi logo"/>
    <img src="https://skillicons.dev/icons?i=mongo" height="40" alt="mongo logo"/>
    <img src="https://skillicons.dev/icons?i=kafka" height="40" alt="kafka logo"/>
    <img src="https://skillicons.dev/icons?i=docker" height="40" alt="docker logo"/>
    <img src="https://skillicons.dev/icons?i=html" height="40" alt="html logo"/>
    <img src="https://skillicons.dev/icons?i=css" height="40" alt="css logo"/>
    <img src="https://skillicons.dev/icons?i=bootstrap" height="40" alt="bootstrap logo"/>
</div>

---
- **Django**  
  Framework utilizado para criar a interface web que exibe as piadas para o usuário final.

- **FastAPI**  
  Utilizado para construção de dois microsserviços:
  - Uma API que gera uma nova piada de Chuck Norris.
  - Uma API que retorna o histórico de piadas já geradas.

- **MongoDB**  
  Banco de dados NoSQL responsável por armazenar as piadas de forma estruturada.

- **Kafka**  
  Sistema de mensageria que transmite as piadas geradas para um tópico, simulando comunicação entre microsserviços.

- **Docker**  
  Responsável por orquestrar os containers, principalmente para subir os serviços do Kafka e Zookeeper de maneira isolada.

---

## Funcionalidades ⚙️
- A interface do usuário, criada em **Django**, permite gerar novas piadas ao clicar em **"Me conte outra"**.
- Ao gerar uma nova piada, o serviço FastAPI retorna uma resposta com a piada.
- A piada é automaticamente enviada para o **Kafka**.
- Um **consumer** em Python consome essa piada e a insere no banco **MongoDB**.
- O histórico completo de piadas é acessível através de um endpoint da FastAPI.


### Diretório 🗂️
```plaintext
📦 interface_chuck_norris
 ┣ 📂 chuck_norris
 ┣ 📂 docker
 ┣ 📂 piada 
 ┣ 📂 static
 ┣ 📂 templates
 ┣ 📜 .gitignore
 ┣ 📜 manage.py
 ┣ 📜 README.md
 ┣ 📜 requirements.txt
```

### 🔧 Configuração do Ambiente 
#### Instalando bibliotecas necessárias
- 💻 Crie um ambiente virtual
```bash
python -m venv {nome-da-sua-venv}
```

- ▶️ Ative o ambiente virtual
```bash
{nome-da-sua-venv}\Scripts\activate
```

- 🏗️ Instalar todas as bibliotecas nessárias
```bash
pip install -r requirements
```

#### ⚡ Para iniciar o servidor local Django via prompt de comando basta rodar o comando a baixo na pasta raiz
```bash
python manage.py runserver
```

## Processos 🔄
### Página Home
<img src="https://raw.githubusercontent.com/KevinSoffa/front-Chuck-Norris/refs/heads/master/static/img/home.png" height="400" alt="pagina home"/>

### Página Histórico
<img src="https://raw.githubusercontent.com/KevinSoffa/front-Chuck-Norris/refs/heads/master/static/img/pagina_historico.png" height="400" alt="pagina home"/>

### API's
<img src="https://raw.githubusercontent.com/KevinSoffa/front-Chuck-Norris/refs/heads/master/static/img/apis.png" height="400" alt="python logo"/>

### Kafka
<img src="https://raw.githubusercontent.com/KevinSoffa/front-Chuck-Norris/refs/heads/master/static/img/kafka.png" height="400" alt="python logo"/>

## 📬Link GitHub API's
#### API Chuck Norris
```bash
https://github.com/KevinSoffa/API_Chuck_Norris-2.0
```

#### API Chuck Norris Histórico
```bash
https://github.com/KevinSoffa/API_Chuck_Norris-2.0-historico
```