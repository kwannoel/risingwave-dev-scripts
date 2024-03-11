#!/usr/bin/env python3

# Usage: ./wide_table.py create NUMBER-OF-COLUMNS > create.sql
# Usage: ./wide_table.py insert NUMBER-OF-COLUMNS NUMBER-OF-ROWS > insert.sql

import sys


def create(columns):
    print("CREATE TABLE t (")
    for i in range(1, columns):
        print(f"  v{i} INT,")
    print(f"  v{columns} INT")
    print(");")


def insert(columns, rows):
    print("INSERT INTO t VALUES")
    for i in range(1, rows):
        print(f"  ({', '.join([str(j) for j in range(1, columns + 1)])}),")
    print(f"  ({', '.join([str(j) for j in range(1, columns + 1)])});")


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} create NUMBER-OF-COLUMNS > create.sql")
        print(f"Usage: {sys.argv[0]} insert NUMBER-OF-COLUMNS NUMBER-OF-ROWS > insert.sql")
        sys.exit(1)

    if sys.argv[1] == "create":
        create(int(sys.argv[2]))
        return
    if sys.argv[1] == "insert":
        insert(int(sys.argv[2]), int(sys.argv[3]))
        return


if __name__ == "__main__":
    main()
