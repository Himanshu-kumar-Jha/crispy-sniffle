import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.datasets import fetch_openml
df= fetch_openml('mnist_784' , as_frame=False)
data=df.values
X,Y=df['data'],df['target']
Y=data[ : ,0]
#8*8 image
# A draw function to explain how image is drawn from a 1d array
'''
def drawimg(X,Y,i):
    plt.imshow(X[i].reshape(8,8),cmap='gray')
    plt.title(Y[i])
    plt.show()
drawimg(X,Y,5)
'''
#############
from sklearn.model_selection import train_test_split
XT,Xt,YT,Yt=train_test_split(X,Y,test_size=0.3,random_state=5)
print(XT.shape,YT.shape)
print(Yt.shape,Yt.shape)
# Plotting a grid of 25 images
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.imshow(XT[i].reshape(28,28), cmap=matplotlib.cm.binary,interpolation="nearest")  # Corrected indexing here
    plt.title(YT[i])  # Convert the label to string
    plt.axis("off")

plt.show()

