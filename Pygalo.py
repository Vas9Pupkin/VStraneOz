import cv2
import numpy as np
import copy
import math
def max_functin(a, b, img):
    img0 = copy.copy(img)
    for i in range(0, img.shape[0]):
        for j in range(2, img.shape[1]):
            for k in range(img.shape[2]):
                temp = original(i, j, k, a, b, img0)
                img[i, j, k] = np.max(temp)
    return img
def original (i, j, k,a, b,img):
    x1, x2 = spilt(a)
    y1, y2 = spilt(b)
    temp = np.zeros(a * b)
    count = 0
    for m in range(x1, x2):
        for n in range(y1, y2):
            if i + m < 0 or i + m > img.shape[0] - 1 or j + n < 0 or j + n > img.shape[1] - 1:
                temp[count] = img[i, j, k]
            else:
                temp[count] = img[i + m, j + n, k]
            count += 1
    return  temp
def spilt( a ):
    if a/2 == 0:
        x1 = x2 = a/2
    else:
        x1 = math.floor( a/2 )
        x2 = a - x1
    return -x1,x2
def min_functin(a, b, img):
    img0 = copy.copy(img)
    for i in range(0, img.shape[0]):
        for j in range(2, img.shape[1]):
            for k in range(img.shape[2]):
                temp = original(i, j, k, a, b, img0)
                img[i, j, k] = np.min(temp)
    return img

def VdolbNochnixDorog(input_img):
    c=copy.copy(input_img)
    d = copy.copy(input_img)
    print('s')
    for i in range (input_img.shape[0]):
        if i==1000:
            print('1000')
        if i==2000:
            print('1000')
        if i==3000:
            print('1000')
        if i==4000:
            print('1000')
        if i==5000:
            print('1000')
        if i==6000:
            print('1000')
        if i==7000:
            print('1000')
        for j in range (input_img.shape[1]):
            a=np.array([])
            try:
                a=np.append(a, input_img[i+1][j][1])
            except:
                pass
            try:
                a=np.append(a, input_img[i+1][j+1][1])
            except:
                pass
            try:
                a=np.append(a, input_img[i][j+1][1])
            except:
                pass
            try:
                a=np.append(a, input_img[i+1][j-1][1])
            except:
                pass
            try:
                a=np.append(a, input_img[i][j-1][1])
            except:
                pass
            try:
                a=np.append(a, input_img[i-1][j-1][1])
            except:
                pass
            try:
                a=np.append(a, input_img[i-1][j][1])
            except:
                pass
            try:
                a=np.append(a, input_img[i-1][j+1][1])
            except:
                pass
            a=np.append(a, input_img[i][j][1])
            c[i][j]=max(a)
            d[i][j]=min(a)

    return c,d
