# 🔒 Login Biométrico com Python e OpenCV

Este projeto implementa um sistema de login biométrico simples, rápido e moderno utilizando Python e os modelos de IA nativos do OpenCV (**YuNet** para detecção facial e **SFace** para extração de características).

Diferente de abordagens mais antigas (como as bibliotecas `dlib` e `face_recognition` que costumam causar problemas de compilação em ambientes Windows ou versões mais recentes do Python), este projeto roda suavemente e requer pouquíssimas dependências.

## 🚀 Como funciona

O projeto é dividido em duas partes principais:
1. **Cadastro (`cadastro.py`)**: Captura o rosto via webcam, extrai o vetor matemático (embedding) das suas características faciais usando Deep Learning e o salva localmente de forma segura num arquivo binário `.npy`. (Não salvamos fotos JPG!).
2. **Validação (`login.py`)**: Carrega a biometria salva, captura o rosto de quem está na câmera em tempo real e calcula a Similaridade de Cosseno entre os rostos. Se a pontuação passar do limiar de segurança (0.363), o acesso é liberado.

## 🛠️ Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina (idealmente Python 3.10+).
Instale as bibliotecas necessárias executando:

```bash
pip install opencv-python numpy
```

## 📦 Modelos Pré-Treinados (ONNX)

Para o código funcionar, você precisa baixar os dois modelos oficiais do projeto **OpenCV Zoo** e colocá-los na mesma pasta dos seus scripts `.py`.

1. **YuNet (Detector Facial)**: [Download `face_detection_yunet_2023mar.onnx`](https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx)
2. **SFace (Reconhecedor)**: [Download `face_recognition_sface_2021dec.onnx`](https://github.com/opencv/opencv_zoo/raw/main/models/face_recognition_sface/face_recognition_sface_2021dec.onnx)

## 💻 Como usar

### Passo 1: Registre seu rosto
Execute o script de cadastro no seu terminal:
```bash
python cadastro.py
```
A sua webcam será iniciada. Posicione o seu rosto na frente da câmera até que ele seja detectado (um retângulo verde aparecerá ao redor do seu rosto). Pressione a tecla **`c`** para capturar e salvar sua biometria.

### Passo 2: Faça o Login
Com o arquivo `biometria_usuario.npy` gerado, rode o script de validação:
```bash
python login.py
```
A webcam abrirá novamente. O sistema irá comparar o seu rosto ao vivo com a biometria salva. Se for você, a mensagem **"Acesso Liberado!"** aparecerá em verde junto com o seu *score* de similaridade. Pressione **`q`** para sair.

## 💡 Ideias de Integração (Launcher)

Você pode usar esse sistema como uma "chave" de entrada para abrir outros programas e jogos! 
No arquivo `login.py`, substitua o trecho de "Acesso Liberado" para desativar a câmera e chamar o seu app principal:

```python
import subprocess

# ... código
if score >= LIMIAR_COSSENO:
    cap.release()
    cv2.destroyAllWindows()
    # Inicia o seu sistema/jogo real
    subprocess.run(["python", "meu_jogo.py"])
    break
```

---
*Projeto criado para fins educacionais e provas de conceito.*
