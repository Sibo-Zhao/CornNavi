from temp_3_6 import navi_3_6
import pickle, csv, sys, time


start_time = time.perf_counter()
data = []
size = 500
with open('ignore/gene.pickle', 'rb') as f:
    while True:
        try:
            chunk = pickle.load(f)
            if chunk is None:
                break
            data.extend(chunk)
        except EOFError:
            print(sys.exc_info())
            break


merged_list = []

for i in range(10):
    way, poss = navi_3_6(size, data[0])
    for j in range(4):
        merged_list.append((data[i], way[j], poss[j]))

sorted_data = sorted(merged_list, key=lambda x: x[2], reverse=True)


# 将三元组写入到文件中
with open('ignore/test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['parents', 'way', 'likely_hood'])  # 写入列名
    for i in range(len(sorted_data)):
        writer.writerow(sorted_data[i])  # 写入三元组数据


end_time = time.perf_counter()
total_time = end_time - start_time
print("程序运行时间为：", total_time, "秒")
