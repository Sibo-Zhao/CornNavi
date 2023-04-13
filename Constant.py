import random


class Gene:
    def __init__(self):
        self.genes = []
        self.num_genes = 0

    def add_gene(self, allele_1, allele_2=None):
        if allele_2 is None:
            for i in range(len(allele_1)):
                self.genes.append({'x': allele_1[i], 'y': allele_1[i]})
                self.num_genes += 1
            return self
        elif isinstance(allele_2, list):
            for i in range(len(allele_1)):
                self.genes.append({'x': allele_1[i], 'y': allele_2[i]})
                self.num_genes += 1
            return self
        else:
            self.genes.append({'x': allele_1, 'y': allele_2})
            self.num_genes += 1

    def get_gene(self, gene_num, allele):
        if gene_num < self.num_genes:
            return self.genes[gene_num][allele]
        else:
            print(f"{gene_num} not found in genes.")

    def division(self, gene_num):
        return random.choice([self.genes[gene_num]['x'], self.genes[gene_num]['y']])
