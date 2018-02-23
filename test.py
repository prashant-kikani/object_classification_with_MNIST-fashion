'''
0 	T-shirt/top
1 	Trouser
2 	Pullover
3 	Dress
4 	Coat
5 	Sandal
6 	Shirt
7 	Sneaker
8 	Bag
9 	Ankle boot
'''
import warnings
warnings.filterwarnings("ignore")
import cv2
import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
import keras
import sys
import collections

model = load_model('mnist_fashion.h5')
from keras.optimizers import RMSprop
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(), metrics=['accuracy'])
items = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
file = sys.argv[1]
img = cv2.imread(file, 0)
img = img.astype('float32')
'''
for i in range(28):
    for j in range(28):
        img[i][j] = 255 - img[i][j]
'''
img = img / 255
img = cv2.resize(img,(28,28))
img = np.reshape(img,[1,28,28,1])
plt.imshow(img.reshape(28,28))
plt.show()
classes = model.predict(img).tolist()
# print(classes)
cla = classes[0].copy()
# print("cla : ", cla)
classes[0].sort(reverse = True)
# print("sorted : ", classes[0])
for i, c in enumerate(classes[0]):
	# print("i : ", i, "c : ", c)
	ind = cla.index(c)
	# print("ind : ", ind)
	print(items[ind], " : ", classes[0][i])
y= np.argmax(classes, axis = 1)	
# print(y, " ", items[y[0]])
