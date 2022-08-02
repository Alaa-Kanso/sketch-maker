import cv2

img=input("please enter the name of the image with it's type for ex image.png: ")
image = cv2.imread(img)
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invertImg = cv2.bitwise_not(grayImg)
blurImg = cv2.GaussianBlur(invertImg, (21, 21), 0)
invertedBlur = cv2.bitwise_not(blurImg)
sketch = cv2.divide(grayImg, invertedBlur, scale=256.0)

name=input("please enter the name of what you would like to save your image with .png for ex sketch.png (make sure that each time you run this script you name the sketch something else): ")
cv2.imwrite(name, sketch)
