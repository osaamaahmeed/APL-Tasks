import torch

tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])

dot_prod = torch.dot(tensor1, tensor2)

elem_mul = tensor1 * tensor2

print(f"Dot Product: {dot_prod}")
print(f"Element-wise Multiplication: {elem_mul}")