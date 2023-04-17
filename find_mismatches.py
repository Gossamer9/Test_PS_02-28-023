import pandas as pd

repeats = pd.read_csv("ZHWCBC5W013-HitTable.csv", header=None)
similar=repeats[repeats[2]==100.00].reset_index(drop=True)
loc=similar[0][0]

for i in range(len(similar[0])-1):
    if similar[0][i+1] != loc:
        loc = similar[0][i+1]
    else:
        if similar[0][i-1] != loc:
            print(loc, similar[1][i],end = " ")
        print(similar[1][i+1], end = " ")
        if similar[0][i+2] != loc:
            print()
