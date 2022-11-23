import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'F:\Tesseract\tesseract.exe' # путь к tesseract.exe

def get_img(width, height, imgname = 'white.png'):
    image = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    image.save(imgname)
    return imgname


def get_text_from_image(image_path):

    img = Image.open(image_path)

    enhancer = ImageEnhance.Contrast(img)
    factor = 0.7
    im_output = enhancer.enhance(factor)
    enhancer = ImageEnhance.Brightness(im_output)

    factor = 1.4
    im_output = enhancer.enhance(factor)
    enhancer = ImageEnhance.Sharpness(im_output)

    factor = 7
    im_output = enhancer.enhance(factor)
    im_output.save(image_path)

    img_grey = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    thresh = 120
    img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite(image_path, img_binary)

    image = cv2.imread(image_path)
    string = pytesseract.image_to_string(image, lang="eng+rus")
    return string


def draw_text_on_img(image_path):
    image = Image.open(get_img(820, 820))
    font = ImageFont.truetype("arial.ttf", 25)
    drawer = ImageDraw.Draw(image)
    drawer.text((50, 100), get_text_from_image(image_path), font=font, fill='black')
    image.show()


draw_text_on_img("1.png")
