#Import all the files that we installed

import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt


img = plt.imread('blur.png') #input image
plt.figure()
plt.imshow(img)


t = np.linspace(-10, 10, 30)
bump = np.exp(-0.1*t**2)
bump /= np.trapz(bump) 

kernel = bump[:, np.newaxis] * bump[np.newaxis, :]

kernel_ft = fftpack.fft2(kernel, shape=img.shape[:2], axes=(0, 1))


img_ft = fftpack.fft2(img, axes=(0, 1))

img2_ft = kernel_ft[:, :, np.newaxis] * img_ft
img2 = fftpack.ifft2(img2_ft, axes=(0, 1)).real


img2 = np.clip(img2, 0, 1)


plt.figure()
plt.imshow(img2)


from scipy import signal

img3 = signal.fftconvolve(img, kernel[:, :, np.newaxis], mode='same')
plt.figure()
plt.imshow(img3)

plt.show()

