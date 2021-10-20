import csv
import json

# example-1
data = '''
{
    "Results":
        [
            {"id": 1, "Name": "Jay"},
            {"id": 2, "Name": "John"},
            {"id": 3, "Name": "Jane"}
        ],
    "status": ["ok"]
}
'''

info = json.loads(data)['Results']

print(info[0].keys())

with open("sample.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=info[0].keys())
    writer.writeheader()
    writer.writerows(info)

# example-2
with open('new_json.json', 'r') as f:
    data = json.load(f)

    print(data["people"][0].keys())

    with open('new_csv.csv', 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data["people"][0].keys())
        writer.writeheader()
        writer.writerows(data["people"])

# example-3
with open('new_json.json', 'r') as f:
    data = json.load(f)

    print(data["people"][0].keys())

    with open('test_csv.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        for row in range(len(data["people"])):
            # print(data["people"][row].values())
            writer.writerow(data["people"][row].values())