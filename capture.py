import cv2
import time

def start():
    camera = cv2.VideoCapture(0)
    time.sleep(2)
    for i in range(1):
        return_value, image = camera.read()
        cv2.imwrite('opencv'+str(i)+'.png', image)
    camera.release()
    del(camera)
    cv2.destroyAllWindows()
