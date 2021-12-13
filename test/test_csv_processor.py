import unittest
from unittest.mock import Mock, patch

from pyfakefs.fake_filesystem_unittest import TestCase

from csv_processor import process_csv


class TestCsProcessor(TestCase):
    valid_csv = 'transaction_id,event_type,date,store_number,item_number,value\n7c71fb42-1f5e-45e1-be16-7d4d772d1aab,' \
                'sale,2018-12-03T23:57:40Z,9,8,116 '
    invalid_csv = 'transaction_id,event_type,date,store_number,item_number,value\ninvalid,' \
                  'sale,2018-12-03T23:57:40Z,9,8,116 '
    invalid_row_format = 'header\nx,sale,2018-12-03T23:57:40Z,9,8,116'

    def setUp(self):
        self.setUpPyfakefs()
        self.callback = Mock()

    def test_valid_csv(self):
        file_path = '/tmp/file.csv'
        self.fs.create_file(
            file_path,
            contents=self.valid_csv
        )
        process_csv(file_path, self.callback)
        self.callback.assert_called_once()

    def test_invalid_row_format_in_csv(self):
        file_path = '/tmp/file.csv'
        self.fs.create_file(
            file_path,
            contents=self.invalid_row_format
        )
        n = process_csv(file_path, self.callback)
        self.assertEqual(0, n)

    def mock_func(*args, **kwargs):
        raise ValueError

    @patch('entity.Entity.__init__', mock_func)
    def test_invalid_csv(self):
        file_path = '/tmp/file.csv'
        self.fs.create_file(
            file_path,
            contents=self.invalid_csv
        )
        n = process_csv(file_path, self.callback)
        self.assertEqual(0, n)

    def test_wrong_csv_path(self):
        file_path = '/tmp/wrong.csv'
        n = process_csv(file_path, self.callback)
        self.assertIsNone(n)


if __name__ == '__main__':
    unittest.main()
