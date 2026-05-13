import pandas as pd  # 导入 pandas，用来读取和处理 BLOSUM62 矩阵表格

def read_sequence(file_path):  # 定义函数，用来读取 FASTA 文件中的蛋白质序列
    seq = ""  # 创建一个空字符串，用来保存蛋白质序列
    file = open(file_path, "r")  # 打开 FASTA 文件，"r" 表示只读取文件
    for line in file:  
        line = line.strip()  # 去掉每一行前后的空格和换行符
        if line.startswith(">"):  # 如果这一行以 > 开头，说明它是 FASTA 的标题行
            continue  # 跳过标题行，因为我们只需要蛋白质序列
        else:  
            seq = seq + line 
    file.close()  
    return seq  

df = pd.read_csv("BLOSUM62.txt", sep=r"\s+", comment="#", index_col=0, header=0)  # 读取 BLOSUM62.txt，sep=r"\s+" 表示用空格分隔（否则read_csv会默认是逗号分隔的），comment="#" 表示跳过 # 开头的说明行。index_col=0 表示第一列是行索引，header=0 表示第一行是列名，转换成 DataFrame 格式
blosum62_matrix = df.to_dict("index")  # 将 DataFrame 转换成嵌套字典，之后可以用 blosum62_matrix[aa1][aa2] 查分数, aa1代表行，aa2代表列

def calculate_score(seq1, seq2, blosum62_matrix):     #此处blosum62_matrix是一个嵌套字典，外层字典（代表行）的键是氨基酸，内层字典（代表列）的键也是氨基酸，值是对应的分数
    score = 0  
    for aa1, aa2 in zip(seq1, seq2):    # 同时逐位读取 seq1 和 seq2 中的氨基酸，zip() 函数会把 seq1 和 seq2 中的氨基酸配对在一起，例如第一个氨基酸配对在一起，第二个氨基酸配对在一起，以此类推
        score = score + blosum62_matrix[aa1][aa2]  # 根据 aa1 和 aa2 在 BLOSUM62 矩阵中找到分数，并加到总分中
    return score  

def calculate_identity(seq1, seq2):  
    identical = 0  # 创建变量 identical，用来统计完全相同的氨基酸数量
    for a, b in zip(seq1, seq2):  # 同时逐位读取两条序列中的氨基酸
        if a == b:  # 如果当前位置的两个氨基酸完全相同
            identical = identical + 1  
    identity = identical / len(seq1) * 100  
    return identity  

human_seq = read_sequence("human_DLX5.fasta")  
mouse_seq = read_sequence("mouse_DLX5.fasta")  
random_seq = read_sequence("random_DLX5.fasta")  

score=calculate_score(human_seq, mouse_seq, blosum62_matrix)
identity=calculate_identity(human_seq, mouse_seq)
print(f"Human vs Mouse: Score = {score}, Identity = {identity:.2f}%")

score=calculate_score(human_seq, random_seq, blosum62_matrix)
identity=calculate_identity(human_seq, random_seq)
print(f"Human vs Random: Score = {score}, Identity = {identity:.2f}%")      

score=calculate_score(mouse_seq, random_seq, blosum62_matrix)
identity=calculate_identity(mouse_seq, random_seq)      
print(f"Mouse vs Random: Score = {score}, Identity = {identity:.2f}%")      