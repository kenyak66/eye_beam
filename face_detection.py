import cv2
from beam_effects import BeamEffects

class FaceDetection:
    def __init__(self, video_source=0):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        self.cap = cv2.VideoCapture(video_source)
        self.beam_effects = BeamEffects()

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray)
        return faces, gray
    
    def draw_beam_effects(self, frame, eye_center):
        self.beam_effects.draw_beam(frame, eye_center)
    
    def draw_eye_circle(self, frame, eye_center):
        self.beam_effects.draw_eye_circle(frame, eye_center)

    def run(self):
        while True:
            ret, frame = self.cap.read()
            faces, gray = self.detect_faces(frame)

            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]
                eyes = self.eye_cascade.detectMultiScale(roi_gray)

                for (ex, ey, ew, eh) in eyes:
                    eye_center = (x + ex + ew // 2, y + ey + eh // 2)
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)
                    self.draw_eye_circle(frame, eye_center)
                    self.draw_beam_effects(frame, eye_center)

            cv2.imshow('Face Recognition with Beam', frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    face_recognition = FaceDetection(video_source=1)
    face_recognition.run()