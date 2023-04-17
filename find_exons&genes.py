import pandas as pd
import re
import copy

uniq_genes = {} #Словарь с уникальными генами
panel = pd.read_csv("annotation_panel.bed", '\s+', header=None)
ID_ = pd.Series(panel[8].values)
ID_cut = copy.deepcopy(ID_)
f = open('genes&exons.txt', 'w')

for i,j in enumerate(ID_cut):
    ID_cut[i]=re.split(';|:',j)[0]
    if ID_cut[i][3]=="E":
        key=ID_[i][ID_[i].index('gene_name=')+10:].split(';')[0]
        uniq_genes.setdefault(key, [])
lst=ID_cut[ID_cut=="ID=exon"].index #Номера строк, в которых содержится информация о экзонах

for j,i in enumerate(lst):
    key=ID_[i][ID_[i].index('gene_name=')+10:].split(';')[0]
    value=ID_[i][ID_[i].index('exon_number=')+12:].split(';')[0]
    uniq_genes.setdefault(key, []).append(value)

for i in uniq_genes:
    rslt=uniq_genes[i]
    s=set(rslt)
    rslt=list(s)
    rslt=list(map(int, rslt))
    str=f'Ген {i}, экзон(ы) {sorted(rslt)}'
    f.write(str + '\n')

