import csv

# open csv file and work with csv.reader and csv.writer methods
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # for line in csv_reader:
    #     print(line[2])

    with open('new_names.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)



# open csv file and specify the delimiter parameter value in csv.reader method
with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)
