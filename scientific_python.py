# Source code for Assignment #3
# Name: YOUR NAME HERE!!!!
#
# Required function definitions:
#
#    Problem #1: 
#        Function: LinearLS(x,y)
#        Input: Two 1D numpy.arrays of length N
#        Output: 1D numpy.array of length two [b, m])
#
#    Problem #2: 
#        Function: Problem2(N)
#        Input: Size of the linear system N (integer)
#        Output: 1D numpy.array of length N
#
def LinearLS(x, y):
    import numpy as np
    #N, = x.shape
    N = x.size
    M =array([ones(N), x)
    Mt = M.T
    A = np.dot(Mt, M)
    b = np.dot(Mt, y)
    z = np.linalg.solve(A, b)
    return z.T
    
   
def SolveFDM(N):
    import numpy as np
    import scipy.linalg as sci
    L = np.array([-np.ones(N), 2*np.ones(N), -np.ones(N)])
    b = (-2/((N+1)**2))*np.ones(N)
    x = sci.solve_banded((1, 1), L, b)      
    return x
    
