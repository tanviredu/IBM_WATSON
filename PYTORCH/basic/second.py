import torch
a = torch.randn(2,2)
a=((a*3)/(a-1))
print (a.requires_grad)
a.requires_grad_(True)
print(a.requires_grad)
b = (a*a).sum()
print (b)
print(b.grad_fn)
print (b.grad)
b=torch.rand(1)
b.backward
print(b.grad)

