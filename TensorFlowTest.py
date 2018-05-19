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


# [[251 245 247]
#   [251 245 247]
#   [251 245 247]
#   ...
#   [251 245 247]
#   [251 245 247]
#   [251 245 247]]

#  [[251 245 247]
#   [251 245 247]
#   [251 245 247]
#   ...
#   [251 245 247]
#   [251 245 247]
#   [251 245 247]]] (60, 160, 3)    高度是 60，宽度是 160，是 60 x 160 像素的验证码，
#   每个像素都有 RGB 值，所以最后一维即为像素的 RGB 值高度是 60，宽度是 160，是 60 x 160 
#   像素的验证码，每个像素都有 RGB 值，所以最后一维即为像素的 RGB 值



def text2ver(text):
	"""
	text to one-hot vector 
	:param text: source text
	:return: np array
	"""
	if len(text) > CAPTCHA_LENGTH:
		return False
	vector = np.zeros(CAPTCHA_LENGTH * VOCAB_LENGTH)
	for i, c in enumerate(text):
		index = i * VOCAB_LENGTH + VOCAB.index(c)
		vector[index] = 1
	return vector

def vec2text(vector):
	"""
	vector to captcha text
	:param vector: np array
	:return:  text 
	"""
	if not isinstance(vector, np.ndarray):
		vector = np.asarray(vector)
	vector = np.reshape(vector, [CAPTCHA_LENGTH, -1])
	text = ''
	for item in vector:
		text += VOCAB[np.argmax(item)]
	return text 

vector = text2ver('1234')
text = vec2text(vector)
print(vector, text)

# [0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.
#  0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0.] 1234



import random 
from os.path import join, exists
import pickle 
import numpy as np 
from os import makedirs 

DATA_LENGTH = 10000
DATA_PATH = 'data'

def get_random_text():
	text = ''
	for i in range(CAPTCHA_LENGTH):
		text += random.choice(VOCAB)
	return text 

def generate_data():
	print('Generating Data ...')
	data_x, data_y = [], []

	# generate data x and y
	for i in range(DATA_LENGTH):
		text = get_random_text()
		#get captcha array 
		captcha_array = generate_captcha(text)
		#get vector
		vector = text2ver(text)
		data_x.append(captcha_array)
		data_y.append(vector)

	#write data to pickle 
	if not exists(DATA_PATH):
		makedirs(DATA_PATH)

	x = np.asarray(data_x, np.float32)
	y = np.asarray(data_y, np.float32)
	with open(join(DATA_PATH, 'data.pkl'), 'wb') as f:
		pickle.dump(x, f)
		pickle.dump(y, f)

with open('data.pkl', 'rb') as f:
	data_x = pickle.load(f)
	data_y = pickle.load(f)
	return standardize(data_x), data_y

train_x, text_x, train_y, test_y = train_test_split(data_x, data_y,test_size=0.4, random_state=40)
dev_x, test_x, dev_y, test_y = train_test_split(test_x, test_y, test_size=0.5, random_state=40)