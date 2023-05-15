from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import random
import os

import tkinter
import matplotlib
matplotlib.use('TkAgg')
# import cv2
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

### For visualizing the outputs ###
import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
#%matplotlib inline

dataDir='../imgs/test2017'

dataType='val'
# annFile='{}/annotations/stuff_{}2017.json'.format(dataDir,dataType)

annFile = '../image_info_test2017/annotations/image_info_test2017.json'

# Initialize the COCO api for instance annotations
coco=COCO(annFile)

# Load the categories in a variable
catIDs = coco.getCatIds()
cats = coco.loadCats(catIDs)

print(cats)


def getClassName(classID, cats):
    for i in range(len(cats)):
        if cats[i]['id']==classID:
            return cats[i]['name']
    return "None"

print('The class name is', getClassName(77, cats))


filterClasses = ['laptop', 'tv', 'cell phone']

# Fetch class IDs only corresponding to the filterClasses
catIds = coco.getCatIds(catNms=filterClasses) 
# Get all images containing the above Category IDs
imgIds = coco.getImgIds(catIds=catIds)

# did not work, figure out later ^^^
imgIds = coco.getImgIds()

# load and display a random image
img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
I = io.imread('{}/{}'.format(dataDir,img['file_name']))/255.0

plt.axis('off')
plt.imshow(I)
plt.show()