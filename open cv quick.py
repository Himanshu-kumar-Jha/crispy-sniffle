import cv2
import matplotlib.pyplot as plt
img=cv2.imread('myimg\golu.jpeg')
print("image shape: ",img.shape)
plt.imshow(img) #this will show image in BGR format
plt.show()
#####color conversion######
rgb_image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)
##plt.axis("off")
plt.show()

#####CROPING AN IMAGE##############
crop_image=rgb_image[0:700,0:650]                 ###rgb_image[col,rows,channels]
plt.imshow(crop_image)
plt.show()

####total pixels
total_pixels=crop_image.shape[0]*crop_image.shape[1]
print(total_pixels)

###resizing image and reducung pixles
crop_image=cv2.resize(crop_image,(100,100))
plt.imshow(crop_image)
plt.show()
