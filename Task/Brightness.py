#Import all the files that we installed

from PIL import Image
from PIL import ImageEnhance
 
im = Image.open("brightness.jpg") #inpute image file

enh = ImageEnhance.Brightness(im)
img=enh.enhance(0.0)
img.save('Brightness_Output/brightness1.jpg') #output image file where we want to save

img=enh.enhance(0.5)
img.save('Brightness_Output/brightness2.jpg') #output image file where we want to save

img=enh.enhance(1.0)
img.save('Brightness_Output/brightness3.jpg') #output image file where we want to save

img=enh.enhance(1.5)
img.save('Brightness_Output/brightness4.jpg') #output image file where we want to save

img=enh.enhance(2.0)
img.save('Brightness_Output/brightness5.jpg') #output image file where we want to save
