#coding:utf-8
import numpy as np

def pnsr(im1,im2):
    im1=im1.astype('float')
    im2=im2.astype('float')
    diff = np.abs(im1 - im2)
    m=im1.shape[0]
    n=im1.shape[1]
    mse = (im1-im2)**2
    mse=np.mean(mse)
    psnr = 10*np.log10(1/mse)
    return psnr


