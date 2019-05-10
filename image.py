from PIL import Image
import pytesseract

im= Image.open("new_image.jpg")
text= pytesseract.image_to_string(im,lang="eng")

print(text)