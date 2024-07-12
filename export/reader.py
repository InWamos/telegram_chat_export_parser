import os

def get_html_content(path: str) -> str:
    with open(f"target/{path}", "r") as html_file:
        return html_file.read()
    
def get_all_target_files() -> list[str]:
    files = os.listdir("./target")

    return files