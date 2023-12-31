import pandas as pd 
import numpy as np
India ={
    "health index":np.random.randint(50,100,5),
    "growth rate":np.random.randint(10,50,5),
    "infrastructue":np.random.randint(40,80,5)
}
print(India)
Excel_Table=pd.DataFrame(India)
Excel_Table.head() # for better visual
print(Excel_Table)
print(Excel_Table.columns)# to see columns name

#########creating a CSV(comma seperated file) file#############
Excel_Table.to_csv("INDIA CSV")
##############How TO READ A CSV FILE#################
csv_file=pd.read_csv("INDIA CSV")
csv_file.drop(columns=['Unnamed: 0'])
csv_file.head()
print(csv_file)
print(csv_file.shape)

