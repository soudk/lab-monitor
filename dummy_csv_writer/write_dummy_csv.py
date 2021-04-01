import csv
from csv import writer
import os
import time
from random import random


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def write_headerlist_as_row(file_name, list_of_elem):
    with open(file_name, 'w') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)



filename  = 'dummy.csv'
headers = ['time','temperature 1','temperature 2']
while(True):
    t = time.time()*1000
    r1 = random()*100
    r2 = random()*100
    r3 = random()*1000
    data = [t, r1, r2, r3] #random data to be appended

    if os.path.exists(filename):
        append_list_as_row(filename, data)
    else:
        write_headerlist_as_row(filename, headers)
    
    time.sleep(2)

