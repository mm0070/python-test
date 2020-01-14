import csv
import os
from tabulate import tabulate


def least_five_rent(tenant_list, header):
    # Requirement 1
    # convert values to floats and dates to datetime objects
    for t in tenant_list:
        t[10] = float(t[10])

    # sort the list in place, no need to reverse as the requirements specify ascending order
    tenant_list.sort(key=lambda x: x[-1:])

    # tell the user what they're looking at
    print('Five tenants that pay the lowest rent:\n')
    # print out first 5, and make it pretty
    print(tabulate(tenant_list[:5], headers=header))


def lease_25_years(tenant_list, header):
    # Requirement 2
    # list comprehension
    mast_25y = [t for t in tenant_list if t[9] == '25']

    total_rent = sum(t[10] for t in mast_25y)

    print('\nTenants that have 25 year lease:\n')
    print(tabulate(mast_25y, headers=header))
    print('Total rent the above tenants pay: £{0:.2f}'.format(total_rent))


def main():
    # Read csv, save header to separate variable
    os.chdir('./data')
    with open('dataset.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        tenant_list = []
        for row in csv_reader:
            if count == 0:
                header = row
                count += 1
            else:
                tenant_list.append(row)

    least_five_rent(tenant_list, header)
    lease_25_years(tenant_list, header)



if __name__ == '__main__':
    main()