from peewee import TimestampField, BigIntegerField
import datetime
import calendar
import time


class CustomTimestampField(TimestampField):

    def db_value(self, value):

        if value is None:
            return

        if isinstance(value, datetime.datetime):
            pass
        elif isinstance(value, datetime.date):

            value -= (datetime.datetime(2001, 1, 2, 0, 0, 0) - datetime.datetime.fromtimestamp(0))
            value = datetime.datetime(value.year, value.month, value.day)
        else:
            return int(round(value * self.resolution))

        if self.utc:
            timestamp = calendar.timegm(value.utctimetuple())
        else:
            timestamp = time.mktime(value.timetuple())
        timestamp += (value.microsecond * .000001)
        if self.resolution > 1:
            timestamp *= self.resolution
        return int(round(timestamp))

    def python_value(self, value):
        if value is not None and isinstance(value, (int, float, int)):
            if value == 0:
                return
            elif self.resolution > 1:
                value, microseconds = divmod(value, self.resolution)
                value += (datetime.datetime(2001, 1, 1, 0, 0, 0) - datetime.datetime.fromtimestamp(0)).total_seconds()
                return self._conv(value).replace(microsecond=microseconds)
            else:
                value += (datetime.datetime(2001, 1, 1, 0, 0, 0) - datetime.datetime.fromtimestamp(0)).total_seconds()
                return self._conv(value)
        return value
