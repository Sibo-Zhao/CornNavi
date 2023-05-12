import pickle
import itertools

my_list = list(itertools.product([0, 1], repeat=6))
my_list = [list(elem) for elem in my_list]
my_list = [l for l in my_list if 5 > l.count(1) > 1]  # 删去0 1 5 6个1的  -->  50个

combinations = itertools.combinations(my_list, 2)  # 生成无序二元组  -->  49 * 50 / 2 = 1250个

triplets = []

for combination in combinations:
    for item in my_list:
        if item not in combination:
            triplets.append((*combination, item))  # 前两个无序，最后一个有序 -->  1250 * 48 = 58800个


combinations = []
for combo in triplets:
    if all(any(c[i] == 1 for c in combo) for i in range(6)):  # 3组的对应位置上都要至少有一个1  -->  24585个
        combinations.append(combo)


CHUNKSIZE = 5000

with open('gene.pickle', 'wb') as f:
    chunks = [combinations[i:i+CHUNKSIZE] for i in range(0, len(combinations), CHUNKSIZE)]
    for chunk in chunks:
        pickle.dump(chunk, f, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(None, f)  # 添加最后一个 STOP 标记


print("pickle 文件已成功写入！")
