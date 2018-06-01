import pytesseract
from PIL import Image
import ipdb

image = Image.open('/Users/chen/cjxh/321519391307_.pic.jpg')
text = pytesseract.image_to_string(image)
ipdb.set_trace()
print(text)
