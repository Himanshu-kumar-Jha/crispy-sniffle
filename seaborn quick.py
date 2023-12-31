import matplotlib.pyplot as plt 
import numpy as np 
x=np.array([1,2,3,4,5])
y=x**2+3
y1=x**2
print(x,y)
print(plt.style.available)
plt.style.use("dark_background")
###########FOR PLOTTING A LINE############################
plt.plot(x,y,label="stock price")
plt.plot(x,y1,label="only fans subscription")
plt.legend()
plt.title("My line plot")
print(plt.show())
################FOR PLOTTING AS DOTS#######################
plt.style.use("dark_background")
plt.scatter(x,y,label="stock price")
plt.scatter(x,y1,label="only fans subscription")
plt.legend()
plt.title("My line plot")
print(plt.show())