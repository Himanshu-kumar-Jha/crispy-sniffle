#########PLAYING  WITH SEABORN############

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

tips_data=sns.load_dataset('tips')
#sns.barplot(x='which coll you want on x axis',y='call you want on y axis',
#data=data set you want to retrive data from) y axis has mean
sns.barplot(x='sex',y='tip',data=tips_data)
plt.show()

#WHAT IF I WANT TO PLOT? SD, OR MEDIAN ON Y AXIS?
#for that we use an additional parameter called the estimator function
sns.barplot(x='sex',y='tip',data=tips_data,estimator=np.std) #std for standard deviation
plt.show()

####COUNT PLOT#### it gives count of varibales on x axis, 
# if you don't give x ,you give y plot will be rotated by 90deg right
#if you give both x and y it will throw an eroor
sns.countplot(x='day',hue='sex',data=tips_data)
plt.show()

#####BOX AND WHISKERS  PLOT######
sns.boxplot(x='sex',y='tip',hue='day',data=tips_data)
plt.show()

##VOLION PLOT
sns.violinplot(x="day",y="tip",hue="sex",data=tips_data)
plt.show()

##DISTRIBUTION PLOT
sns.distplot(tips_data["tip"],kde=True) #kde can be turned off and on
plt.show()

##KDE PLOT
sns.kdeplot(tips_data["tip"])
plt.show()

##JOINT PLOT
sns.jointplot(x="total_bill",y="tip",data=tips_data,kind='hex')#kind can be hex,reg,kde
plt.show()

##PAIR PLOT
sns.pairplot(tips_data,hue="sex")
plt.show()

##HEAT MAPS
flights=sns.load_dataset('flights')
flights_pivot=flights.pivot_table(index="month",columns="year",values="passengers")
sns.heatmap(flights_pivot)
plt.show()








