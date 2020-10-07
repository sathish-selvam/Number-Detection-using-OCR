import cv2
import pytesseract
import numpy as np
import glob
import os

base = Image.open('Images/AbbiveDashboard_wm.png').convert('RGBA')
width, height = base.size

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))
fnt = ImageFont.truetype("C:\Windows\Fonts\\ariali.ttf",75)
# get a drawing context
d = ImageDraw.Draw(txt)

x = width/2
y = height/2

# draw text, half opacity
d.text((x,y), "This visual is strictly for internal use. Please do", font=fnt, fill=(198,198,198,240))
d.text((x,y+66), "not share with anyone outside the organization.", font=fnt, fill=(198,198,198,240))
# txt = txt.rotate(45)

out = Image.alpha_composite(base, txt)
# out.show()
out.save('output/result.png')
cv2.waitKey(0)






