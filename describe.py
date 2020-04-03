import sys
import csv
import pandas as pd

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise "Usage: {} data_file".format(sys.argv[0])

    with open('test.csv', 'r') as csvfile:
        dataReader = csv.reader(csvfile, delimiter=',')

    df = pd.read_csv(sys.argv[1])
