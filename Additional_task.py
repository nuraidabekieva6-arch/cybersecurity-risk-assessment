def xor_chiper(text, key):
    result = ""    
    for char in text:
       encrypted_char = chr(ord(char) ^ key)
       result += encrypted_char
       return result
    secret_data = "PROJECT_ALPHA_v2_FINAL_BLUEPRINTS"
    encrypted_key = 42
    encrypted = xor_cipher(secret_data, encrypted_key)
    print(f"Зашифрованный вид: {encrypted}")
    decrypted = xor_cipher(encrypted, encrypted_key)
    print(f"Восстановленные данные: {decrypted}")
    assert secret_data == decrypted, "Ошибка: данные не совпадают!"
