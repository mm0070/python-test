import csv
import os
from tabulate import tabulate

DIR = './data'
DATASET = 'dataset.csv'

def least_five_rent(tenant_list, header):
    # Requirement 1
    # sort the list in place, no need to reverse as the requirements specify ascending order
    tenant_list.sort(key=lambda x: x[-1:])

    return tenant_list[:5]


def lease_25_years(tenant_list, header):
    # Requirement 2
    # list comprehension
    mast_25y = [t for t in tenant_list if t[9] == 25]
    total_rent = sum(t[10] for t in mast_25y)

    return mast_25y, total_rent


# def mast_count(tenant_list, header):
#
def prepare_data(dir, dataset):
    # Read csv, save header to separate variable
    os.chdir(dir)
    with open(dataset) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        tenant_list = []
        for row in csv_reader:
            if count == 0:
                header = row
                count += 1
            else:
                tenant_list.append(row)

    # convert values to ints and floats and dates to datetime objects
    for t in tenant_list:
        t[10] = float(t[10]) #rent
        t[9] = int(t[9]) #lease duration

    return header, tenant_list


def main():
    header, tenant_list = prepare_data(DIR, DATASET)

    # Requirement 1
    least_five = least_five_rent(tenant_list, header)
    # tell the user what they're looking at
    print('Five tenants that pay the lowest rent:\n')
    # print out first 5, and make it pretty
    print(tabulate(least_five, headers=header))

    # Requirement 2
    lease_25y, total_25y = lease_25_years(tenant_list, header)
    print('\nTenants that have 25 year lease:\n')
    print(tabulate(lease_25y, headers=header))
    print('Total rent the above tenants pay: £{0:.2f}'.format(total_25y))


if __name__ == '__main__':
    main()