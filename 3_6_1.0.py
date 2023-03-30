from Function import inbred, hybrid, find_pure
from Constant import Gene


num = 1000
p1 = [1, 1, 0, 0, 0, 0]
p2 = [0, 1, 1, 1, 0, 0]
p3 = [0, 0, 0, 1, 1, 1]
parent_1 = Gene().add_gene(p1)
parent_2 = Gene().add_gene(p2)
parent_3 = Gene().add_gene(p3)

# 子一代
F_gene = Gene().add_gene(p1, p2)

# 子一代自交
F1_gene = inbred(num, F_gene)

# 子一代和另一个亲本回交获得子二代
F2_gene = hybrid(num, parent_3, F1_gene)


# 子二代自交
F3_gene = inbred(num, F2_gene)

# 计算概率
print(find_pure(num, F3_gene)/num * 100, end='')
print('%')
