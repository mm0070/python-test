import unittest

from process_csv import prepare_data, least_five_rent, lease_25_years

test_data = [['Beecroft Hill', 'Broad Lane', '', '', 'LS13', 'Beecroft Hill - Telecom App',
                   'Arqiva Services ltd', '01 Mar 1994', '28 Feb 2058', 64, 23950.00],
                  ['Potternewton Crescent', 'Potternewton Est Playing Field', '', '', 'LS7',
                   'Potternewton Est Playing Field', 'Arqiva Ltd', '24 Jun 1999', '23 Jun 2019', 20, 6600.00],
                  ['Seacroft Gate (Chase) - Block 2', 'Telecomms Apparatus', 'Leeds', '', 'LS14',
                   'Seacroft Gate (Chase) block 2-Telecom App.', 'Vodafone Ltd.', '30 Jan 2004',
                   '29 Jan 2029', 25, 12250.00],
                  ['Queenswood Heights', 'Queenswood Heights', 'Queenswood Gardens', 'Headingley', 'Leeds',
                   'Queenswood Hgt-Telecom App.', 'Vodafone Ltd', '08 Nov 2004', '07 Nov 2029', 25, 9500.00],
                  ['Armley - Burnsall Grange', 'Armley', 'LS13', '', '', 'Burnsall Grange CSR 37865', 'O2 (UK) Ltd',
                   '26 Jul 2007', '25 Jul 2032', 25, 12000.00]]
test_header = ['Property Name', 'Property Address [1]', 'Property  Address [2]', 'Property Address [3]',
                    'Property Address [4]', 'Unit Name', 'Tenant Name', 'Lease Start Date', 'Lease End Date',
                    'Lease Years', 'Current Rent']

class TestProcessCsv(unittest.TestCase):


    def test_prepare_data(self):
        # Test if data processing works as expected
        DIR = '../data'
        DATASET = 'dataset.csv'
        header, tenant_list = prepare_data(DIR, DATASET)
        self.assertEqual(header[0], 'Property Name')
        self.assertEqual(tenant_list[10][0], 'Gledhow Towers - Telecom App')


    def test_five_rent(self):
        result = least_five_rent(test_data, test_header)
        self.assertEqual(result[0][0], 'Potternewton Crescent')
        self.assertEqual(len(result), 5)


    def test_lease_25y(self):
        mast_25y, total = lease_25_years(test_data, test_header)
        self.assertEqual(mast_25y[0][0], 'Seacroft Gate (Chase) - Block 2')
        self.assertEqual(len(mast_25y), 3)


if __name__ == '__main__':
    unittest.main()