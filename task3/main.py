import sys

from logs_handlers import (
    load_logs,
    filter_logs_by_level,
    count_logs_by_level,
    display_log_counts,
)


def main():
    # Check if enetered additional arguments from command line
    if len(sys.argv) > 1:
        path_to_logs = sys.argv[1]
        try:
            logs_list = load_logs(path_to_logs)
        except:
            FileNotFoundError
            print(f"Error: File '{path_to_logs}' not found.")
            sys.exit(1)

        # Calculates and display results of lines quantity for each level
        error_counts = count_logs_by_level(logs_list)
        display_log_counts(error_counts)

        # Display all lines for a level if it was specified in command line
        if len(sys.argv) > 2:
            level = sys.argv[2]
            filtered_logs = filter_logs_by_level(logs_list, level)
            print(f"Деталі логів для рівня '{level.upper()}':")
            for logs in filtered_logs:
                print(f"{logs['data']} {logs['time']} - {logs['message']}")
    else:
        print("Usage: main.py <path_to_logs> <level>")


if __name__ == "__main__":
    main()
