import re

class Interval:
    start: str
    end: str
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def getStartMs(self):
        return self.intervalToMilliseconds(self.start)
    def getEndMs(self):
        return self.intervalToMilliseconds(self.end)
    def __repr__(self):
        first_part = ('NONE' if isinstance(self.start, type(None)) else self.start)
        second_part = ('NONE' if isinstance(self.end, type(None)) else self.end)
        return first_part + '-' + second_part
    def intervalToMilliseconds(interval_str: str):
        groups = re.search('([0-9]+)M([0-9]+.?[0-9]*)S', interval_str)
        minutes = int(groups.group(1)) * 60 * 1000
        seconds = int(float(groups.group(2)) * 1000)
        return minutes + seconds