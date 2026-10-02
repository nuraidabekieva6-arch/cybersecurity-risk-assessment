import pandas as pd

# 1. Структура хранения данных (Задание 1)
variant_1 = {
    "asset": "База данных студентов",
    "A": 2000000,
    "K": 5,
    "threats": [
        {"name": "Фишинг", "P": 0.6, "V": 4, "I": 0.7},
        {"name": "SQL-инъекция", "P": 0.4, "V": 5, "I": 0.9},
        {"name": "Ошибка администратора", "P": 0.5, "V": 3, "I": 0.6}
    ]
}

# Определение контрмер (Задание 5)
countermeasures = {
    "Обучение персонала": {"target": "Фишинг", "P_reduction": 0.2}, # -20% к вероятности
    "Обновление ПО (WAF)": {"target": "SQL-инъекция", "V_reduction": 0.4}, # -40% к уязвимости
    "Резервное копирование": {"target": "Ошибка администратора", "I_reduction": 0.5} # -50% к ущербу
}

def calculate_risk_val(A, P, V, I, K):
    # Формула R = A * P * V * I * K
    return A * P * V * I * K

results = []

# 2. Расчет базового и остаточного риска
for threat in variant_1["threats"]:
    # Базовый расчет
    base_r = calculate_risk_val(variant_1["A"], threat["P"], threat["V"], threat["I"], variant_1["K"])
    
    # Применение контрмер
    p_res, v_res, i_res = threat["P"], threat["V"], threat["I"]
    
    for cm_name, cm_data in countermeasures.items():
        if cm_data["target"] == threat["name"]:
            p_res *= (1 - cm_data.get("P_reduction", 0))
            v_res *= (1 - cm_data.get("V_reduction", 0))
            i_res *= (1 - cm_data.get("I_reduction", 0))
            
    resid_r = calculate_risk_val(variant_1["A"], p_res, v_res, i_res, variant_1["K"])
    
    # 4. Определение категории (нормализация относительно максимума)
    # Для простоты: всё что выше 10 млн - Критический, выше 5 - Высокий
    category = "Критический" if base_r > 10000000 else "Высокий" if base_r > 5000000 else "Средний"
    
    results.append({
        "Угроза": threat["name"],
        "Базовый риск": base_r,
        "Остаточный риск": resid_r,
        "Категория": category,
        "Снижение %": round((1 - resid_r/base_r)*100, 1)
    })

# 3. Сортировка по убыванию
df = pd.DataFrame(results).sort_values(by="Базовый риск", ascending=False)

print("--- ТАБЛИЦА РИСКОВ (ВАРИАНТ 1) ---")
print(df.to_string(index=False))

print("\n--- ТОП-3 КРИТИЧЕСКИХ УГРОЗ ---")
print(df["Угроза"].head(3).tolist())