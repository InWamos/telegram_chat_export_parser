from bs4 import BeautifulSoup


def find_all_messages(file_content: str) -> list[str]:
    soup = BeautifulSoup(file_content, "html.parser")
    all_messages_fields = soup.find_all(class_="text")
    messages = list(message.get_text(strip=True) for message in all_messages_fields)

    return messages[1:]
