import csv

f = open("sample.csv", "w")
writer = csv.writer(f)
writer.writerow(["a", "1"])
f.close()