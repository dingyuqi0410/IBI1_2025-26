def predicting_protein_mass(sequence):     #定义函数predicting_protein_mass，参数sequence表示输入的氨基酸序列
    residue_mass={      #用一个字典保存氨基酸字母编号和对应的质量
        "G":57.02,
        "A":71.04,
        "S": 87.03,  
        "P": 97.05,  
        "V": 99.07,  
        "T": 101.05,  
        "C": 103.01,  
        "I": 113.08,  
        "L": 113.08,  
        "N": 114.04,   
        "D": 115.03, 
        "Q": 128.06,  
        "K": 128.09,  
        "E": 129.04,  
        "M": 131.04,   
        "H": 137.06,  
        "F": 147.07,  
        "R": 156.10,  
        "Y": 163.06, 
        "W": 186.08 
    }
    total_mass=0       #从0开始累加总质量
    sequence=sequence.upper()       
    for amino_acid in sequence:
        if amino_acid not in residue_mass:
            return "Error: amino acid "+ amino_acid+" has no recorded mass"     #如果找不到，立刻返回错误信息，不再往下继续
        total_mass=total_mass+residue_mass[amino_acid]
    return total_mass
example_sequence="GJS"
example_mass=predicting_protein_mass(example_sequence)
print(f"Sequence: {example_sequence}")
print(f"Protein mass: {example_mass} amu")