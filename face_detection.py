import cv2
import numpy as np

# 顔認識器の読み込み
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 目の認識器の読み込み
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# ビームの描画色とサイズ
beam_color = (0, 255, 0)  # RGB (Green)
beam_thickness = 5

# カメラの起動
cap = cv2.VideoCapture(1)

while True:
    # フレームの読み込み
    ret, frame = cap.read()

    # グレースケールに変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 顔の検出
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # 顔の範囲を切り取り
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # 目の検出
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            # 目の中心座標
            eye_center = (x + ex + ew // 2, y + ey + eh // 2)

            # ビームの描画
            cv2.line(frame, eye_center, (eye_center[0] + 100, eye_center[1] + 100), beam_color, beam_thickness)

    # 結果の表示
    cv2.imshow('Face Recognition with Beam', frame)

    # 終了条件
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラの解放
cap.release()
cv2.destroyAllWindows()