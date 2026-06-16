import cv2
import numpy as np
import os

if not os.path.exists("biometria_usuario.npy"):
    print("Erro: Arquivo 'biometria_usuario.npy' não encontrado. Por favor, execute o 'cadastro.py' primeiro.")
    exit()

# Carrega a biometria salva
print("Carregando biometria salva...")
vetor_salvo = np.load("biometria_usuario.npy")

print("Inicializando modelos YuNet e SFace...")
# Inicializa o detector e o reconhecedor nativos
detector = cv2.FaceDetectorYN.create(
    "face_detection_yunet_2023mar.onnx", "", (320, 320)
)
reconhecedor = cv2.FaceRecognizerSF.create(
    "face_recognition_sface_2021dec.onnx", ""
)

print("Iniciando webcam...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro: Não foi possível abrir a câmera.")
    exit()

print("=====================================================")
print("Posicione seu rosto em frente à câmera para logar.")
print("Pressione 'q' para sair.")
print("=====================================================")

# Limiar recomendado para distância de cosseno no SFace
LIMIAR_COSSENO = 0.363

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro: Não foi possível ler da câmera.")
        break

    # Pega as dimensões do frame e seta no detector
    h, w, _ = frame.shape
    detector.setInputSize((w, h))

    # Detecta rostos
    _, rostos = detector.detect(frame)

    frame_display = frame.copy()

    if rostos is not None:
        for rosto in rostos:
            box = list(map(int, rosto[:4]))
            
            # Extrai o rosto alinhado e o vetor da câmera
            rosto_alinhado = reconhecedor.alignCrop(frame, rosto)
            vetor_camera = reconhecedor.feature(rosto_alinhado)
            
            # Compara usando Similaridade de Cosseno
            score = reconhecedor.match(vetor_salvo, vetor_camera, cv2.FaceRecognizerSF_FR_COSINE)
            
            if score >= LIMIAR_COSSENO:
                # Login com sucesso
                cv2.rectangle(frame_display, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0, 255, 0), 2)
                cv2.putText(frame_display, f"Acesso Liberado! ({score:.2f})", (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            else:
                # Login negado
                cv2.rectangle(frame_display, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0, 0, 255), 2)
                cv2.putText(frame_display, f"Acesso Negado ({score:.2f})", (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Validacao de Login Biometrico", frame_display)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Saindo da validação.")
        break

cap.release()
cv2.destroyAllWindows()
