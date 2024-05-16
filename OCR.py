import cv2
import pytesseract

def ocr(imagefile):
    image = cv2.imread(imagefile)

    # path
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(imagefile)
    print("Extracted Text:")
    print(text)

ocr("imagefile.png")
