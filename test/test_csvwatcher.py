import os
import time
from unittest.mock import patch, Mock

from pyfakefs.fake_filesystem_unittest import TestCase

from csvwatcher import CsvWatcher, Handler
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

    # def test_init2(self):
    #     cb = Mock()
    #     w = CsvWatcher("/tmp", cb)
    #     w.run()
    #
    #     file_path = '/tmp/file.csv'
    #     self.assertFalse(os.path.exists(file_path))
    #     self.fs.create_file(file_path)
    #     self.assertTrue(os.path.exists(file_path))
    #     cb.assert_called_with(file_path)
    #     w.canRun = False

    # def test_handle_xr(self):
    #     cb = Mock()
    #     event_handler = Handler(cb)
    #     observer = Observer()
    #
    #     self.fs.create_dir('/tmp')
    #     observer.schedule(event_handler, '/tmp', recursive=False)
    #     observer.start()
    #
    #     file_path = '/tmp/file.csv'
    #     file_path2 = '/tmp/file.csvx'
    #     self.fs.create_file(file_path)
    #     self.assertTrue(os.path.exists(file_path))
    #     # cb.assert_called_with(file_path)
    #     event = FileCreatedEvent(file_path)
    #     event2 = FileCreatedEvent(file_path2)
    #     event_handler.on_created(event)
    #     cb.assert_called_once_with(event)
    #     cb.reset_mock()
    #     event_handler.on_created(event2)
    #     cb.assert_not_called()
    #     observer.stop()

    def test_handler(self):
        callback = Mock()
        event_handler = Handler(callback)

        event = FileCreatedEvent('/tmp/file.csv')
        event_handler.on_created(event)
        callback.assert_called_once_with(event)
        callback.reset_mock()

        event2 = FileCreatedEvent('/tmp/file.csvx')
        event_handler.on_created(event2)
        callback.assert_not_called()
        callback.reset_mock()

        event3 = DirCreatedEvent('/tmp/x')
        event_handler.on_created(event3)
        callback.assert_not_called()

