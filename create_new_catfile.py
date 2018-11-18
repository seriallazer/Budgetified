import config_file
import csv

outfile = '/Users/mayankgupta/Documents/Budget/Categories_all_NEW.csv'

infile = open(config_file.old_category_file, 'r')
ofile = open(outfile, 'w+')
writer = csv.writer(ofile, delimiter=';')

for line in infile.readlines():
    tokens = line.strip().split(';')
    key = tokens[0]
    val = '|'.join(tokens[1:])
    if tokens[-1] == '':
        val = '|'.join(tokens[1:-1])
    writer.writerow([key,val])