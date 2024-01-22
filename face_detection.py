import cv2
import numpy as np

# 顔認識器の読み込み
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 目の認識器の読み込み
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# ビームの描画色とサイズ
# beam_color = (0, 255, 0)
# beam_thickness = 5

# カメラの起動
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            eye_center = (x + ex + ew // 2, y + ey + eh // 2)# 目の中心座標
            #魔法陣を描画
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255, 255, 0), 2)# 眼の中心座標を描画1
            cv2.circle(frame, eye_center, 10, (255, 255, 0), 2)# 眼の中心座標を描画2
            cv2.circle(frame, eye_center, 13, (255, 255, 0), 2)
            cv2.circle(frame, eye_center, 30, (255, 255, 0), 2)
            cv2.drawMarker(frame, eye_center, (255, 255, 0), cv2.MARKER_DIAMOND, 75, 4)
            # 画面の下方向に画面端までビームを描画する
            cv2.line(frame, eye_center, (eye_center[0], frame.shape[0]), (0, 0, 255), 6)
            cv2.line(frame, eye_center, (eye_center[0], frame.shape[0]), (235, 245, 255), 4)
            cv2.line(frame, eye_center, (eye_center[0], frame.shape[0]), (255, 255, 255), 2)
            # ビームが端に来たら爆発するエフェクトを描画する
            cv2.circle(frame, (eye_center[0], frame.shape[0]), 20, (0, 0, 255), -1)
            cv2.circle(frame, (eye_center[0], frame.shape[0]), 40, (0, 0, 255), 2)

    # 結果の表示
    cv2.imshow('Face Recognition with Beam', frame)

    # 終了条件
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラの解放
cap.release()
cv2.destroyAllWindows()

