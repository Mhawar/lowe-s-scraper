file_name = 'Promo1.txt' #Put here your file

with open(file_name,'r') as fnr:
    text = fnr.readlines()

text = "'".join([line.strip() + "'," for line in text])

with open(file_name,'w') as fnw:
    fnw.write(text)