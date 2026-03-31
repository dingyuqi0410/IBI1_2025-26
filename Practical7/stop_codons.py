import re
in_file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
out_file=open('stop_genes.fa','w')
stop_codons=['TAA','TAG','TGA']
header=''
sequence=''
for line in in_file:
    line=line.rstrip()     #去掉行尾的\n
    if re.findall(r'^>',line):     #这里讨论header的行数情况。判断是不是FASTA的标题行,^表示行开头（标题行开头是>）
        if header!='':    #header不是空的，说明前面已经读到过一个基因的标题行了，那么就先处理手头的这个读到的基因
            found_stops=[]     #创建一个空列表，用来储存找到的file中的stop codon类型
            for i in range(len(sequence)-2):
                part=sequence[i:]
                codons=re.findall(r'[ATGC]{3}',part)
                if codons and codons[0]=='ATG':
                    for codon in codons[1:]:       #跳过ATG从第二个往后数
                        if codon in stop_codons:
                            if codon not in found_stops:
                                found_stops.append(codon)       
                                break       #相当于把还没有被found的终止密码子加入found的列表中，然后结束这个循环
            if found_stops:    #现在讲的就是found_stops中已经有东西了的情况
                gene_name=re.findall(r'gene:([^\s]+)',header)        #先找到gene:，然后把后面连续的非空白字符提取出来(^的意思是“不是”)
                name=gene_name[0]    #此时gene_name是一个列表，所以要用[0]把它拿出来
                stop_text=found_stops[0]
                if len(found_stops)>1:
                    stop_text=stop_text+' '+found_stops[1]     #拼接字符串，把第二个拼到第一个后面，中间加一个空格
                    if len(found_stops)>2:
                        stop_text=stop_text+' '+found_stops[2]     #总共也就三种，这样写够了
                out_file.write('>'+name+' '+stop_text+'\n')       #格式类似于：YBR024W TGA TAA TAG
                out_file.write(sequence+'\n')
        header=line     #把当前这一行新的标题存起来，因为接下来的程序要开始读取这个基因。比如说一开始header是空的，那么就会执行这一行把line加进去，这一行不能放到前面去
        sequence=''      #把sequence清空，因为新的sequence还没有开始讲
    else:
        sequence=sequence+line     #把这一行的sequence拼接到当前基因的sequence后面
if header!='':      #以下相当于是处理“最后一个基因”。上面的主循环的意思是碰到了下一个header才会去处理上一个基因（因为碰到下一个header意味着知道上一个结束了），但是对最后一个基因就无效了，所以需要手动处理一次
    found_stops=[]
    for i in range(len(sequence)-2):
        part=sequence[i:]
        codons=re.findall(r'[ATCG]{3}',part)
        if codons and codons[0]=='ATG':
            for codon in codons[1:]:
                if codon in stop_codons:
                    if codon not in found_stops:
                        found_stops.append(codon)
                        break
    if found_stops:
        gene_name=re.findall(r'gene:([^\s]+)',header)
        name=gene_name[0]
        stop_text=found_stops[0]
        if len(found_stops) > 1:
            stop_text = stop_text + ' ' + found_stops[1]
            if len(found_stops) > 2:
                stop_text = stop_text + ' ' + found_stops[2]
        out_file.write('>' + name + ' ' + stop_text + '\n')
        out_file.write(sequence + '\n')
in_file.close()     #记得close
out_file.close()
print("Finished")