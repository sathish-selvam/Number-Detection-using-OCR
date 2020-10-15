import cv2
import pytesseract
import numpy as np
import glob
import os

from blurImage import blur_found_area;

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

print(pytesseract.get_tesseract_version())

cong = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ --oem 1 --psm 11 outputbase digits'

class MyImage:
    def __init__(self, img_name):
        self.img = cv2.imread(img_name)
        self.__name = img_name

    def __str__(self):
        return self.__name

img_dir = ".\Images\\"
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []
for f1 in files:
    print(f1)
    img = cv2.imread(f1)
    img2 = img.copy()
    hImg, wImg,_ = img.shape
    imageName = MyImage(f1);
    newfileName = str(imageName).replace(img_dir, "").replace(".png","")
    # print(newfileName)
    # Detecting Words
    boxes = pytesseract.image_to_data(img, config=cong)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                img2[y:y + h, x:x + w] = cv2.blur(img2[y:y + h, x:x + w], (10, 10))

    # Detecting Charecters
    # boxes = pytesseract.image_to_boxes(img, config=cong)
    # for b in boxes.splitlines():
    #     b = b.split(" ")
    #     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    #     cv2.rectangle(img, (x, (hImg-y)), (w, hImg-h), (0, 0, 225), 2)
    #     img[y:y + h, x:x + w] = cv2.blur(img[y:y + h, x:x + w], (5, 5))



    # cv2.imshow('result', img2)
    cv2.imwrite("output/FirstFry/"+newfileName+".png", img2)










#Detecting Words

# cv2.imshow('Result', img2)
cv2.waitKey(0)






