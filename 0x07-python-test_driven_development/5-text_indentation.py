def text_indentation(text):
    punctuation_marks = ['.', '?', ':']
    new_text = ""
    current_line = ""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for char in text:
        if char in punctuation_marks:
            new_text += current_line.strip() + '\n\n'
            current_line = ""
        else:
            current_line += char
    new_text += current_line.strip()
    print(new_text)
