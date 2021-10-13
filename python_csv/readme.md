## read, parse and write csv files

```python
import csv

# csv.reader and csv.writer methods
with open('file.csv', 'r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        print(row)

    with open('file_to_save', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file)

        for line in csv_reader:
            csv_writer.writerow(line)
```

```python
# csv.DictReader and csv.DictWriter classes
with open('file.csv', 'r') as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        print(row['key'])

    with open('file_to_save', 'w', newline='') as new_file:
        fieldnames = [
            'key1',
            'key2',
            'key3'
        ]

        csv_writer = csv.DictWriter(
            new_file,
            fieldnames=fieldnames
            )

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email'] # in case you wish to delete a specific column  or key
            csv_writer.writerow(line)
```
