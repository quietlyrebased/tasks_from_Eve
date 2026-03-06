def caesar_cipher(text, shift):
    """Шифрует/расшифровывает текст с использованием шифра Цезаря."""
    result = []
    
    for letter in text:
        if letter.isalpha():

            if letter.isupper():
                start = ord('A')
            else:
                start = ord('a')
            
            code = ord(letter)
            shifted = (code - start + shift) % 26 + start
            
            result.append(chr(shifted))
        else:
            result.append(letter)
    
    return ''.join(result)

text = input("Введите текст: ")
shift = int(input("Введите сдвиг (чтобы расшифровать - отрицательный): "))

encrypted = caesar_cipher(text, shift)

print(f"\nРезультат: {encrypted}")