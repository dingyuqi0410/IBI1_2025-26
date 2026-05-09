import re
import matplotlib.pyplot as plt
in_file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
stop_codons=['TAA','TAG','TGA']
selected_stop=input("Enter one stop codon (TAA, TAG or TGA): ")
while selected_stop not in stop_codons:
    selected_stop = input("Invalid input. Please enter TAA, TAG or TGA: ")

header=''
sequence=''
codon_counts={}     
gene_total=0
for line in in_file:
    line=line.rstrip()
    if re.findall(r'^>',line):
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
                gene_total += 1
                for i in range(0,len(longest_orf)-3,3):    
                    codon=longest_orf[i:i+3]      
                    if codon in codon_counts:         
                        codon_counts[codon]=codon_counts[codon]+1      
                    else:        
                        codon_counts[codon]=1      
        header=line
        sequence=''
    else:
        sequence+=line

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
for codon in codon_counts:     
    print(f"{codon}: {codon_counts[codon]}")       

labels=[]    
sizes=[]    
for codon in codon_counts:
    labels.append(codon)    
    sizes.append(codon_counts[codon])      
plt.figure(figsize=(12,12))
plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90,labeldistance=1.08,pctdistance=0.80,textprops={'fontsize': 7})    
plt.title('Codon distribution upstream of '+selected_stop)
file_name='codon_pie.png'
plt.savefig(file_name)     
plt.close()     
print('Pie chart saved as', file_name)     