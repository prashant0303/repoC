#!/usr/bin/python3

import csv
import argparse

parser = argparse.ArgumentParser(description="Mention input log file and output csv file")
parser.add_argument('-i', help="input log file", default="text.log"
parser.add_argument('-o', help="output csv file", default="output.csv")
args = vars(parser.parse_args())

def read_log(filename):
    file = []
    line = []
    messages = []
    file1 = open(filename, 'r')
    lines = file1.readlines()
    for eachline in lines:
        if "warning:" in eachline:
            data = eachline.split(':')
            file.append(data[0])
            line.append(data[1])
            data2 = eachline.split("warning:")
            messages.append(data2[1])
    rows = zip(file, line, messages)
    return(rows)

def write_csv(rows):
    with open(args['o'], "w") as f:
        writer = csv.writer(f)
        writer.writerow(('File', 'line', 'message'))
        for row in rows:
            writer.writerow(row)

if __name__ == "__main__":
    write_csv(read_log(args['i']))
