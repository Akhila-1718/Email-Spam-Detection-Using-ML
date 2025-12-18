import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)
import easyocr

# Initialize EasyOCR reader (English)
reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path):
    """
    Extracts text from an image using EasyOCR
    """
    result = reader.readtext(image_path, detail=0)
    return " ".join(result)
    result = real_world_spam_detector(
    "Check this deal!", 
    image_path="spam_image.png"
)
print("Detected:", result)


