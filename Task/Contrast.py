#Import all the files that we installed

from PIL import Image
from PIL import ImageEnhance
 
im = Image.open("contrast.jpg") #input Image File

enh = ImageEnhance.Contrast(im)
img=enh.enhance(-0.5)
img.save('Contrast_Output/contrast1.jpg') #output image file where we want to save

img=enh.enhance(0.0)
img.save('Contrast_Output/contrast2.jpg') #output image file where we want to save

img=enh.enhance(0.5)
img.save('Contrast_Output/contrast3.jpg') #output image file where we want to save

img=enh.enhance(1.0)
img.save('Contrast_Output/contrast4.jpg') #output image file where we want to save

img=enh.enhance(1.7)
img.save('Contrast_Output/contrast5.jpg') #output image file where we want to save
