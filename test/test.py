import torch
import my_ops

a = torch.ones(3)
result = torch.ops.my_ops.ops1(a)
print("Result:", result)
