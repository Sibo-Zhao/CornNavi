from Function import inbred, hybrid, find_pure
from Constant import Gene


num = 1000  # 种群个数
p = []
p1 = [1, 1, 0, 0, 0, 0]
p2 = [0, 1, 1, 1, 0, 0]
p3 = [0, 0, 0, 1, 1, 1]
p.append(p1)
p.append(p2)
p.append(p3)
parent = [Gene().add_gene(p1), Gene().add_gene(p2), Gene().add_gene(p3)]
for i in range(3):
    res = 0
    for j in range(20):
        # 子一代
        F_gene = Gene().add_gene(p[i % 3], p[(i+1) % 3])

        # 子一代自交
        F1_gene = inbred(num, F_gene)

        # 子一代和另一个亲本回交获得子二代
        F2_gene = hybrid(num, parent[(i+2) % 3], F1_gene)

        # 子二代自交
        F3_gene = inbred(num, F2_gene)

        # 计算概率
        # print(find_pure(num, F3_gene)/num * 100, end='%')
        res += find_pure(num, F3_gene)
        print(find_pure(num, F3_gene), end=' ')
    print('\n', res, sep='')
