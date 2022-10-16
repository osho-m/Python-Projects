print("Entropy")
import numpy as np
from skimage import io, color, img_as_ubyte
from skimage.feature import greycomatrix, greycoprops
from sklearn.metrics.cluster import entropy

rgbImg = io.imread('D:/PAPERS/With_Pratap_2019/figs/airplane_cipher.png')
grayImg = img_as_ubyte(color.rgb2gray(rgbImg))
#grayImg = Image.open('Documents/figs/barbara.jpg')


print (entropy(grayImg))
