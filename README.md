<div align="center">
  <h1>🔒 Login Biométrico com Python e OpenCV</h1>
  <p><i>Um sistema de login biométrico moderno, leve e eficiente utilizando modelos de IA nativos do OpenCV.</i></p>
</div>

<br>

Este projeto implementa uma solução de login biométrico utilizando a linguagem Python aliada aos modelos de Inteligência Artificial nativos da biblioteca OpenCV: **YuNet** (para detecção facial) e **SFace** (para extração e reconhecimento de características).

Ao contrário de abordagens tradicionais que dependem de bibliotecas como `dlib` e `face_recognition` — que frequentemente apresentam desafios de compilação em ambientes Windows ou conflitos em versões mais recentes do Python —, esta implementação destaca-se pela sua facilidade de execução, alta performance e baixa dependência de pacotes externos.

---

## ✨ Principais Características

- **Leveza e Eficiência**: Requer pouquíssimas dependências para funcionar, garantindo uma instalação rápida e livre de dores de cabeça.
- **Foco em Privacidade**: A biometria é processada e armazenada localmente em um vetor matemático (arquivo `.npy`), eliminando a necessidade de armazenar imagens ou fotografias dos usuários.
- **Alta Compatibilidade**: Construído utilizando as ferramentas nativas do OpenCV, o que confere ao projeto uma estabilidade superior em diversos sistemas operacionais.
- **Simplicidade de Integração**: Arquitetura direta, facilitando a sua adaptação como um módulo de autenticação em aplicações maiores.

---

## 🚀 Arquitetura e Funcionamento

A estrutura do sistema é dividida de forma modular em duas etapas fundamentais:

1. **Módulo de Cadastro (`cadastro.py`)**:
   - Acessa a webcam e captura a imagem do usuário.
   - Utiliza as redes neurais profundas (Deep Learning) para extrair o vetor matemático (embedding) que representa as características únicas da face detectada.
   - Salva estas informações de forma segura no disco local em um arquivo binário `.npy`.

2. **Módulo de Validação (`login.py`)**:
   - Realiza o carregamento da biometria previamente cadastrada.
   - Captura, em tempo real, o rosto posicionado diante da câmera.
   - Calcula a **Similaridade de Cosseno** entre a face lida e a biometria arquivada. O acesso é concedido exclusivamente se a pontuação obtida superar o limiar de segurança estipulado (0.363).

---

## 🛠️ Pré-requisitos

Para que o projeto funcione corretamente, certifique-se de ter o Python instalado em seu ambiente (versão recomendada: **Python 3.10+**).

Instale as dependências necessárias através do gerenciador de pacotes `pip`:

```bash
pip install opencv-python numpy
```

---

## 📦 Modelos Pré-Treinados (ONNX)

O funcionamento correto da aplicação depende de dois modelos oficiais do repositório **OpenCV Zoo**. É obrigatório realizar o download dos arquivos abaixo e alocá-los no mesmo diretório em que se encontram os scripts `.py`:

1. **YuNet (Detector Facial)**: [Download `face_detection_yunet_2023mar.onnx`](https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx)
2. **SFace (Reconhecedor Facial)**: [Download `face_recognition_sface_2021dec.onnx`](https://github.com/opencv/opencv_zoo/raw/main/models/face_recognition_sface/face_recognition_sface_2021dec.onnx)

---

## 💻 Como Usar

### Passo 1: Cadastro da Biometria Facial
No terminal, execute o script correspondente ao cadastro:

```bash
python cadastro.py
```
*A sua webcam será ativada. Posicione-se de frente para a câmera até que a detecção ocorra (indicada por um retângulo verde ao redor do rosto). Em seguida, pressione a tecla **`c`** para capturar e gravar os seus dados biométricos.*

### Passo 2: Autenticação / Login
Com o arquivo `biometria_usuario.npy` devidamente gerado no passo anterior, inicie o processo de validação:

```bash
python login.py
```
*A câmera será novamente acionada e o sistema fará a comparação do rosto detectado com a biometria cadastrada. Em caso de sucesso, será exibida na tela a mensagem **"Acesso Liberado!"** destacada em verde, acompanhada da sua pontuação (score) de similaridade. Pressione a tecla **`q`** a qualquer momento para encerrar.*

---

## 💡 Ideias de Integração (Launcher)

A flexibilidade deste projeto permite que ele opere como uma "chave" de segurança para o acesso a outros softwares, painéis ou jogos.

Como exemplo prático, você pode modificar o script `login.py`. Substitua o bloco onde a validação é bem-sucedida pelo encerramento da câmera e o acionamento da sua aplicação principal:

```python
import subprocess

# ... restante do código ...

if score >= LIMIAR_COSSENO:
    cap.release()
    cv2.destroyAllWindows()

    # Inicia o seu sistema ou jogo principal
    subprocess.run(["python", "meu_jogo.py"])
    break
```

---
<div align="center">
  <i>Projeto desenvolvido com propósitos educacionais e como prova de conceito (PoC).</i>
</div>
