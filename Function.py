from Constant import Gene


target = [1, 1, 1, 1, 1, 1]


# 自交
def inbred(size, parent):
    f_gene = []
    if isinstance(parent, Gene):
        for i in range(size):
            f = Gene()
            for j in range(6):
                xgene = parent.division(j)
                ygene = parent.division(j)
                f.add_gene(xgene, ygene)
            f_gene.append(f)
    else:
        for i in range(size):
            f = Gene()
            for j in range(6):
                xgene = parent[i].division(j)
                ygene = parent[i].division(j)
                f.add_gene(xgene, ygene)
            f_gene.append(f)
    return f_gene


# 杂交
def hybrid(size, mum: Gene, dad: [Gene]):
    f_gene = []
    for i in range(size):
        f = Gene()
        for j in range(6):
            xgene = dad[i].division(j)
            ygene = mum.division(j)
            f.add_gene(xgene, ygene)
        f_gene.append(f)
    return f_gene


# 展示
def dayin(gene, num=None):
    x = []
    y = []
    if num is None:
        for i in range(6):
            x.append(gene.get_gene(i, 'x'))
            y.append(gene.get_gene(i, 'y'))
        print(x, y)
    else:
        for i in range(6):
            x.append(gene[num].get_gene(i, 'x'))
            y.append(gene[num].get_gene(i, 'y'))
        print(x, y)


#

# 找到纯和
def find_pure(size, gene):
    res = 0
    for i in range(size):
        x = []
        y = []
        for j in range(6):
            x.append(gene[i].get_gene(j, 'x'))
            y.append(gene[i].get_gene(j, 'y'))
        print(x, y)
        if x == target and y == target:
            res += 1
    return res
