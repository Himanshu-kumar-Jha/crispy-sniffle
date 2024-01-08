import seaborn as sb 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
movies=pd.read_csv("imdb_top_1000.csv")
col_name=list(movies.get("Series_Title"))
movie_len={}
for i in col_name:
    x=len(i)
    try:
        movie_len[x]+=1
    except:
        movie_len[x]=1

print(movie_len)
####PLOTTING LEN VS OCCURENCE
X=np.array(list(movie_len.keys()))
Y=np.array(list(movie_len.values()))
plt.scatter(X,Y)
plt.xlabel('Movie length')
plt.ylabel('Number of movies')
plt.show()





