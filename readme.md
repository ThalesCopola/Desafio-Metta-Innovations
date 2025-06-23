# Detecção de Pessoas com YOLOv8

Esse projeto detecta pessoas em vídeos usando a rede neural YOLOv8 (pré-treinada). Ele gera um novo vídeo com as detecções desenhadas (caixas ao redor das pessoas), arquivos .json com contagem de pessoas e uma interface gráfica para visualizar tudo com gráfico.


## O que precisa

- Python 3.9 ou superior
- (Opcional) Virtualenv para isolar o ambiente


## Funcionalidades

- Detecção de pessoas em todos os frames de um vídeo com a geração de:
  - video_out.mp4 com boxes desenhadas nos frames.
  - history.json com a contagem de pessoas por frame.
  - alerts.json com frames onde a contagem ultrapassa o limite definido.
  - Interface gráfica (GUI) que mostra o vídeo e um gráfico da contagem de pessoas ao longo do tempo.


## Instalação

## Crie e ative um ambiente virtual:

No terminal, executa os comando abaixo:

No Windows:

 python -m venv venv

venv\Scripts\activate

No Linux/macOS:

source venv/bin/activate

## Após, instale as dependências

- pip install -r requirements.txt 

## As principais dependências incluem:
.opencv-python==4.11.0.86
.matplotlib==3.10.3
.pillow==11.2.1
.torch==2.7.1
.torchvision==0.22.1
.ultralytics==8.3.156

## Executando o projeto

 Rode a detecção:

 python detector.py sample/people-walking.mp4 4 

Onde o número 4 é o limite de pessoas por frame para gerar alertas no arquivo alerts.json

 E ao final rode a interface gráfica:

  python gui.py






