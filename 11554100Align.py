# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:54:02 2016

@author: jessicaschonhut
"""

#PROGRAM TO ALIGN FLATSUBIMAGES INTO FINAL SCIENCE IMAGE.
#Aligning and combining images for 11554100

#Import appropriate modules
from astropy.io import fits
import numpy as np

#Open subimages which have been flatfielded and dark subtracted - These will be called Sally
Sally1 = fits.open('flat_image_1.fits')
Sally2 = fits.open('flat_image_2.fits')
Sally3 = fits.open('flat_image_3.fits')

#Get data from these files 
SallyA = Sally1[0].data
SallyB = Sally2[0].data
SallyC = Sally3[0].data

#Align the images over the top of one another
StillImage = SallyA 
MoveImage1 = np.zeros([512, 512])
SallyB = MoveImage1[3:, 6:]
MoveImage2 = np.zeros([512, 512])
SallyC = MoveImage2[1:, 11:]

#Stack the aligned images
FinalImage = StillImage + MoveImage1 + MoveImage2

#Save the final image
hdul = fits.HDUList()
hdul.append(fits.PrimaryHDU(FinalImage))
hdul.writeto('final_image.fits')