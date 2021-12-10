import logging
from typing import Callable

from csv import DictReader
from entity import Entity


def process_csv(filename: str, callback: Callable):
    """Process a csv file.

    Returns:
        None
    """
    try:
        with open(filename, 'r') as read_obj:
            # pass the file object to DictReader() to get the DictReader object
            csv_dict_reader = DictReader(read_obj)
            # iterate over each line as an ordered dictionary
            for row in csv_dict_reader:
                try:
                    # row variable is a dictionary that represents a row in csv
                    try:
                        e = Entity(row['transaction_id'], row['event_type'], row['date'], row['store_number'],
                                   row['item_number'],
                                   row['value'])
                        callback(e)
                    except KeyError as v:
                        logging.warning(v)
                        raise KeyError("invalid row format in csv")
                except ValueError as v:
                    logging.warning(v)
    except FileNotFoundError as e:
        logging.warning(e)
        raise e
