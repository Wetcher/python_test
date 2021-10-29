import xml.etree.ElementTree as ElementTree
from interval import Interval
import sys
import os

script_name, read_file = sys.argv
root = ElementTree.parse(os.getcwd() + '/' + read_file).getroot()

silence_intervals = []
for silence in root.findall('silence'):
    silence_from = silence.attrib.get('from')
    silence_to = silence.attrib.get('until')
    silence_intervals.append(Interval(silence_from, silence_to))

parts = []
start_part_interval = 'PT0M0S'
end_part_interval = None
for silence_interval in silence_intervals:
    end_part_interval = silence_interval.start
    parts.append(Interval(start_part_interval, end_part_interval))
    start_part_interval = silence_interval.end
last_interval = silence_intervals[-1]
parts.append(Interval(last_interval.end, None))

print(parts)
