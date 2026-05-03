from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    lines = open(path, 'r').read().split('\n')
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\\\')
        if '/' in file or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    template_start = '{"English":"'
    template_mid = '","German":"'
    template_end = '"}'

    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file)
        json_line = template_start + english_file + template_mid + german_file + template_end
        processed_file_list.append(json_line)
    return processed_file_list

def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each on a new line"""
    with open(path, 'w') as f:
        for line in file_list:
            f.write(line + '\n')

def main():
    english_lines = path_to_file_list('english.txt')
    german_lines = path_to_file_list('german.txt')
    json_lines = train_file_list_to_json(english_lines, german_lines)
    write_file_list(json_lines, 'concated.json')

if __name__ == "__main__":
    main()
