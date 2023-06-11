import pytesseract
from PIL import Image, ImageEnhance
import os
os.environ['TESSDATA_PREFIX'] = "~/Development/code/torah"

# Open the image file
test_image = Image.open('/home/eli_moshe/Development/code/torah/Screenshot (43).png')

# Extract text using pytesseract
text = pytesseract.image_to_string(test_image, lang='heb')

# Print the extracted text
print(test_image)