import csv

file1 = "dwarf_stars2.csv"
file2 = "unit_converted_stars.csv"

dataset_1 = []
dataset_2 = []

with open(file1,"r", encoding = "utf8" ) as f:
    csv_reader =csv.reader(f)
    for i in csv_reader:
        dataset_1.append(i)
        
with open(file2, "r", encoding = "utf8" ) as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        dataset_2.append(i)

headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

headers = headers_1 + headers_2
planet_data = []

for i in planet_data_1:
    planet_data.append(i)
for j in planet_data_2:
    planet_data.append(j)
with open("total_stars.csv", "w", encoding = "utf8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(planet_data)