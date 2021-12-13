import os
import time
from unittest.mock import patch, Mock

from pyfakefs.fake_filesystem_unittest import TestCase

from csv_watcher import CsvWatcher, Handler
from watchdog.observers import Observer
from watchdog.events import FileCreatedEvent, DirCreatedEvent


class TestCsvWatcher(TestCase):

    def setUp(self):
        self.setUpPyfakefs()

    # patch sleep to allow loop to exit
    @patch("time.sleep", side_effect=InterruptedError)
    def test_state_reset(self, mocked_sleep):
        cb = Mock()
        w = CsvWatcher("/tmp", cb)
        w.run()
        self.assertFalse(w.running)

    def test_init(self):
        w = CsvWatcher("/tmp", lambda x: print(x))
        self.assertEqual('/tmp', w.directory)

    def test_handler(self):
        callback = Mock()
        event_handler = Handler(callback)

        event = FileCreatedEvent('/tmp/file.csv')
        event_handler.on_created(event)
        callback.assert_called_once_with(event.src_path)
        callback.reset_mock()

        event2 = FileCreatedEvent('/tmp/file.csvx')
        event_handler.on_created(event2)
        callback.assert_not_called()
        callback.reset_mock()

        event3 = DirCreatedEvent('/tmp/x')
        event_handler.on_created(event3)
        callback.assert_not_called()
