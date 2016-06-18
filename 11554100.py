# -*- coding: utf-8 -*-
"""
Created on Wed May 11 08:59:58 2016

@author: jessicaschonhut
"""

#PROGRAM TO CREATE SUBIMAGES OF ALL THE SCIENCE IMAGES, MINUS THE DARKS AND DIVIDE THEM BY FLATS. 
#THIS PROGRAM IS SPECIFICALLY FOR 11554100 ALTHOUGH ONLY FILE NAMES NEED CHANGING TO ADAPT TO OTHER STARS.
 
#Import necessary modules
from astropy.io import fits

#Creating subimage1, subimage2 and subimage3
#KIC 11554100 will now be called Berty - open all images of Berty
Berty1 = fits.open('N2.20160423.55047.fits')
Berty2 = fits.open('N2.20160423.55079.fits')
Berty3 = fits.open('N2.20160423.55111.fits')

#Get data from images of Berty
BertyA = Berty1[0].data
BertyB = Berty2[0].data
BertyC = Berty3[0].data

#Get dark image and data 
darkopen = fits.open('dark.fits')
dark = darkopen[0].data

#Cut the dark images down to the appropriate size for the science images they will be reducing.
dark1 = dark[512:1024, 0:512]
dark2 = dark[0:512, 512:1024]
dark3 = dark[512:1024, 512:1024] 

#SUBIMAGE1
#Berty 1 + half Berty 2 + half Berty 3
#(A - [1/2]B - [1/2]C)

subimage1 = (BertyA) - ((BertyB*0.5) + (BertyC*0.5))

#Cut down image 1 and dark subtract
subimage1 = subimage1[512:1024, 0:512]
subimage1 = subimage1-dark1

#SUBIMAGE2
#Berty 2 + half Berty 1 + half Berty 3
#(B - [1/2]A - [1/2]C)

subimage2 = (BertyB) - ((BertyC*0.5) + (BertyA*0.5))

#Cut down image 2 and dark subtract
subimage2 = subimage2[0:512, 512:1024]
subimage2 = subimage2-dark2

#SUBIMAGE3
#Berty 3 + half Berty 1 + half Berty 2
#(C - [1/2]A - [1/2]B)

subimage3 = (BertyC) - ((BertyA*0.5) + (BertyB*0.5))

#Cut down up image 1 and dark subtract
subimage3 = subimage3[512:1024, 512:1024] 
subimage3 = subimage3-dark3 

#Divide subimages by appropriate flat
#Open flat 
flatopen = fits.open('flat_final.fits')
flat = flatopen[0].data

#FLATSUBIMAGE1
#Cut down flat1
flat1 = flat[512:1024, 0:512]

#Create flatsubimage1
flatsubimage1 = subimage1 / flat1

#Saveflatsubimage1
hdul = fits.HDUList()
hdul.append(fits.PrimaryHDU(flatsubimage1))
hdul.writeto('flat_image_1.fits')

#FLATSUBIMAGE2
#Cut down flat2
flat2 = flat[0:512, 512:1024]

#Create flatsubimage2
flatsubimage2 = subimage2 / flat2 

#Saveflatsubimage2
hdul = fits.HDUList()
hdul.append(fits.PrimaryHDU(flatsubimage2))
hdul.writeto('flat_image_2.fits')

#FLATSUBIMAGE3
#Cut down flat3
flat3 = flat[512:1024, 512:1024]

#Create flatsubimage3
flatsubimage3 = subimage3 / flat3 

#Saveflatsubimage1
hdul = fits.HDUList()
hdul.append(fits.PrimaryHDU(flatsubimage3))
hdul.writeto('flat_image_3.fits')

