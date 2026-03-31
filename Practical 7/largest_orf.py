import re
seq='AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
stop_codons=['UAA','UAG','UGA']
largest_orf=''
for i in range(len(seq)-2):      #-2的原因：因为一次要取三个连续的密码子，如果取到最后两个就取不了了，所以直接-2
    part=seq[i:]
    codons=re.findall(r'[AUCG]{3}',part)      #[AUCG]表示匹配的字符一定要是AUCG中的一个，和[0-9]是一个意思。{3}表示前面的模式连着出现三次，对应密码子一次要取三个
    if codons and codons[0]=='AUG':     #如果codons这个列表不是空的（if codons），并且第一个codon是AUG（codons[0]=='AUG')，那就继续，进入循环
        current_orf='' 
        for codon in codons:    #依次读取codons列表里面的每一个codon   
            current_orf+=codon       #把当前读到的codon接到current_orf的后面，也就是逐步把整个ORF拼起来，此时current_orf里面有所有满足第一个密码子是AUG的序列
            if codon in stop_codons:    #如果当前的这个codon是终止密码子
                if len(current_orf)>len(largest_orf):     #如果当前ORF比目前记录里的最长ORF长
                    largest_orf=current_orf
                    break
if largest_orf:
    print(largest_orf)
    print(len(largest_orf))
else:
    print('No ORF Found')