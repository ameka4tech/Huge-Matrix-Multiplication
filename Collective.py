""" 
************************************************************************************* **** 
                     MATRIX MULTIPLICATION USING MPI SCATTER AND GATHER 
                       DOT PRODUCT OF (1000X1000) USING 10 NODES 
************************************************************************************* **** 
""" 
 
import numpy as np                 #Importing Numpy Liabrary 
from scipy.linalg import det       #Scipy Liabrary for Determinant 
from mpi4py import MPI             #MPI Liabrary 
 
 
comm = MPI.COMM_WORLD              #Communication and Rank Instantiation rank = comm.Get_rank() size = comm.Get_size() 
 
 
A	= np.arange(0,10000,0.01).reshape((1000,1000)) #Generating 1000X1000 Matrix 
 
B	= A.T #Taking Transpose 
 
#Spliting A Matrix into 10 subdivisions 100*1000 matrix 
 
if rank == 0: 
   data = [ A[(i*100):((i+1)*100),:] for i in range(size)] 
else: 
   data = None 
 
data =comm.scatter(data, root=0) #Scattering The A matrix 
 
comm.Barrier()       #Initializing Barrier 
 
#data=comm.bcast(B,root=0)  #Broadcasting data = np.dot(data,B)    #Dot Product At Nodes 
 
ndata = comm.gather(data, root=0)   #Gathering the Computed Result at Master 
 
if rank == 0: 
    cndata = np.concatenate(ndata)        #Concatenation of Data     print "Determinant of A is ",det(A) 
    print "Determinant OF B is ",det(B)   #Determinants of A & B 
    # Dot Product 
    print "\nData on rank 0 is the dot product: \n\n\a  " ,cndata     print "Determinant is  ",det(cndata)  #Determinant else: 
    data = None 
 
#Code Ends 
