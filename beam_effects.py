import cv2

class BeamEffects:
    def draw_beam(self, frame, eye_center):
        cv2.line(frame, eye_center, (eye_center[0], frame.shape[0]), (0, 0, 255), 6)
        cv2.line(frame, eye_center, (eye_center[0], frame.shape[0]), (235, 245, 255), 4)
        cv2.line(frame, eye_center, (eye_center[0], frame.shape[0]), (255, 255, 255), 2)
        cv2.circle(frame, (eye_center[0], frame.shape[0]), 20, (0, 0, 255), -1)
        cv2.circle(frame, (eye_center[0], frame.shape[0]), 40, (0, 0, 255), 2)
    
    def draw_eye_circle(self, frame, eye_center):
        cv2.circle(frame, eye_center, 10, (255, 255, 0), 2)
        cv2.circle(frame, eye_center, 13, (255, 255, 0), 2)
        cv2.circle(frame, eye_center, 30, (255, 255, 0), 2)
        cv2.drawMarker(frame, eye_center, (255, 255, 0), cv2.MARKER_DIAMOND, 75, 4)