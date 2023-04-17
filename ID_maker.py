import pandas as pd

panel = pd.read_csv("convert_panel.bed", '\s+', header=None)
annotation = pd.read_csv("annotation_panel.bed", '\s+', header=None)
result = pd.read_csv("IAD143293_241_Designed.bed", '\s+', header=None)
for k in range(len(panel)):
    start=panel[1][k]+1
    end=panel[2][k] #a=annotation[3]    b=annotation[4]
#    l1=((annotation[3]>=start) & (annotation[4]<=end)) нахождение экзона внутри последовательности
#    l2=((annotation[3]<=start) & (annotation[4]>= end)) нахождение последовательности внутри экзона
#    l3=((annotation[4]>start) & (annotation[3]<=start)) частичное вхождение экзона слева
#    l4=((annotation[3]<end) & (annotation[4]>=end)) частичное вхождение экзона справа
    df=annotation[((annotation[3]>=start) & (annotation[4]<=end))|((annotation[3]<=start) & (annotation[4]>= end))|((annotation[4]>start) & (annotation[3]<=start))|((annotation[3]<end) & (annotation[4]>=end))].reset_index(drop=True)
#    print(df)
    a=-1
    s=set()
    for i in range(len(df)):
        j=0
        s=set()
        if (df[2][i]=='gene') & (j==0):
            a=df[8][i][df[8][i].index('gene_name=')+10:].split(';')[0]
            j=1
        elif df[2][i]=='exon':
            s.add(df[8][i][df[8][i].index('exon_number=')+12:].split(';')[0])
    if s==set():
        s='no_exons'
    else:
        s=f"{list(s)[0]}"
    if a==-1:
        a='gene_not_found'
    result.at[k,"Gene"]=a
    result.at[k,"Exon"]=s
result.to_csv("IAD143293_241_Designed_with_IDs.bed",sep='\t', index=False, header=False, encoding='utf-8')
