"""Suppport for Clickhouse data sources."""

import attr
from .core import Target


@attr.s
class ClickhouseTarget(Target):
    query = attr.ib(default=None)
    database = attr.ib(default=None)
    table = attr.ib(default=None)
    date = attr.ib(default=None)
    timestamp = attr.ib(default="timestamp")

    def to_json_data(self):
        params = {
            "query": self.query,
        }

        if self.database is not None:
            params["database"] = self.database
        if self.table is not None:
            params["table"] = self.table
        if self.date is not None:
            params["dateColDataType"] = self.date
        if self.timestamp is not None:
            params["dateTimeColDataType"] = self.timestamp
        return params
