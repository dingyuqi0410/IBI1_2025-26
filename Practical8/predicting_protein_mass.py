def predicting_protein_mass(sequence):     
    residue_mass={      
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
    total_mass=0       
    sequence=sequence.upper()       
    for amino_acid in sequence:
        if amino_acid not in residue_mass:
            return "Error: amino acid "+ amino_acid+" has no recorded mass"     
        total_mass=total_mass+residue_mass[amino_acid]
    return total_mass
example_sequence="GAS"
example_mass=predicting_protein_mass(example_sequence)
print(f"Sequence: {example_sequence}")
#print results
if type(example_mass) == str:      #if the result is a string, it means there was an error, so we print the error message
    print(example_mass)       
else:          #if the result is not a string, it means we got a valid mass, so we print the mass and the units
    print(f"Protein mass: {example_mass} amu")