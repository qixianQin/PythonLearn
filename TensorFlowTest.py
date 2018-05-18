# -*- conding:utf-8 -*- 


###  生成简单图形验证码    
# from captcha.image import ImageCaptcha
# from PIL import Image 

# text = '12344d'
# image = ImageCaptcha()
# captcha = image.generate(text)
# captcha_image = Image.open(captcha)
# captcha_image.show()     ##  生成一张图片




###  生成随机的四个数字

from PIL import Image 
from captcha.image import ImageCaptcha
import numpy as np 

VOCAB = ['0','1','2','3','4','5','6','7','8','9']
CAPTCHA_LENGTH = 4
VOCAB_LENGTH = len(VOCAB)

def generate_captcha(captcha_text):
	"""
	get captcha text and np array
	:param captcha_text： source text 
	:return: captcha image and array 
	"""
	image = ImageCaptcha()
	captcha = image.generate(captcha_text)
	captcha_image = Image.open(captcha)
	captcha_array = np.array(captcha_image)
	return captcha_array

captcha = generate_captcha('1234')
print(captcha, captcha.shape)
