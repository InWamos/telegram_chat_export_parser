import csv


def append_messages_to_csv(messages: list[str]) -> None:
    with open("./output.csv", "a", newline="", encoding="utf-8") as csv_file:
        for message in messages:
            writer = csv.writer(csv_file)
            writer.writerow([message])
