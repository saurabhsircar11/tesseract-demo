from PIL import Image
import pytesseract


im = Image.open("german_prescription.png")
gray = im.convert('L')
bw = gray.point(lambda p: p > 50 and 255)
bw.save("result_bw.png")
text = pytesseract.image_to_string(bw, lang="eng")

print(text)
