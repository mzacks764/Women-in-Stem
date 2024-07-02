import os
import csv
import collections

data = []

Record = collections.namedtuple(
    'Record','Rank, Major_code, Major, Major_category, Total, Men, Women, ShareWomen, Median'
)

def main():
    print()
    print('Women in STEM data')
    print()

    init()


    popular_majors = top_majors()
    unpopular_majors = bottom_majors()

    print('10 STEM Majors with the highest percent women.')
    for idx, d in enumerate(popular_majors[0:10]):
        print(f'{idx+1} {d.Major.title()} {d.ShareWomen}')

    print()
    print('10 STEM Majors with lowest percent women.')
    for idx, d in enumerate(unpopular_majors[0:10]):
        print(f'{idx + 1} {d.Major.title()} {d.ShareWomen}')
'''
Init opens the file women_stem.csv and uses DictReader to import the data.
Next it reads the data row by row and prints the row to screen

'''
def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'women_stem.csv')
    with open(filename, 'r', encoding='utf-8') as bin:
        reader = csv.DictReader(bin)

        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)
            #print(f"The median salary for {(record.Major.lower())} is ${record.Median}")

def parse_row(row):
    #Rank, Major_code, Major, Major_category, Total, Men, Women, ShareWomen, Median
    #1, 2419, PETROLEUM, ENGINEERING, Engineering, 2339, 2057, 282, 0.120564344, 110000

    row['Rank'] = int(row['Rank'])
    row['Major_code'] = int(row['Major_code'])
    row['Total'] = int(row['Total'])
    row['Men'] = int(row['Men'])
    row['Women'] = int(row['Women'])
    row['ShareWomen'] = float(row['ShareWomen'])
    row['Median']= int(row['Median'])

    record = Record(
        **row
    )
    return record

def top_majors():
    return sorted(data, key=lambda r: -r.ShareWomen)

def bottom_majors():
    return sorted(data, key=lambda r: r.ShareWomen)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
