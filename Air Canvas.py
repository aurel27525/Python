import cv2
import numpy as np
import mediapipe as mp

#Atur set
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7)

colors = [(255,0,0),(0,255,0),(0,0,255),(0,255,255)]
colorIndex = 0

canvas = np.ones((480,640,3),dtype=np.uint8)*255
prev_x, prev_y = None, None

cap = cv2.VideoCapture(0)

#Loop 
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame,1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    #Tombol gambar
    cv2.rectangle(frame,(40,1),(140,80),(122,122,122),-1)
    cv2.rectangle(frame,(160,1),(255,80),colors[0],-1)
    cv2.rectangle(frame,(275,1),(370,80),colors[1],-1)
    cv2.rectangle(frame,(390,1),(485,80),colors[2],-1)
    cv2.rectangle(frame,(505,1),(600,80),colors[3],-1)

    cv2.putText(frame,"CLEAR",(45,45),0,0.6,(0,0,0),2)
    cv2.putText(frame,"BLUE",(170,45),0,0.6,(255,255,255),2)
    cv2.putText(frame,"GREEN",(275,45),0,0.6,(255,255,255),2)
    cv2.putText(frame,"RED",(405,45),0,0.6,(255,255,255),2)
    cv2.putText(frame,"YELLOW",(505,45),0,0.6,(0,0,0),2)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        lm = hand.landmark

        #Posisi ujung jari telunjuk
        x = int(lm[8].x * w)
        y = int(lm[8].y * h)
        cv2.circle(frame,(x,y),8,(0,0,0),-1)

        #Deteksi jari
        index_up = lm[8].y < lm[6].y
        middle_up = lm[12].y < lm[10].y

        #Pilih warna
        if y < 100:
            prev_x, prev_y = None, None
            if 40 <= x <= 140:
                canvas[:] = 255
            elif 160 <= x <= 255:
                colorIndex = 0
            elif 275 <= x <= 370:
                colorIndex = 1
            elif 390 <= x <= 485:
                colorIndex = 2
            elif 505 <= x <= 600:
                colorIndex = 3

        #Gambar 1 jari
        elif index_up and not middle_up:
            if prev_x is None:
                prev_x, prev_y = x, y
            cv2.line(canvas,(prev_x,prev_y),(x,y),colors[colorIndex],5)
            prev_x, prev_y = x, y

        #Gambar 2 jari
        else:
            prev_x, prev_y = None, None
    else:
        prev_x, prev_y = None, None

    cv2.imshow("Air Canvas - MediaPipe", frame)
    cv2.imshow("Canvas", canvas)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()