import unittest

from entity import Entity


class TestEntity(unittest.TestCase):
    def test_init(self):
        e = Entity('188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2019-08-10T21:27:17Z', 10, 12312, 23)
        self.assertEqual('188be094-0ba6-4fb1-b752-310a9808b229', e.transaction_id)
        self.assertEqual('incoming', e.event_type)
        self.assertEqual('2019-08-10T21:27:17Z', e.date)
        self.assertEqual(10, e.store_number)
        self.assertEqual(12312, e.item_number)
        self.assertEqual(23, e.value)

    def test_wrong_transaction_id(self):
        foo = 2
        self.assertRaises(Exception, Entity, 'x', 'incoming', '2021-11-01', 10, 12312, 23)

    def test_wrong_date(self):
        foo = 2
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-x1', 10,
                          12312,
                          23)

    def test_wrong_event_type(self):
        foo = 2
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'x', '2021-11-01', 10, 12312,
                          23)

    def test_wrong_store_id(self):
        foo = 2
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-01', 'q',
                          12312, 23)

    def test_negative_store_id(self):
        foo = 2
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-01', -12,
                          12312, 23)

    def test_wrong_item_id(self):
        foo = 2
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-01', 2, 'qw',
                          23)

    def test_negative_item_id(self):
        foo = 2
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-01', 2, 'qw',
                          23)

    def test_wrong_value(self):
        foo = 2
        self.assertRaises(ValueError, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-01', 23,
                          12312, 'a')

    def test_negative_value(self):
        foo = 2
        self.assertRaises(Exception, Entity, '188be094-0ba6-4fb1-b752-310a9808b229', 'incoming', '2021-11-01', 23,
                          12312, -12)


if __name__ == '__main__':
    unittest.main()
