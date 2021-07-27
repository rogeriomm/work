#
#
#

from faker import Faker
import csv
import pandas as pd
import json


def write_file():
    print('Writing file')
    output = open('data.csv', 'w')
    fake = Faker()

    header = ['name', 'age', 'street', 'city', 'state', 'zip', 'lng', 'lat']

    mywriter = csv.writer(output)
    mywriter.writerow(header)

    for r in range(1000):
        mywriter.writerow([fake.name(), fake.random_int(min=18, max=80, step=1), fake.street_address(),
                           fake.city(), fake.state(), fake.zipcode(), fake.longitude(), fake.latitude()])


def read_file():
    print("Reading file")
    with open('data.csv') as f:
        myreader = csv.DictReader(f)
        headers = next(myreader)
        for row in myreader:
            print(row['name'])


def panda_read():
    print("Panda: reading file")
    df = pd.read_csv('data.csv')
    df.head(10)
    print(df)


def create_pandas_dataframe():
    data = {'Name': ['Paul', 'Bob', 'Susan', 'Yolanda'], 'Age': [23, 45, 18, 21]}
    df = pd.DataFrame(data)
    print(df)
    df.to_csv('fromdf.csv', index=False)


def write_json():
    output = open('data.json', 'w')
    fake = Faker()
    alldata = {'records': []}  # Empty dictionary
    for x in range(1000):
        data = {"name": fake.name(), "age": fake.random_int(min=18, max=80, step=1),
                "street": fake.street_address(),
                "city": fake.city(), "state": fake.state(),
                "zip": fake.zipcode(),
                "lng": float(fake.longitude()),
                "lat": float(fake.latitude())}
        alldata['records'].append(data)
    json.dump(alldata, output)


def read_json():
    with open("data.json", "r") as f:
        data = json.load(f)

    print(data['records'][0])
    print(data['records'][1])


def read_pandas_json():
    print("Read json file using Pandas")
    df = pd.read_json('data.json')
    print(df)

7
def main():
    x = input("Option: ")

    cases = {
        '1': lambda: write_file(),
        '2': lambda: read_file(),
        '3': lambda: panda_read(),
        '4': lambda: create_pandas_dataframe(),
        '5': lambda: write_json(),
        '6': lambda: read_json(),
        '7': lambda: read_pandas_json()
    }

    cases.get(x, lambda: print("Didn't match a case"))()


if __name__ == '__main__':
    main()
