def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    actual_shift = shift if mode == 'encrypt' else -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + actual_shift) % 26)
            result += new_char
        else:
            result += char
    return result
def main():
    print("Система защиты данных MedicalCard")
    user_password = input("Введите ваш пароль: ")
    shift_key = 9
    encrypted = caesar_cipher(user_password, shift_key, 'encrypt')
    print(f"Зашифрованный вид: {encrypted}")
    decrypted = caesar_cipher(encrypted, shift_key, 'decrypt')
    print(f"Расшифрованный вид: {decrypted}")
if __name__ == "__main__":
    main()