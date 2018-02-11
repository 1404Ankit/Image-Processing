#Import all the files that we installed

from PIL import Image

imageFile = "Scale.jpg"
im1 = Image.open(imageFile)
# adjust width and height to your needs
width = 500
height = 420
# use one of these filter options to resize the image
im2 = im1.resize((width, height), Image.NEAREST)      # use nearest neighbour
im3 = im1.resize((width, height), Image.BILINEAR)     # linear interpolation in a 2x2 environment
im4 = im1.resize((width, height), Image.BICUBIC)      # cubic spline interpolation in a 4x4 environment
im5 = im1.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
ext = ".jpg"
im2.save("Scale_Output/NEAREST" + ext)   #output image file where we want to save
im3.save("Scale_Output/BILINEAR" + ext)  #output image file where we want to save
im4.save("Scale_Output/BICUBIC" + ext)    #output image file where we want to save
im5.save("Scale_Output/ANTIALIAS" + ext)   #output image file where we want to save
