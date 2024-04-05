# RobotFlask-Ponderada - Gustavo Wagon Widman
Esta atividade tem por objetivo realizar uma integração do sistema construído com Flask e o robô físico. O estudante deverá construir um sistema que realiza o log dos comandos enviados por uma interface gráfica construída com HTMX e servida com Flask em um servidor local. Neste servidor, o robô físico deve estar conectado. Quando o robô não estiver conectado, apenas as funcionalidades de visualização do log devem estar disponíveis no sistema. A forma como a interface do sistema será construída fica a critério do estudante, desde que contemple no mínimo: - Uma interface de dashboard para visualizar os logs do sistema; - Uma interface que permita controlar o robô. O banco de dados utilizado deve ser o TinyDB. Como barema, espera-se encontrar: 1. Backend construído em Flask conectado ao banco de dados TinyDB (até 2.0 pontos); 2. Frontend construído com HTMX (até 2.0 pontos); 3. O sistema verifica se o robô está conectado e exibe as interfaces corretamente (até 2.0 pontos); 4. Existe uma página funcional de controle do robô (até 2.0 pontos); 5. Existe uma página funcional de exibição de logs do sistema (até 2.0 pontos).

## Descrição

O projeto consiste em um sistema que realiza o log dos comandos enviados por uma interface gráfica construída com HTMX e servida com Flask em um servidor local. Neste servidor, o robô físico deve estar conectado. Quando o robô não estiver conectado, apenas as funcionalidades de visualização do log ficam disponíveis no sistema. A interface do sistema foi construída com o intuito de ser simples e intuitiva, contendo um dashboard para visualizar os logs do sistema e uma interface que permite controlar o robô.

## Instalação e execução

### Para instalar as dependências do projeto, comece clonando o repositório

```bash
git clone https://github.com/GustavoWidman/Prova2-Modulo1.git
```

### Depois, entre na pasta do projeto, e crie um ambiente virtual (venv)

```bash
cd Prova2-Modulo1
```

```bash
python -m venv venv
```

OU (usando [uv](https://github.com/astral-sh/uv))

```bash
uv venv venv
```

### Ative o ambiente virtual com o seguinte comando

```bash
source venv/bin/activate
```

OU (no Windows)

```bash
.\venv\Scripts\activate
```

### Finalmente, instale as dependências do projeto com o comando:

```bash
pip install -r requirements.txt
```

OU (usando [uv](https://github.com/astral-sh/uv))

```bash
uv pip install -r requirements.txt
```

### Para rodar o projeto, execute:

```bash
python src/main.py
```

## Estrutura do projeto

A estrutura do projeto é composta por pastas e arquivos que organizam os comandos, classes e utilitários. Segue abaixo a estrutura do projeto, resultado do comando `tree --gitignore`

```bash
.
├── README.md
├── requirements.txt
├── src
│   ├── classes
│   │   └── robot.py
│   ├── database
│   │   ├── archives
│   │   │   └── logs.json
│   │   └── wrapper.py
│   ├── main.py
│   ├── routes
│   │   ├── frontend.py
│   │   ├── logs.py
│   │   ├── main.py
│   │   └── robot.py
│   ├── templates
│   │   ├── current.html
│   │   ├── dashboard.html
│   │   ├── index.html
│   │   ├── log_list.html
│   │   ├── logs.html
│   │   └── no_robot.html
│   └── utils
│       ├── logger.py
│       ├── ports.py
│       └── text.py
└── video
    ├── logs.mp4
    ├── main.mp4
    └── no_robot.mp4
```

## Rotas

O projeto possui as seguintes rotas:

### API

#### Logs

- `GET /api/logs` - Retorna todos os logs do sistema
- `DELETE /api/logs/<id>` - Deleta um log específico
- `DELETE /api/logs` - Deleta todos os logs

### Robot

- `GET /api/robot/current` - Retorna o estado atual do robô (x, y, z) em forma de mídia HTML.
- `POST /api/robot/move` - Move o robô para uma posição específica (x, y, z)
- `POST /api/robot/move_unsafe` - Move o robô para uma posição específica (x, y, z) de maneira insegura (movimento brusco, sem mover verticalmente para cima e depois para baixo para impedir colisões)
- `POST /api/robot/home` - Move o robô para a posição home (250, 0, 150)
- `POST /api/robot/tool` - Ativa ou desativa uma ferramenta no robô
- `GET /api/robot` - Resolve se o robô esta disponível ou nao retornando mídia HTML.

Campos obrigatórios para as rotas de movimento: `x`, `y`, `z`
Campos obrigatórios para a rota de ativação de ferramenta: `tool` e `state`

### Frontend

- `GET /` - Página inicial do sistema (dashboard)
- `GET /logs` - Página de logs do sistema

## Vídeos

Os vídeos de demonstração do projeto estão disponíveis na pasta `video`. Os vídeos são:

### `main.mp4` - Demonstração do projeto com o robô conectado

https://github.com/GustavoWidman/RobotFlask-Ponderada/assets/123963822/21177b0c-0d77-4391-bdf7-362b1aafff6f

### `no_robot.mp4` - Demonstração do projeto sem o robô conectado

https://github.com/GustavoWidman/RobotFlask-Ponderada/assets/123963822/f4e34565-990e-4da8-82d9-9e180556cd8c

### `logs.mp4` - Demonstração da página de logs do sistema

https://github.com/GustavoWidman/RobotFlask-Ponderada/assets/123963822/53f16ce8-f612-4d46-a152-9e6f09b0b227

## Dependências

- PyDobot 1.3.2
- Flask 3.0.2
- TinyDB 4.8.0
- PySerial 3.4

## Dependências frontend

- HTMX 1.9.11
- Bulma CSS 1.0.0

## Autor

Gustavo Wagon Widman
