# ОБЩИЕ НАСТРОЙКИ (Алфавит для обоих заданий)
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ЗАДАНИЕ №1: РЕАЛИЗАЦИЯ ШИФРА ВИЖЕНЕРА
# Суть: Сдвиг каждой буквы зависит от буквы ключевого слова.
def vigenere_encrypt(text, key):
    encrypted_text = ""
    text = text.upper()
    key = key.upper()
    key_index = 0

    for char in text:
        if char in ALPHABET:
            # 1. Находим индекс буквы текста
            text_idx = ALPHABET.index(char)
            # 2. Находим индекс буквы ключа (используем текущий key_index)
            key_char = key[key_index]
            key_idx = ALPHABET.index(key_char)
            


            # 3. Складываем индексы и берем остаток от деления на 26
            new_idx = (text_idx + key_idx) % 26
            
            # 4. Находим новую букву и добавляем в результат

            encrypted_text += ALPHABET[new_idx]
            
            # 5. Сдвигаем индекс ключа. Если ключ кончился — начинаем сначала (% len(key))
            key_index = (key_index + 1) % len(key)
        else:
            # Пробелы и знаки препинания не шифруем
            encrypted_text += char
            
    return encrypted_text


# ЗАДАНИЕ №2: ВЗЛОМ ШИФРА ЦЕЗАРЯ (BRUTE-FORCE)
# Суть: Перебор всех 25 вариантов сдвига, чтобы найти текст.

def brute_force_caesar(ciphertext):
    print("\n" + "="*50)
    print("ЗАПУСК ВЗЛОМА ШИФРА ЦЕЗАРЯ (МЕТОД BRUTE-FORCE)")
    print("="*50)
    
    # Цикл перебирает все возможные ключи (shift) от 1 до 25
    for shift in range(1, 26):
        decrypted_text = ""
        
        for char in ciphertext.upper():
            if char in ALPHABET:
                # Находим текущий индекс и сдвигаем НАЗАД на текущий shift
                idx = ALPHABET.index(char)
                new_idx = (idx - shift) % 26
                decrypted_text += ALPHABET[new_idx]
            else:
                # Символы оставляем как есть
                decrypted_text += char
        
        # Печатаем результат для каждого ключа
        print(f"Ключ {shift:2}: {decrypted_text}")



# БЛОК ЗАПУСКА (ТО, ЧТО ВЫВОДИТСЯ В ТЕРМИНАЛ)

if __name__ == "__main__":
   #  1
    print("="*50)
    print("РЕЗУЛЬТАТ ЗАДАНИЯ №1 (ШИФР ВИЖЕНЕРА)")
    print("="*50)
    
    secret_message = "CYBERSECURITY IS AWESOME"
    secret_key = "IITU"
    result_vigenere = vigenere_encrypt(secret_message, secret_key)
    
    print(f"Оригинал: {secret_message}")
    print(f"Ключ:     {secret_key}")
    print(f"Шифр:     {result_vigenere}")

    #  2 
    intercepted_message = "KYV JVTIVK G/JJNFIU ZJ: UZJRJ-YRTBVI-99"
    brute_force_caesar(intercepted_message)
    
    print("\n" + "="*50)
    print("")
    print("="*50)