#Import all the files that we installed

from PIL import Image

def changeImageSize(maxWidth, 
                    maxHeight, 
                    image):
    
    widthRatio  = maxWidth/image.size[0]
    heightRatio = maxHeight/image.size[1]

    newWidth    = int(widthRatio*image.size[0])
    newHeight   = int(heightRatio*image.size[1])

    newImage    = image.resize((newWidth, newHeight))
    return newImage

# Take two images    
image1 = Image.open("Composite_Output/base.jpg")
image2 = Image.open("Composite_Output/top.jpg")

# Make the sizes of images uniform
image3 = changeImageSize(800, 500, image1)
image4 = changeImageSize(800, 500, image2)

# Make sure the images have alpha channels
image3.putalpha(1)
image4.putalpha(1)

# Display the images
image3.show()
image4.show()

# Do an alpha composite of image4 over image3
alphaComposited = Image.alpha_composite(image3, image4)

# Display the alpha composited image
alphaComposited.show()