import cv2
import pygame
import numpy as np

class BeamEffects:
    def __init__(self):
        pygame.mixer.init()
        self.sound1 = pygame.mixer.Sound('sound/beam1.mp3')
        self.sound2 = pygame.mixer.Sound('sound/laser.mp3')

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
        
    # 眼から、右下斜めと左下斜めにビームが出るようにする、そのビームの間を埋めるように色を塗る(fillpolyを使う, 色を埋める, 半透明, 黄色)
    def draw_beam_multiple(self, frame, eye_center):
        bottom_center = (frame.shape[1] // 2, frame.shape[0])
        pts = np.array([[eye_center[0], eye_center[1]], [frame.shape[1], frame.shape[0]], [frame.shape[1], frame.shape[0]], bottom_center], np.int32)
        pts2 = np.array([[eye_center[0], eye_center[1]], [0, frame.shape[0]], bottom_center], np.int32)
        pts = pts.reshape((-1, 1, 2))
        pts2 = pts2.reshape((-1, 1, 2))
        cv2.fillPoly(frame, [pts], (0, 255, 255))
        cv2.fillPoly(frame, [pts2], (0, 255, 255))

    def play_sound1(self):
        self.sound1.play()
    
    def play_sound2(self):
        self.sound2.play()

# commitmessage: "add draw_beam_multiple