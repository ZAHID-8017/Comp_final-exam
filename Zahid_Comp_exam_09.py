import numpy as np

def Singular_val(X,J , dtype = int):
    X_T = np.transpose(X)
    D = np.matmul(X_T,X)
    eigenvalues = np.linalg.eigvals(D)

    S=[]
    m=0
    for i in (eigenvalues):
      
        if (i!=0):
            S.append(np.sqrt(i))
            m = m+1
            print("Singular vlaues of matrix",J,"=", round(S[m-1],8))
    return "Task completed for the above matrix"

A = np.array([[2,1],[1,0],[0,1]])

B = np.array([[1,1,0],[1,0,1],[0,1,1]])

H1 = Singular_val(A,1)
print(H1)


H2 = Singular_val(B,2)
print(H2)


X_T = np.transpose(A)
print(X_T)
D = np.matmul(X_T,A)
print(D)
eigenvalues = np.linalg.eigvals(D)
print(eigenvalues)
########################################
print("Results obtaind by Numpy")


U,S,V = np.linalg.svd(A)
print(S)
###########################
U1,S1,V1 = np.linalg.svd(B)
print(S1)





