from Function import inbred, hybrid, find_pure
from Constant import Gene


def navi_3_6(num, p):
    """
    3个亲本6对基因组的育种模版

    :param num:种群数量
    :param p:育种材料
    :return:育种路径和纯和子概率
    """
    poss = []
    way = []
    for i in range(1, 5):

        j = 5 - i
        like = 0
        for times in range(100):
            # 子一代
            f_gene = Gene().add_gene(p[0], p[1])

            # 子一代多次自交
            for x in range(i):
                f_gene = inbred(num, f_gene)

            # 子一代和另一个亲本i次回交

            f_gene = hybrid(num, Gene().add_gene(p[2]), f_gene)

            # 子二代j次自交
            for x in range(j):
                f_gene = inbred(num, f_gene)

            like += find_pure(num, f_gene)
        poss.append(round(like/num/100, 4))
        way.append('{n}次子一代自交和{m}次子二代自交'.format(n=i, m=j))

    return way, poss
