import unittest

from entity import Entity


class TestEntity(unittest.TestCase):
    expected_json = '{"_date": "2019-08-10T21:27:17Z", "_event_type": "incoming", "_item_number": 12312, ' \
                    '"_store_number": 10, "_transaction_id": "188be094-0ba6-4fb1-b752-310a9808b229", "_value": 23, ' \
                    '"valid": true}'

    def test_init(self):
        e = Entity('188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2019-08-10T21:27:17Z', 10, 12312, 23)
        self.assertEqual('188be094-0ba6-4fb1-b752-310a9808b229', e.transaction_id)
        self.assertEqual('incoming', e.event_type)
        self.assertEqual('2019-08-10T21:27:17Z', e.date)
        self.assertEqual(10, e.store_number)
        self.assertEqual(12312, e.item_number)
        self.assertEqual(23, e.value)

    def test_wrong_transaction_id(self):
        self.assertRaises(Exception, Entity, 'x', 'incoming', '2021-11-01', 10, 12312, 23)

    def test_wrong_date(self):
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-x1', 10,
                          12312,
                          23)

    def test_wrong_event_type(self):
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'x', '2021-11-01', 10, 12312,
                          23)

    def test_wrong_store_id(self):
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-01', 'q',
                          12312, 23)

    def test_negative_store_id(self):
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-01', -12,
                          12312, 23)

    def test_wrong_item_id(self):
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-01', 2, 'qw',
                          23)

    def test_negative_item_id(self):
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-01', 2, 'qw',
                          23)

    def test_wrong_value(self):
        self.assertRaises(ValueError, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-01', 23,
                          12312, 'a')

    def test_negative_value(self):
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-01', 23,
                          12312, -12)

    def test_to_json(self):
        e = Entity('188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2019-08-10T21:27:17Z', 10, 12312, 23)
        self.assertEqual(self.expected_json, e.to_json())


if __name__ == '__main__':
    unittest.main()
