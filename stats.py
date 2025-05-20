
def get_num_words(text:str) -> int:
    return len(text.split())

def get_chars(text:str) -> dict:
    new_dict = {}
    for char in text:
        char = char.lower()
        new_dict[char] = new_dict.get(char, 0) + 1
    return sorted_dict(new_dict)

def sorted_dict(new_dict: dict)-> dict:
    return dict(sorted(new_dict.items(), key=lambda num: num[1], reverse = True))