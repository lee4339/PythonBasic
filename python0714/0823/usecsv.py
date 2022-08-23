import csv

def open_csv(file_name):
    f = open(file_name, 'r', encoding='UTF-8')

    csv_reader = csv.reader(f)
    read_data = []

    for item in csv_reader:
        read_data.append(item)

    f.close()

    return read_data

def write_csv(file_name, write_data_list):
    f = open(file_name, 'w', encoding='UTF-8', newline='')

    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerows(write_data_list)

    f.close()
