#!/usr/bin/python3
"""
log parsing
"""

import sys

if __name__ == '__main__':

    totalsize = 0
    line_count = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, total_size: int) -> None:
        """
        Method that takes in stats and total size as args
        """
        print("File size: {:d}".format(totalsize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))
    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                totalsize += int(data[-1])
            except BaseException:
                pass
            if line_count % 10 == 0:
                print_stats(stats, totalsize)
    except KeyboardInterrupt:
        print_stats(stats, totalsize)
        raise
