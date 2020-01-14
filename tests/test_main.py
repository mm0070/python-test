import unittest

from datetime import datetime

from process_csv import prepare_data, least_five_rent, lease_25_years, mast_count, date_range

test_data = [['Beecroft Hill', 'Broad Lane', '', '', 'LS13', 'Beecroft Hill - Telecom App',
                   'Arqiva Services ltd', datetime(1994, 3, 1, 0, 0), datetime(2058, 2, 28, 0, 0), 64, 23950.00],
                  ['Potternewton Crescent', 'Potternewton Est Playing Field', '', '', 'LS7',
                   'Potternewton Est Playing Field', 'Arqiva Ltd', datetime(1999, 6, 24, 0, 0),
                   datetime(2019, 6, 23, 0, 0), 20, 6600.00],
                  ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14',
                   'Seacroft Gate (Chase) block 2-Telecom App.', 'Vodafone Ltd.', datetime(2004, 1, 30, 0, 0),
                   datetime(2029, 1, 29, 0, 0), 25, 12250.00],
                  ['Queenswood Heights', 'Queenswood Heights', 'Queenswood Gardens', 'Headingley', 'Leeds',
                   'Queenswood Hgt-Telecom App.', 'Vodafone Ltd', datetime(2004, 11, 8, 0, 0),
                   datetime(2029, 11, 7, 0, 0), 25, 9500.00],
                  ['Armley - Burnsall Grange', 'Armley', 'LS13', '', '', 'Burnsall Grange CSR 37865', 'O2 (UK) Ltd',
                   datetime(2007, 7, 26, 0, 0), datetime(2032, 7, 25, 0, 0), 25, 12000.00]]
test_header = ['Property Name', 'Property Address [1]', 'Property  Address [2]', 'Property Address [3]',
                    'Property Address [4]', 'Unit Name', 'Tenant Name', 'Lease Start Date', 'Lease End Date',
                    'Lease Years', 'Current Rent']
start_date = datetime(1999, 6, 1, 0, 0)
end_date = datetime(2007, 8, 31, 0, 0)

class TestProcessCsv(unittest.TestCase):


    def test_prepare_data(self):
        # Test if data processing works as expected
        DIR = '../data'
        DATASET = 'dataset.csv'
        header, tenant_list = prepare_data(DIR, DATASET)
        self.assertEqual(header[0], 'Property Name')
        self.assertEqual(tenant_list[0][7], datetime(1994, 3, 1, 0, 0))
        self.assertEqual(tenant_list[0][8], datetime(2058, 2, 28, 0, 0))
        self.assertEqual(tenant_list[0][10], 23950.0)
        self.assertEqual(tenant_list[0][0], 'Beecroft Hill')
        self.assertEqual(len(tenant_list), 42) # the answer to life, universe, and everything, and also the length of this list


    def test_five_rent(self):
        result = least_five_rent(test_data, test_header)
        self.assertEqual(result[0][0], 'Potternewton Crescent')
        self.assertEqual(len(result), 5)


    def test_lease_25y(self):
        mast_25y, total = lease_25_years(test_data, test_header)
        self.assertEqual(mast_25y[0][0], 'Seacroft Gate (Chase) - Block 2')
        self.assertEqual(len(mast_25y), 3)


    def test_mast_count(self):
        count = mast_count(test_data)
        self.assertEqual(count, {'Arqiva Services ltd': 1, 'Arqiva Ltd': 1, 'Vodafone Ltd.': 1,
                                 'Vodafone Ltd': 1, 'O2 (UK) Ltd': 1})

    def test_dates(self):
        dates = date_range(test_data, start_date, end_date)
        self.assertEqual(len(dates), 4)

                         )
if __name__ == '__main__':
    unittest.main()