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
            rowNumber = 0
            # iterate over each line as an ordered dictionary
            for row in csv_dict_reader:
                rowNumber += 1
                try:
                    # row variable is a dictionary that represents a row in csv
                    try:
                        e = Entity(row['transaction_id'], row['event_type'], row['date'], row['store_number'],
                                   row['item_number'],
                                   row['value'])
                        callback(e)
                    except KeyError as v:
                        logging.warning(v)
                        raise KeyError(f"invalid format in row {rowNumber}")
                except ValueError as v:
                    logging.warning(f"invalid format in row {rowNumber} ({v})")
                    raise ValueError(f"invalid value in row {rowNumber}")
    except FileNotFoundError as e:
        logging.warning(e)
        raise e
