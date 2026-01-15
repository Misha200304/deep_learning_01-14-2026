import torch

# 0D tensor (scalar)
t0 = torch.tensor(7)
print("t0:", t0)
print("shape:", t0.shape, "dimension:", t0.dim())
print()

# 1D tensor (vector)
t1 = torch.tensor([1, 2, 3, 4])
print("t1:", t1)
print("shape:", t1.shape, "dimension:", t1.dim())
print()

# 2D tensor – row vector (1 row, n columns)
row_vec = torch.tensor([[1, 2, 3]])
print("row_vec:", row_vec)
print("shape:", row_vec.shape, "dimension:", row_vec.dim())

# 2D tensor – column vector (n rows, 1 column)
col_vec = torch.tensor([[1],
                        [2],
                        [3]])
print("col_vec:", col_vec)
print("shape:", col_vec.shape, "dimension:", col_vec.dim())
