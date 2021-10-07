import cv2

cap = cv2.VideoCapture(0)

size = (int(cap.get(3)), int(cap.get(4)))
character_codes = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
output = cv2.VideoWriter('Video.mp4', character_codes, 20, size)

while True:
    success, img = cap.read()
    frame = cv2.flip(img, 1)

    output.write(frame)

    cv2.imshow("frame", frame)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

output.release
cap.release()
cv2.destroyAllWindows()
