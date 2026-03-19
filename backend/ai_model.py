import cv2
from deepface import DeepFace

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

MAX_FACES = 10

def analyze_class(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.1, 3)
    faces = faces[:MAX_FACES]

    confused = 0
    attentive = 0
    faces_data = []

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]

        try:
            result = DeepFace.analyze(
                face,
                actions=['emotion'],
                enforce_detection=False,
                detector_backend='opencv'
            )

            emotion = result[0]['dominant_emotion']

            if emotion in ["sad", "fear", "angry", "disgust"]:
                confused += 1
                color = (0, 0, 255)
            else:
                attentive += 1
                color = (0, 255, 0)
                
            faces_data.append({
                "box": (x, y, w, h),
                "color": color,
                "emotion": emotion
            })

        except:
            pass

    total = confused + attentive
    percent = int((confused / total) * 100) if total > 0 else 0

    return faces_data, confused, attentive, percent