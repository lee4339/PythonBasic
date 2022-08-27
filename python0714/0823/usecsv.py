import csv


# open_csv() 는 지정한 파일을 읽어서 사용자에게 데이터를 넘겨줌
def open_csv(file_name):
    f = open(file_name, 'r', encoding='UTF-8')

    csv_reader = csv.reader(f)
    read_data = []

    for item in csv_reader:
        read_data.append(item)

    f.close()

    return read_data


# write_csv() 는 매개변수로 받은 데이터를 지정한 파일로 저장
def write_csv(file_name, write_data_list):
    f = open(file_name, 'w', encoding='UTF-8', newline='')

    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerows(write_data_list)

    f.close()

