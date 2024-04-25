# import pytesseract
# import cv2
#
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Sudhanshu\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
# img = cv2.imread('whatsapp.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
#
# # detecting characters
# # hImg, wImg, _ = img.shape
# # boxes = pytesseract.image_to_boxes(img)
# #
# # for b in boxes.splitlines():
# #     b = b.split(' ')
# #     print(b)
# #     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
# #     cv2.rectangle(img, (x,hImg-y), (w,hImg-h), (0,0,255), 1)
# #     cv2.putText(img, b[0], (x,hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 1)
#
# # detecting words
# hImg, wImg, _ = img.shape
# # cong = r'--oem 3 --psm 6 outputbase digits'
# boxes = pytesseract.image_to_data(img, )
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b = b.split()
#         print(b)
#         if len(b) == 12:
#             x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img, (x,y), (w+x,h+y), (0,0,255), 1)
#             cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 1)
#
#
#
#
# # print(pytesseract.image_to_string(img))
# cv2.imshow('result',img)
# cv2.waitKey(0)

# //////////////////////////////////////////////////////////////////////////////////////////////
# import cv2
# import easyocr
# import matplotlib.pyplot as plt
#
# img = cv2.imread('whatsapp.jpg')
#
# reader = easyocr.Reader(['en'], gpu=False)
#
# text_ = reader.readtext(img)
# for t in text_:
#     print(t)
#     bbox, text, score = t
#     print("Bounding Box:", bbox)
#     # Extracting individual points of the bounding box
#     x1, y1 = bbox[0]
#     x2, y2 = bbox[1]
#     x3, y3 = bbox[2]
#     x4, y4 = bbox[3]
#     # Drawing the rectangle using all four points
#     cv2.rectangle(img, (int(x1), int(y1)), (int(x3), int(y3)), (0, 0, 255), 3)
#     # Put text on the image
#     cv2.putText(img, text, (int(x1), int(y1)), cv2.FONT_HERSHEY_COMPLEX, 0.65, (0, 255, 0), 2)
#
#     # cv2.rectangle(img, bbox[0], bbox[2], (0, 0, 255), 3)
#     # cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()
#

# /////////////////////////////////////////////////////////////////////

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Sudhanshu\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

dire=input("Type full path to image you want to convert to text:")
im = Image.open(dire)

language=input("Type the language of the scanned document (3 letter ID):")
text = pytesseract.image_to_string(im, lang=language)
filename=input("Type output file name:")
file1 = open(filename+"-"+language+".txt","w")
file1.write(text)
file1.close()
print("Done...")