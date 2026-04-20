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
            start_pos = sequence.find('ATG')      #在当前序列中找第一个“ATG”，如果找到了就返回第一个ATG的位置，找不到就返回-1
            if start_pos != -1:      #会看完整个sequence，然后循环结束
                for i in range(start_pos, len(sequence) - 2, 3):      #从第一个 ATG 开始，每次往后跳 3 个碱基，到倒数第三个结束
                    codon = sequence[i:i+3]        #在位置i取出一个codon，也就是3个碱基
                    
                    if codon in stop_codons:
                        if codon not in found_stops:
                            found_stops.append(codon)       
            if found_stops:    #现在讲的就是found_stops中已经有东西了的情况
                name = re.findall(r'^>(\S+)', header)[0]     #找到所有最前面的序列名，（但是此时得到的是列表）[0]用来把列表的第一个提取出来    
                stop_text=found_stops[0]     #先把第一个放好，后面再拼接
                if len(found_stops)>1:
                    stop_text=stop_text+' '+found_stops[1]     #拼接字符串，把第二个拼到第一个后面，中间加一个空格
                    if len(found_stops)>2:
                        stop_text=stop_text+' '+found_stops[2]     #总共也就三种，这样写够了
                out_file.write('>' + name + ';' + stop_text + '\n')      #格式类似于：YBR024W_mRNA;TGA 
                out_file.write(sequence+'\n')
        header=line     #把当前这一行新的标题存起来，因为接下来的程序要开始读取这个基因。比如说一开始header是空的，那么就会执行这一行把line加进去，这一行不能放到前面去
        sequence=''      #把sequence清空，因为新的sequence还没有开始讲
    else:
        sequence=sequence+line     #把这一行的sequence拼接到当前基因的sequence后面
if header!='':      #以下相当于是处理“最后一个基因”。上面的主循环的意思是碰到了下一个header才会去处理上一个基因（因为碰到下一个header意味着知道上一个结束了），但是对最后一个基因就无效了，所以需要手动处理一次
    found_stops=[]
    if start_pos != -1:
        for i in range(start_pos, len(sequence) - 2, 3):
            codon = sequence[i:i+3]
                
            if codon in stop_codons:
                if codon not in found_stops:
                    found_stops.append(codon)
    if found_stops:
        name = re.findall(r'^>(\S+)', header)[0]
        stop_text=found_stops[0]
        if len(found_stops) > 1:
            stop_text = stop_text + ' ' + found_stops[1]
            if len(found_stops) > 2:
                stop_text = stop_text + ' ' + found_stops[2]
        out_file.write('>' + name + ';' + stop_text + '\n')
        out_file.write(sequence + '\n')
in_file.close()     #记得close
out_file.close()
print("Finished")