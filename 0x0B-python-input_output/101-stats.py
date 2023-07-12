#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys
from collections import defaultdict


def print_statistics(total_size, status_counts):
    """
    function named print_statistics to print the computed metrics
    """
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        print(f"{status_code}: {count}")


def process_input():
    """
    function named process_input to read input, compute metrics
    and print statistics
    """
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) >= 6:
                size = int(parts[-1])
                status_code = parts[-2]
                total_size += size
                status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    process_input()
