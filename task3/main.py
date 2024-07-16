
import sys

from logs_handlers import load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts


# path_to_logs = Path("task3/logs.txt")


# for arg in sys.argv:
#     path_to_logs = sys.argv[1]
#     level = sys.argv[2]
# print(path_to_logs)

# list_logs = load_logs(path_to_logs)
# print(filter_logs_by_level(list_logs, level))

# d = count_logs_by_level(list_logs)
# display_log_counts(d)


def main():
    if len(sys.argv) > 1:
        path_to_logs = sys.argv[1]
        logs_list = load_logs(path_to_logs)

        error_counts = count_logs_by_level(logs_list)
        display_log_counts(error_counts)
        if len(sys.argv) > 2:
            level = sys.argv[2]
            filtered_logs = filter_logs_by_level(logs_list, level)
            print(f"Деталі логів для рівня '{level.upper()}':")
            for logs in filtered_logs:
                print(
                    f"{logs['data']} {logs['time']} - {logs['message']}", end="")


if __name__ == "__main__":
    main()

"""Рівень логування | Кількість
-----------------|----------
INFO             | 4
DEBUG            | 3
ERROR            | 2
WARNING          | 1"""

# python main.py path/to/logfile.log error
# [{'data': '2024-01-22', 'time': '09:00:45', 'level': 'ERROR', 'message': 'Database connection failed.\n'}, {'data': '2024-01-22', 'time': '11:30:15', 'level': 'ERROR', 'message': 'Backup process failed.\n'}]

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
