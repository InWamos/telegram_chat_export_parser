from export import parser, reader, writer


def main() -> None:
    files = reader.get_all_target_files()
    i = 0

    if files:
        for file in files:
            i += 1
            content = reader.get_html_content(file)
            messages = parser.find_all_messages(content)
            writer.append_messages_to_csv(messages)
            print(f"File no {i}/{len(files)}")

if __name__ == "__main__":
    main()