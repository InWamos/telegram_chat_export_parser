from export import parser, reader


def main() -> None:
    files = reader.get_all_target_files()
    i = 0

    if files:
        for file in files:
            i += 1
            content = reader.get_html_content(file)
            parser.find_all_messages(content)
            print(f"File no {i}/{len(files)}")

if __name__ == "__main__":
    main()