""" 
*********************************************************************** 
            MATRIX MULTIPLICATION USING MPI SEND AND RECEIVE 
               DOT PRODUCT OF (1000X1000) USING 10 NODES 
 
*********************************************************************** 
""" 
 
import numpy as np                #Importing Numpy Liabrary 
from scipy.linalg import det      #Scipy Liabrary for Determinant 
from mpi4py import MPI            #MPI Liabrary 
 
comm = MPI.COMM_WORLD             #Communication and Rank Instantiation rank = comm.Get_rank() 
 
 
A	= np.arange(0,10000,0.01).reshape((1000,1000)) #Generating 1000X1000 Matrix 
 
B	= A.T                 #Taking Transpose 
 
 
#Dividing 1000X1000 Matrices in 10 Matrix 
 
A0 = A[ 0:100,:] 
A1 = A[ 100:200,:] 
A2 = A[ 200:300,:] 
A3 = A[ 300:400,:] 
A4 = A[ 400:500,:] 
A5 = A[ 500:600,:] 
A6 = A[ 600:700,:] 
A7 = A[ 700:800,:] 
A8 = A[ 800:900,:] 
A9 = A[ 900:1000,:] 
#Conditioning The Loop for Masters and Nodes 
 
if rank == 0: 
 
#Sending the Broken Matrices to 10 Nodes 
 
    comm.send(A1, dest=1, tag=11)     comm.send(A2, dest=2, tag=11)     comm.send(A3, dest=3, tag=11)     comm.send(A4, dest=4, tag=11)     comm.send(A5, dest=5, tag=11)     comm.send(A6, dest=6, tag=11)     comm.send(A7, dest=7, tag=11)     comm.send(A8, dest=8, tag=11)     comm.send(A9, dest=9, tag=11) 
 
#Sending B Matrix Nodes to Compute the Dot Product     comm.send(B, dest=1, tag=13)     comm.send(B, dest=2, tag=13)     comm.send(B, dest=3, tag=13)     comm.send(B, dest=4, tag=13)     comm.send(B, dest=5, tag=13)     comm.send(B, dest=6, tag=13)     comm.send(B, dest=7, tag=13)     comm.send(B, dest=8, tag=13)     comm.send(B, dest=9, tag=13) 
 
#Defining the Reception Matrices of Size 100x1000 
C1 = {} 
    C2 = {} 
    C3 = {} 
    C4 = {} 
    C5 = {} 
    C6 = {} 
    C7 = {} 
    C8 = {} 
    C9 = {} 
    C0 = {} 
 
#Dot Product at Master Node 
 
    C0  = np.dot(A0,B) 
 
#Receiving From Nodes 
 
    C1 = comm.recv(source=1, tag=15) 
    C2 = comm.recv(source=2, tag=15) 
    C3 = comm.recv(source=3, tag=15) 
    C4 = comm.recv(source=4, tag=15) 
    C5 = comm.recv(source=5, tag=15) 
    C6 = comm.recv(source=6, tag=15) 
    C7 = comm.recv(source=7, tag=15) 
    C8 = comm.recv(source=8, tag=15)     C9 = comm.recv(source=9, tag=15) 
 
#Concatenating The Received Matrices 
 
    C = np.concatenate([C0,C1,C2,C3,C4,C5,C6,C7,C8,C9]) print C.shape 
    print "The dot product of part 1 is:",C  #Dot Product of A nd B transpose 
 
#Computation of Determinant 
 
    print "The Determinant of A is: " ,det(A)     print "The Determinant of B is: " ,det(B)     Det = det(C) 
    print "The Overall Determinant is: " ,Det 
 
#Rank Reception Loop 
 
elif rank == 1: 
     A1 = comm.recv(source=0,tag=11)  #Reception of 100*1000 Matrix 
     B  = comm.recv(source=0,tag=13)  #Reception of B 1000*1000 Matrix      C1 = np.dot(A1,B)                #Computation of Dot Product      comm.send(C1, dest=0, tag=15)    #Sending the Computed Product to Master elif rank == 2: 
     A2 = comm.recv(source=0,tag=11) 
     B  = comm.recv(source=0,tag=13)      C2 = np.dot(A2,B)      comm.send(C2, dest=0, tag=15) 
 
elif rank == 3: 
     A3 = comm.recv(source=0,tag=11) 
     B  = comm.recv(source=0,tag=13)      C3 = np.dot(A3,B)      comm.send(C3, dest=0, tag=15) 
 
elif rank == 4: 
A4 = comm.recv(source=0,tag=11) 
     B  = comm.recv(source=0,tag=13)      C4 = np.dot(A4,B)      comm.send(C4, dest=0, tag=15) 
 
elif rank == 5: 
     A5 = comm.recv(source=0,tag=11) 
     B  = comm.recv(source=0,tag=13)      C5 = np.dot(A5,B)      comm.send(C5, dest=0, tag=15) 
 
elif rank == 6: 
     A6 = comm.recv(source=0,tag=11) 
     B  = comm.recv(source=0,tag=13)      C6 = np.dot(A6,B)      comm.send(C6, dest=0, tag=15) elif rank == 7: 
     A7 = comm.recv(source=0,tag=11) 
     B  = comm.recv(source=0,tag=13)      C7 = np.dot(A7,B)      comm.send(C7, dest=0, tag=15) 
 
elif rank == 8: 
     A8 = comm.recv(source=0,tag=11) 
     B  = comm.recv(source=0,tag=13)      C8 = np.dot(A8,B)      comm.send(C8, dest=0, tag=15) 
 
else : 
     A9 = comm.recv(source=0,tag=11) 
     B  = comm.recv(source=0,tag=13)      C9 = np.dot(A9,B)      comm.send(C9, dest=0, tag=15) 
 
#Code Ends 
