import argparse
import time
import csv

start = time.time()
file = open('data/names.csv', encoding="utf8")
names = {}
for i in file:
    data = i.split(',')
    if data[1] =='F\n':
    	names.update({data[0]:'Female'})
    elif data[1] =='M\n':
    	names.update({data[0]:'Male'})
    else:
    	names.update({data[0]:'Andy'})
file.close()

def gender(name):
    if name is "":
        return('null')
    name = name.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
    if name.capitalize() in names.keys():
        return (names[name.capitalize()])
    return ('IDK')

def gendercsv(INPUT):
    with open(INPUT, "r", encoding="utf8") as f_in, open('output.csv', 'w', encoding="utf8") as f_out:
        header = f_in.readline()
        header = header.rstrip()+",gender"
        f_out.write(header+'\n')
        reader = csv.reader(f_in) 
        writer = csv.writer(f_out) 
        for row in reader: 
            person = row[1] 
            person = person.split(' ', 1)[0] 
            print(person)
            gender_info=gender(person)
            row.extend([gender_info]) 
            writer.writerow(row)
    end = time.time()
    print(end - start,'seconds to process')
    return
                
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help = "input filename")
#    parser.add_argument("--output", help = "output filename")
    args = parser.parse_args()
    INP = args.input
#    OUT = args.output
    gendercsv(INP)

if __name__ == "__main__":
    # execute only if run as a script
    main()

