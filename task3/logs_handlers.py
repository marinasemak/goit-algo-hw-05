from collections import Counter


def parse_log_line(line: str) -> dict:
    """
    Parse line from logs and converts it into dictionary
    """
    components_names = ["data", "time", "level", "message"]
    line_list = line.strip().split(maxsplit=3)
    components = dict(zip(components_names, line_list))
    return components


def load_logs(file_path: str) -> list:
    """
    Opens log file
    """
    with open(file_path, "r", encoding="utf-8") as fh:
        parsed_logs = [parse_log_line(line) for line in fh.readlines()]
    return parsed_logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filter logs according to specified level
    """
    level = level.upper()

    def contains_level(log, level):
        return any(level in value for value in log.values())

    return list(filter(lambda log: contains_level(log, level), logs))


def count_logs_by_level(logs: list) -> dict:
    """
    Calculates quantity of lines for each logs level
    """
    levels = [log["level"] for log in logs if "level" in log]
    return dict(Counter(levels))


def display_log_counts(counts: dict):
    """
    Format and display result
    """
    # Print the names of the columns.
    print("{:<20} {:<10}".format("Рівень логування", "Кількість"))

    # print each data item.
    for item in counts.items():
        level, qnty = item
        print("{:<20} {:<10}".format(level, qnty))
