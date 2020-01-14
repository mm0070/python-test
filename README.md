## What is it
It's a script that processes UK mobile phone mast data in csv format, and displays the following information:
  * 1 - 5 tenants that pay the least rent
  * 2 - All tenants that have signed a 25 year lease
  * 3 - Mast count for each tenant
  * 4 - Rentals with lease date between 1st Jun 1999 and 31st Aug 2007

## How to use
Just run process_csv.py with no arguments, then choose from one of the following options:
  * 0 - Run tasks 1-4
  * 1 - Run task 1 - Show 5 tenants that pay the least rent
  * 2 - Run task 2 - Show all tenants with 25 year lease
  * 3 - Run task 3 - Show mast count for each tenant
  * 4 - Run task 4 - Show rentals with lease date between 1st Jun 1999 and 31st Aug 2007

## Dependencies
`tabulate` in order to format the output
