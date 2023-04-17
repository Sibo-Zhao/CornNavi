from temp_3_6 import navi_3_6
import pickle, csv, sys, time
import pandas as pd

start_time = time.time()
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

for i in range(5):
    way, poss = navi_3_6(size, data[0])
    for j in range(4):
        merged_list.append((data[i], way[j], poss[j]))

sorted_data = sorted(merged_list, key=lambda x: x[2], reverse=True)

p = [x[0] for x in sorted_data]
w = [x[1] for x in sorted_data]
l = [x[2] for x in sorted_data]

data = {'parents': p,
        'way': w,
        'likelihood': l}

df = pd.DataFrame(data)
df.to_csv('output.csv', index=False)

end_time = time.time()

with open('time.txt', 'w') as f:
    f.write(str(end_time - start_time))
