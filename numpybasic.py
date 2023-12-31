import numpy as np #importing numpy as np for easy use
a=np.array([1,2,3,4,5]) #to declare a 1d array
print(a)
b=np.array([[1,2,3,4,5],[7,6,5,4,3]]) # to declare 2d array
print(a.shape) #size of matrix
print(b.shape) #size of matrix
print(np.dot(b,b.T)) #dot product of two matrixes  and transpose of matrix can be done by b.T
print(np.random.randint(60,100,10)) #this prints random integers in form of matrix (start , end (exc),how many numbers)
matrix=np.random.randint(60,100,(5,5)) # same but in a 2d matrix of given size
print(matrix)
print(np.min(matrix)) #returns min ele in a matrix
print(np.max(matrix)) # returns max elemet in 2d matrix
print(np.argmin(matrix)) #posistion of min element 
print(np.argmax(matrix))#position of maximum element
print(np.unique(matrix)) #returns an array of unique elements in matrix
print(np.unique(matrix,return_counts=True)) #returns 2 arrays with unique elements and their frequencies

x=np.unique(matrix,return_counts=True)
print(x[0]) #this gives the unique elemets in matrix 
print(x[1]) #thi gives it frequencies

# a program to find a number with highest frequency in matrix
mat_x=np.random.randint(70,100,10) #creating random nubers in matrix
p=np.unique(mat_x,return_counts=True)#storing two arrays one for unique elements and their frequencies 
idx=np.argmax(p[1])  #finding index of maximum elemnet in p[1] freq array
ele=p[0][idx]# storing max freq elemnet from number array taking position from freq array
print(ele)
##################

#slicing a matrix (matrix at line no 9)
print(matrix[2:4,1:2])
#   matrix[[s,e),col[s,e)]


