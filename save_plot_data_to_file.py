from typing import Sequence
import csv

def save_function_data(function_number: int, data_dict: Sequence):
    file_name = ""
    if function_number == 1:
        file_name = "result_fx.csv"
    elif function_number == 2:
        file_name = "result_gx.csv"
    else:
        raise ValueError('function_number can be either 1 or 2')
    with open(file_name, 'w', newline='') as file:
        fieldnames = data_dict[0].keys()
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for row in data_dict:
            csv_writer.writerow(row)
