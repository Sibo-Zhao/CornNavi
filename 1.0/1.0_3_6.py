import matplotlib.pyplot as plt
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

for i in range(1, 5):
    plt.figure(i)
    line = []
    row = []
    j = 5 - i

    for times in range(1, 21):
        # 子一代
        F_gene = Gene().add_gene(p[0], p[1])

        # 子一代i次自交
        for x in range(i):
            F_gene = inbred(num, F_gene)

        # 子一代和另一个亲本回交
        F_gene = hybrid(num, parent[2], F_gene)

        # 子二代j次自交
        for x in range(j):
            F_gene = inbred(num, F_gene)

        row.append(times)
        line.append(find_pure(num, F_gene))

    print(line)
    plt.plot(row, line)
    name = '{n}{m}回交和子二代自交1_2.jpg'.format(n=i, m=j)
    plt.savefig(name, format='jpg', dpi=300)

# plt.savefig('折_回交和子二代自交2_3.jpg', format='jpg', dpi=300)



