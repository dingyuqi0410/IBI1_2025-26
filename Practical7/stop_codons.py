import re
in_file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
out_file=open('stop_genes.fa','w')
stop_codons=['TAA','TAG','TGA']
header=''
sequence_lines = []

for line in in_file:
    line=line.rstrip()     
    if re.findall(r'^>',line):     
        if header!='':   
            sequence = ''.join(sequence_lines)     
            found_stops=[]    
            start_pos = sequence.find('ATG')      
            if start_pos != -1:      
                for i in range(start_pos, len(sequence) - 2, 3):     
                    codon = sequence[i:i+3]        
                    
                    if codon in stop_codons:
                        if codon not in found_stops:
                            found_stops.append(codon)       
            if found_stops:    
                name = re.findall(r'^>(\S+)', header)[0]         
                stop_text=found_stops[0]     
                if len(found_stops)>1:
                    stop_text=stop_text+' '+found_stops[1]     
                    if len(found_stops)>2:
                        stop_text=stop_text+' '+found_stops[2]     
                out_file.write('>' + name + '; ' + stop_text + '\n')      
                for seq_line in sequence_lines:
                    out_file.write(seq_line + '\n')    
        header=line     
        sequence_lines = []      
    else:
        sequence_lines.append(line)   
if header!='':      
    sequence = ''.join(sequence_lines)
    found_stops=[]
    start_pos = sequence.find('ATG')
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
        out_file.write('>' + name + '; ' + stop_text + '\n')
        for seq_line in sequence_lines:
            out_file.write(seq_line + '\n')
in_file.close()     
out_file.close()
print("Finished")