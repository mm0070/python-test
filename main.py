import csv
import os
from tabulate import tabulate

def main():
    # Some preparations first

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

        # Requirement 1
        #convert values to floats and dates to datetime objects
        for t in tenant_list:
            t[10] = float(t[10])

        #sort the list in place, no need to reverse as the requirements specify ascending order
        tenant_list.sort(key=lambda x: x[-1:])

        # tell the user what they're looking at
        print('Five tenants that pay the lowest rent:\n')
        # print out first 5, and make it pretty
        print(tabulate(tenant_list[:5], headers=header))



if __name__ == '__main__':
    main()