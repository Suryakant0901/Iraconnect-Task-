def solution(input_str):
    text = input_str.strip()
    if text == "":
        return ""
    return text[0].upper() + text[1:].lower()
