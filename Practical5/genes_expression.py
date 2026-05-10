import matplotlib.pyplot as plt
#step 1
genes={"TP53":12.4,"EGFR":15.1,"BRCA1":8.2,"PTEN":5.3,"ESR1":10.7}
print(genes)
#step 2
genes["MYC"]=11.6
print(genes)
#step 3
gene=list(genes.keys())     
expression_values=list(genes.values())     
plt.figure(figsize=(8,5))   
plt.bar(gene, expression_values,width=0.35)     
plt.title("Gene Expression Levels")
plt.xlabel("Gene")
plt.ylabel("Expression Value")
plt.tight_layout()    
plt.show()   
#step 4
# Here is the variable, you can change the gene name below if you want to test another gene
gene_of_interest="EGFR"
if gene_of_interest in genes:
    print(genes[gene_of_interest])
else:
    print(f"Error:{gene_of_interest} is not present in the dataset.")
#step 5
total=0
for expression_value in expression_values:
    total+=expression_value
mean_expression=total/len(expression_values)
print(mean_expression)