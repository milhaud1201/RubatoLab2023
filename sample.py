import cv2
cap = cv2.VideoCapture("/data/folk_village.mp4")
i = 0
while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    cv2.imwrite(f"/content/drive/MyDrive/Dataset/raw_video/frames/{str(i).zfill(5)}.png", img)
    i += 1