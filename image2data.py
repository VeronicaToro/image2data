# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:15:21 2019

@author: Verónica Toro Betancur

Class to calculate data from image.
"""
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt


# Function taken from stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

class i2d:
    
    def __init__(self, f):
        self.file = f
        self.x = []
        self.y = []
    
    def process(self):
        _img = misc.imread(self.file)
        grayimg = rgb2gray(_img)
        grayhist, graybins = np.histogram(grayimg.ravel(),256,[0,256])
        
        maxi = np.argmax(grayhist[:-15])
        interval = 5
        m = np.size(grayimg, axis=0)    # Number of rows
        n = np.size(grayimg, axis=1)    # Number of columns
        for col in range(n):
            pixel = [[],[],[]]
            for row in range(m):
                if (grayimg[row][col] >= maxi-interval and grayimg[row][col] <= maxi+interval):
                    pixel[0].extend([grayimg[row][col]])    # Color of pixel
                    pixel[1].extend([col])  # x coordinate
                    pixel[2].extend([row])  # y coordinate
            if pixel[0]:
                idx = np.argmax(pixel[0])       # We keep the pixel with the highest color
                self.x.extend([pixel[1][idx]])
                self.y.extend([pixel[2][idx]])
        max_y = max(self.y)
        self.y = [-1*element + max_y for element in self.y]
        return self.x, self.y
        
    def plot(self):
        plt.plot(self.x,self.y,'.')
        plt.show()
        