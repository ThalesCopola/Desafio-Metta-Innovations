#  Detecção de Pessoas com YOLOv8

Neste projeto, o objetivo principal foi desenvolver uma solução que detecta pessoas em vídeos usando uma rede neural pré-treinada, ou seja, sem precisar treinar nenhum modelo do zero. A ideia é simples: pegar um vídeo, analisar cada frame, contar quantas pessoas aparecem e gerar resultados fáceis de entender e usar.


## Como o projeto funciona 

1. **Leitura do vídeo frame a frame**: 
O programa abre o vídeo e lê um quadro de cada vez para analisar.  

2. **Detecção das pessoas com YOLOv8**: 
Em cada frame, o modelo YOLOv8 (que já está treinado para identificar objetos) é usado para detectar todas as pessoas presentes. 

3. **Desenho das caixas (bounding boxes)**: 
Para facilitar a visualização, o programa desenha um retângulo ao redor de cada pessoa detectada naquele frame.  

4. **Registro dos dados**: 
O programa conta quantas pessoas foram detectadas em cada frame e salva esses dados em dois arquivos JSON, um com a contagem total por frame (history.json) e 
outro só com os frames que ultrapassam o limite definido, para alertas (alerts.json).  

5. **Geração do vídeo final**: 
Um novo vídeo é criado, contendo todas as detecções visuais.  

6. **Visualização via interface gráfica (GUI)**: 
O programa ainda mostra tudo isso em uma janela com o vídeo processado e um gráfico que mostra como a quantidade de pessoas varia ao longo do tempo.  


## Ferramentas utilizadas

 **YOLOv8 (Ultralytics)**: 
 Para a detecção de pessoas nos frames do vídeo (detector.py). Uma das redes mais modernas para detecção de objetos, rápida, eficiente e fácil de usar. Por ser pré-treinada, evita o trabalho pesado do treinamento.  
 **OpenCV**:
 Para abrir, ler e manipular o vídeo, além de desenhar as caixas e salvar o vídeo de saída (detector.py e utils.py). Ferramenta padrão para manipulação de vídeo e imagens, simples de usar para ler frames, desenhar caixas e gerar o vídeo final.  
 **Tkinter**:
 Para criar a interface gráfica (gui.py), uma interface leve e funcional que já vem com o Python, ideal para exibir vídeo e gráficos sem complicação.  
 **Matplotlib**: 
 Usado dentro do gui.py para criar o gráfico da contagem de pessoas ao longo dos frames, integrado com Tkinter. Uma biblioteca popular para gráficos que permite mostrar a variação da contagem de pessoas ao longo do vídeo.  


## Sobre o aprendizado

Esse projeto foi um ótimo desafio proposto para integrar diversas ferramentas e conceitos, capazes de unir a visão computacional com o GUI. Excelente oportunidade de aprofundar redes neurais pré-treinadas e manipular vídeos em Python através de um exercício de pesquisa e prática, que resultou numa solução completa e funcional.


## Prints da aplicação rodando

### 1. GUI após abrir
![GUI após abrir](./prints/print%201.PNG)

### 2. GUI em reprodução detectando pessoas
![GUI em reprodução detectando pessoas](./prints/print%202.PNG)

### 3. GUI sem detectar pessoas
![GUI sem detectar pessoas](./prints/print%203.PNG)

### 4. GUI detectando pessoas com reprodução pausada
![GUI detectando pessoas com reprodução pausada](./prints/print%204.PNG)

### 5. GUI detectando pessoas com objetos em cena
![GUI detectando pessoas com objetos em cena](./prints/print%205.PNG)

