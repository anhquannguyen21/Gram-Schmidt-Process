import numpy as np


def normalize(vector):
    norm_vector=np.linalg.norm(vector)
    return vector/norm_vector


#A is matrix which columns are idependent.
def GramSchmidtProcess(A):
    n=A.shape[0]
    B=np.zeros((n,n))
    e_1=normalize(A[:,0])
    B[:,0]=e_1
    for i in range(1,n):
        temp=0
        for j in range(0,i):
            temp=temp+(np.inner(A[:,i],B[:,j]))*B[:,j]
        temp2=normalize(A[:,i]-temp)
        B[:,i]=temp2
    return B

x=np.array([[1,1,1],[0,1,1],[0,0,1]])
result=GramSchmidtProcess(np.transpose(x))
print(result)
