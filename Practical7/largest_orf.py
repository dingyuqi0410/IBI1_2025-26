import re
seq='AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
stop_codons=['UAA','UAG','UGA']
largest_orf=''
for i in range(len(seq)-2):      
    part=seq[i:]
    codons=re.findall(r'[AUCG]{3}',part)      
    if codons and codons[0]=='AUG':    
        current_orf='' 
        for codon in codons:       
            current_orf+=codon       
            if codon in stop_codons:   
                if len(current_orf)>len(largest_orf):     
                    largest_orf=current_orf
                break
if largest_orf:
    print(largest_orf)
    print(len(largest_orf))
else:
    print('No ORF Found')