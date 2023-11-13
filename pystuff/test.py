import mylib
import torch
x = torch.ones(2, 2, device='cuda')
print(mylib.myfunc(x))
