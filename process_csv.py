import csv
import os

from datetime import datetime
from pprint import pprint
from tabulate import tabulate

DIR = './data'
DATASET = 'dataset.csv'
START_DATE = datetime(1999, 6, 1, 0, 0)
END_DATE = datetime(2007, 8, 31, 0, 0)

def least_five_rent(tenant_list, header):
    # sort the list in place, no need to reverse as the requirements specify ascending order
    tenant_list.sort(key=lambda x: x[-1:])

    return tenant_list[:5]


def lease_25_years(tenant_list, header):
    mast_25y = [t for t in tenant_list if t[9] == 25]
    total_rent = sum(t[10] for t in mast_25y)

    return mast_25y, total_rent


def mast_count(tenant_list):
    transposed_list = list(map(list, zip(*tenant_list)))[6] # 7th column is tenant name
    tenants_list = list(dict.fromkeys(transposed_list))
    mast_count = {t: transposed_list.count(t) for t in tenants_list}

    return mast_count


def date_range(tenant_list, start_date, end_date):
    dates_list = [t for t in tenant_list if (t[7]>start_date and t[7]<end_date)]
    # format dates
    for d in dates_list:
        d[7] = datetime.strftime(d[7], '%d/%m/%Y')
        d[8] = datetime.strftime(d[8], '%d/%m/%Y')

    return dates_list


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

    # convert values used to ints and floats
    for t in tenant_list:
        t[7] = datetime.strptime(t[7], '%d %b %Y')
        t[8] = datetime.strptime(t[8], '%d %b %Y')
        t[9] = int(t[9])  # lease duration
        t[10] = float(t[10]) #rent


    return header, tenant_list


def main():
    header, tenant_list = prepare_data(DIR, DATASET)

    choice = input('Choose from the following options: \n\
                    0 - Run tasks 1 to 4\n\
                    1 - Run task 1 only\n\
                    2 - Run task 2 only\n\
                    3 - Run task 3 only\n\
                    4 - Run task 4 only\n\
                    Input: ')

    if choice == '0':
        least_five = least_five_rent(tenant_list, header)
        lease_25y, total_25y = lease_25_years(tenant_list, header)
        tenant_mast_count = mast_count(tenant_list)
        dates_limited = date_range(tenant_list, START_DATE, END_DATE)
        print('Five tenants that pay the lowest rent:\n')
        print(tabulate(least_five, headers=header))
        print('\nTenants that have 25 year lease:\n')
        print(tabulate(lease_25y, headers=header))
        print('Total rent the above tenants pay: £{0:.2f}'.format(total_25y))
        print('\nMast count per tenant: \n')
        print(tabulate(tenant_mast_count.items(), headers=['Tenant Name', 'Mast Count']))
        print('\nTenants with lease start date between 1st of June 1999 and 31st of August 2007: \n')
        print(tabulate(dates_limited, headers=header))
    elif choice == '1':
        # Requirement 1
        least_five = least_five_rent(tenant_list, header)
        print('Five tenants that pay the lowest rent:\n')
        print(tabulate(least_five, headers=header))
    elif choice == '2':
        # Requirement 2
        lease_25y, total_25y = lease_25_years(tenant_list, header)
        print('\nTenants that have 25 year lease:\n')
        print(tabulate(lease_25y, headers=header))
        print('Total rent the above tenants pay: £{0:.2f}'.format(total_25y))
    elif choice == '3':
        # Requirement 3
        tenant_mast_count = mast_count(tenant_list)
        print('\nMast count per tenant: \n')
        print(tabulate(tenant_mast_count.items(), headers=['Tenant Name', 'Mast Count']))
    elif choice == '4':
        # Requirement 4
        dates_limited = date_range(tenant_list, START_DATE, END_DATE)
        print('\nTenants with lease start date between 1st of June 1999 and 31st of August 2007: \n')
        print(tabulate(dates_limited, headers=header))


if __name__ == '__main__':
    main()