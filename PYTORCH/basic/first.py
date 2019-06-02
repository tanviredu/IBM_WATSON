## basic calculation
import torch

## matrix genaretion

matrix1 = torch.rand(5,3)
print (matrix1)

## another matric
matrix2 = torch.empty(5,3)
print (matrix2)

## ones matric

matrix3 = torch.ones(5,3)
print (matrix3)

## creating tensor

tensor1 = torch.tensor([5,6,7])
print (tensor1)
print (torch.Size(tensor1))

print (torch.add(matrix1,matrix2))

## only one item can be converter to scaler
tensor1 = torch.randn(1)
print (tensor1.item())

## convert numpy into the tensor
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
print (a)
print (b)



#### taking record of the calculation

x=torch.ones(2,2,requires_grad=True)
print (x)
x=x+2
print (x)

## the operation can be fetched
print (x.grad_fn)

print (x.grad)
