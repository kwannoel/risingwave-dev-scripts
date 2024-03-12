#!/usr/bin/env python3

# Usage: ./wide_table.py

import sys
import random


def create(columns):
    print("CREATE TABLE t (")
    for i in range(1, columns+1):
        print(f"  v{i} varchar,")
    # Make first 50% of them PKs.
    pks = [f"v{i}" for i in range(1, columns//2 + 1)]
    print(f"  PRIMARY KEY ({', '.join(pks)}),")
    print(");")

def insert(columns, rows):
    print("INSERT INTO t VALUES")
    for i in range(1, rows):
        s = ', '.join([f"'padpadpadpadpadpadpadpadpadpad{random.randint(1, 100000)}'" for j in range(1, columns + 1)])
        print(f"  ({s}),")
    s = ', '.join([f"'padpadpadpadpadpadpadpadpadpad{random.randint(1, 100000)}'" for j in range(1, columns + 1)])
    print(f"  ({s});")

def query(scan_range_len):
    # Always just query v1 / v2.
    # Generate scan ranges
    scan_strings = []
    for i in range(scan_range_len):
        # generate a string with length 45
        s = "0" * 40 + str(random.randint(1, 10000))
        scan_strings.append(s)
    print("SELECT * FROM t WHERE")
    print("  v2 IN (")
    print(", ".join([f"'{s}'" for s in scan_strings]))
    print(") AND")
    print("  v1 IN (")
    print(", ".join([f"'{s}'" for s in scan_strings]))
    print(");")

def filter_query(scan_range_len):
    scan_strings = []
    for i in range(scan_range_len):
        # generate a string with length 45
        s = "0" * 40 + str(random.randint(1, 10000))
        scan_strings.append(s)
        print("SELECT * FROM t WHERE")
        print("  v1 IN (")
        print(", ".join([f"'{s}'" for s in scan_strings]))
        print(");")


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} create NUMBER-OF-COLUMNS > create.sql")
        print(f"Usage: {sys.argv[0]} insert NUMBER-OF-COLUMNS NUMBER-OF-ROWS > insert.sql")
        print(f"Usage: {sys.argv[0]} query SCAN-RANGE-LEN > query.sql")
        print(f"Usage: {sys.argv[0]} filter_query SCAN-RANGE-LEN > filter_query.sql")
        sys.exit(1)

    if sys.argv[1] == "create":
        create(int(sys.argv[2]))
        return
    if sys.argv[1] == "insert":
        insert(int(sys.argv[2]), int(sys.argv[3]))
        return
    if sys.argv[1] == "query":
        query(int(sys.argv[2]))
        return
    if sys.argv[1] == "filter_query":
        filter_query(int(sys.argv[2]))
        return


if __name__ == "__main__":
    main()
