import cv2
import pytesseract
import numpy as np
import glob
import os

from PIL import Image, ImageDraw, ImageFont

class MyImage:
    def __init__(self, img_name):
        self.img = cv2.imread(img_name)
        self.__name = img_name

    def __str__(self):
        return self.__name

img_dir = ".\output\SecondFry"
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []
for f1 in files:

    base = Image.open(f1).convert('RGBA')
    width, height = base.size
    imageName = MyImage(f1);
    newfileName = str(imageName).replace(img_dir, "").replace(".png","");
    print(newfileName)
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype("C:\Windows\Fonts\\ariali.ttf", 75)
    # get a drawing context
    d = ImageDraw.Draw(txt)
 
    x = width / 2
    y = height / 2

    # draw text, half opacity
    d.text((x - 700, y - 33), "First Line of Statement", font=fnt, fill=(198, 198, 198, 240))
    d.text((x - 700, y + 33), "Second Line of Statement", font=fnt, fill=(198, 198, 198, 240))
    # txt = txt.rotate(45)

    out = Image.alpha_composite(base, txt)
    # out.show()
    out.save('output/watermark/'+newfileName+"_wm.png")


    # cv2.imshow('result', img2)
    # cv2.imwrite("output/"+newfileName, img2)










#Detecting Words

cv2.waitKey(0)






