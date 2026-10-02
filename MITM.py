intercepted_packets = [
    "Alice |Charlie |150 |20",
    "Alice |Bob     |500 |42", 
    "Dave  |Eve     |50  |78"
]

def calculate_checksum(data_string):
    """
    Банк считает контрольную сумму так:
    Сумма ASCII-кодов всех символов строки по модулю 100.
    """
    total = 0
    for char in data_string:
        total += ord(char)
    return total % 100

def mitm_attack(packets):
    modified_packets = []
    
    for packet in packets:
        
        parts = [p.strip() for p in packet.split('|')]
        sender = parts[0]
        receiver = parts[1]
        amount = parts[2]

        # Ищем пакет, адресованный "Bob"
        if receiver == "Bob":
            #  Подменяем получателя и сумму
            new_receiver = "Hacker"
            new_amount = "9999"
            
        
            new_data = f"{sender} |{new_receiver} |{new_amount}"
            
      
            new_checksum = calculate_checksum(new_data)

            final_packet = f"{new_data} |{new_checksum}"
            modified_packets.append(final_packet)
        else:
            modified_packets.append(packet)
            
    return modified_packets

hacked_packets = mitm_attack(intercepted_packets)

print("Пакеты после атаки MITM:")
for p in hacked_packets:
    print(p)


def bank_receive(packet):
    parts = packet.split('|')

    data = parts[0].strip() + " |" + parts[1].strip() + " |" + parts[2].strip()
    received_checksum = int(parts[3])
    expected_checksum = calculate_checksum(data)
    
    print(f"Получен пакет: {packet}")
    if received_checksum == expected_checksum:
        print("✅ БАНК: Транзакция одобрена! Целостность подтверждена.\n")
    else:
        print(f"❌ БАНК: ТРЕВОГА! Ожидалась сумма {expected_checksum}, а пришла {received_checksum}.")
        print("❌ БАНК: Пакет отброшен (MITM Атака заблокирована!)\n")

print("\n--- ОТПРАВКА ПАКЕТОВ В БАНК ---")
for p in hacked_packets:
    bank_receive(p)