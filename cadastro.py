import cv2
import numpy as np
import os

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

print("Pressione 'c' para cadastrar seu rosto ou 'q' para sair.")

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

    # Desenha um retângulo se um rosto for encontrado
    if rostos is not None:
        for rosto in rostos:
            # Rostos contém a bounding box (primeiros 4) e pontos faciais
            box = list(map(int, rosto[:4]))
            cv2.rectangle(frame_display, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0, 255, 0), 2)
            cv2.putText(frame_display, "Rosto Detectado", (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Cadastro Biometrico", frame_display)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        if rostos is not None:
            # Extrai o rosto alinhado e o vetor
            rosto_alinhado = reconhecedor.alignCrop(frame, rostos[0])
            vetor_facial = reconhecedor.feature(rosto_alinhado)
            
            # Salva a biometria pura
            np.save("biometria_usuario.npy", vetor_facial)
            print("=====================================================")
            print("Cadastro realizado com sucesso! ")
            print("Arquivo 'biometria_usuario.npy' salvo no disco.")
            print("Pode fechar a janela (apertando q) e rodar o login.py")
            print("=====================================================")
            break
        else:
            print("Nenhum rosto detectado para cadastro! Tente novamente.")
    elif key == ord('q'):
        print("Saindo do cadastro.")
        break

cap.release()
cv2.destroyAllWindows()
