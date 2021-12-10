import json
import uuid
from datetime import datetime


class Entity:

    def __init__(self, transaction_id: str, event_type: str, date: str, store_number: int   , item_number: int, value: int):
        self.transaction_id = transaction_id
        self.event_type = event_type
        self.date = date
        self.store_number = int(store_number)
        self.item_number = int(item_number)
        self.value = int(value)
        self.valid = True

    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        try:
            uuid.UUID(value)
            self._transaction_id = value
        except ValueError:
            raise ValueError("Invalid transaction_id format")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        date_format = "%Y-%m-%d"
        try:
            datetime.fromisoformat(value[:-1])
            self._date = value
        except ValueError:
            raise ValueError("Invalid date format")

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        if value == 'incoming' or value == 'sale':
            self._event_type = value
        else:
            raise ValueError("Invalid event_type format")

    @property
    def store_number(self):
        return self._store_number

    @store_number.setter
    def store_number(self, value):
        if value < 0:
            raise ValueError("Invalid store_number format")
        self._store_number = value

    @property
    def item_number(self):
        return self._item_number

    @item_number.setter
    def item_number(self, value):
        if value < 0:
            raise ValueError("Invalid item_number format")
        self._item_number = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError("Invalid value format")
        self._value = value

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)
