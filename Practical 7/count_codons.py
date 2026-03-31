import re
import matplotlib.pyplot as plt
in_file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
stop_codons=['TAA','TAG','TGA']
selected_stop=input("Enter one stop codon (TAA, TAG or TGA): ")
header=''
sequence=''
codon_counts={}     #建立一个空字典，用来统计每个codon出现了多少次
gene_total=0
for line in in_file:
    line=line.rstrip()
    if re.findall(r'^>',line):
        if header!='':
            longest_orf=''      #建立一个空字符串，用来保存在这个基因里，以用户指定stop codon结束的最长ORF
            for i in range(len(sequence)-2):
                part=sequence[i:]
                codons=re.findall(r'[ATGC]{3}',part)
                if codons and codons[0]=='ATG':
                    current_orf=''         #建立一个空字符串，储存现在的
                    for codon in codons:      #一个一个读codon
                        current_orf=current_orf+codon        #读一个就加入一个到current
                        if codon in stop_codons:    #说明这个ORF到这里结束了
                            if codon==selected_stop:
                                if len(current_orf)>len(longest_orf):
                                    longest_orf=current_orf
                                    break
            if longest_orf!='':      #如果确实找到了以用户输入结束的ORF，继续统计（如果还是空字符串说明还没有找到）
                for i in range(0,len(longest_orf)-3,3):    #表示从第0个位置开始，到最后三个字符前停下，每次跳3个位置。意思是把longest_orf从头开始，每次按3个碱基去一个codon，但是不取最后的stop codon->符合题目条件要specified stop codon 上游的 in-frame codons
                    codon=longest_orf[i:i+3]       #取出当前位置的3个碱基组成的codon
                    if codon in codon_counts:         #如果codon已经在字典里了，就下一行（现在还在存储到字典里面的过程）
                        codon_counts[codon]=codon_counts[codon]+1      #把这个codon的计数+1
                    else:        #如果之前还没有出现过
                        codon_counts[codon]=1      #记入字典，计数为1
        header=line
        sequence=''
    else:
        sequence+=line
#处理最后一个基因
if header!='':      
    longest_orf=''
    for i in range(len(sequence)-2):
                part=sequence[i:]
                codons=re.findall(r'[ATGC]{3}',part)
                if codons and codons[0]=='ATG':
                    current_orf=''         
                    for codon in codons:      
                        current_orf=current_orf+codon        
                        if codon in stop_codons:    
                            if codon==selected_stop:
                                if len(current_orf)>len(longest_orf):
                                    longest_orf=current_orf
                                    break
    if longest_orf!='':      
                gene_total+=1
                for i in range(0,len(longest_orf)-3,3):    
                    codon=longest_orf[i:i+3]       
                    if codon in codon_counts:         
                        codon_counts[codon]=codon_counts[codon]+1      
                    else:        
                        codon_counts[codon]=1      
in_file.close()
print(f'Selected stop codon: {selected_stop}')
print("Counts of upstream in-frame codons:")
for codon in codon_counts:     #分别遍历每一个密码子
    print(f"{codon}: {codon_counts[codon]}")       #分别打印每一个密码子的counts
#下面开始画图
labels=[]     #建立一个空列表储存pie的label，也就是codon的名字
sizes=[]    #建立一个空列表储存pie每一块的大小，也就是counts
for codon in codon_counts:
    labels.append(codon)    #把每一个codon都加入labels中
    sizes.append(codon_counts[codon])      #把每一个对应计数都加入sizes中
plt.figure(figsize=(12,12))
plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)     #autopct='%1.1f%%'表示会显示百分比
plt.title('Codon distribution upstream of '+selected_stop)
file_name="codon_pie_"+selected_stop+'.png'
plt.savefig(file_name)      #这一部非常重要，明确说了要把图保存到文件里面，不能只是show
plt.close()     #关闭图像，防止重复画图的时候出问题
print('Pie chart saved as', file_name)     #相当于提示你结束了