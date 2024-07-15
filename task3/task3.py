from pathlib import Path
import sys
from collections import Counter


path_to_logs = Path("task3/logs.txt")

# for arg in sys.argv:
# path_to_logs = sys.argv[1]
# print(path_to_logs)


def parse_log_line(line: str) -> dict:
    components_names = ["data", "time", "level", "message"]
    line_list = line.split(maxsplit=3)
    components = dict(zip(components_names, line_list))
    return components


def load_logs(file_path: str) -> list:

    with open(file_path, "r", encoding="utf-8") as fh:
        parsed_logs = [parse_log_line(line) for line in fh.readlines()]
        # for line in fh:
        #     parse_log_line(line)
        # print(parsed_logs)
    return parsed_logs


def filter_logs_by_level(logs: list, level: str) -> list:
    def contains_level(log, level):
        return any(level in value for value in log.values())

    filtered_logs = list(filter(lambda log: contains_level(log, level), logs))
    print(filtered_logs)
    return filtered_logs


def count_logs_by_level(logs: list) -> dict:
    levels = [log["level"] for log in logs if "level" in log]
    counts = dict(Counter(levels))
    # print(level_quantities)
    print(counts)
    return counts


def display_log_counts(counts: dict):
    # Print the names of the columns.
    print("{:<20} {:<10}".format("Рівень логування", "Кількість"))

    # print each data item.
    for item in counts.items():
        level, qnty = item
        print("{:<20} {:<10}".format(level, qnty))


list_logs = load_logs(path_to_logs)
filter_logs_by_level(list_logs, "INFO")
d = count_logs_by_level(list_logs)
display_log_counts(d)

#  2024-01-22 13:30:30 INFO Scheduled maintenance.
# python [main.py](<http://main.py/>) /path/to/logfile.log


"""Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1"""

# python main.py path/to/logfile.log error

"""
    Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1

Деталі логів для рівня 'ERROR':
2024-01-22 09:00:45 - Database connection failed.
2024-01-22 11:30:15 - Backup process failed.

    """
