from src import config_file
import csv

infile = open(config_file.old_category_file, 'r')
ofile = open(config_file.category_file, 'w+')
writer = csv.writer(ofile, delimiter=';')

for line in infile.readlines():
    tokens = line.strip().split(';')
    key = tokens[0]
    val = '|'.join(tokens[1:])
    if tokens[-1] == '':
        val = '|'.join(tokens[1:-1])
    writer.writerow([key,val])