import csv

def read_csv(path: str) -> list:
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)


def write_csv(path: str, rows: list):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def read_csv_as_dict(path: str) -> list:
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
