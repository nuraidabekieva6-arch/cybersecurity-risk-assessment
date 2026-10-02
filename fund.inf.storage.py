import json
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class RiskManagementSystem:
    def __init__(self):
        self.assets = [
            {"name": "Сервер БД", "value": 5000000, "criticality": 5, "type": "Сервер"},
            {"name": "Локальная сеть", "value": 1000000, "criticality": 3, "type": "Сеть"},
            {"name": "Рабочие станции", "value": 2000000, "criticality": 2, "type": "ПК"}
        ]
        self.threats = [
            {"name": "Фишинг", "prob": 0.8, "impact_coeff": 0.6, "type": "Внешняя"},
            {"name": "Вирусная атака", "prob": 0.5, "impact_coeff": 0.7, "type": "Внешняя"},
            {"name": "Отказ оборудования", "prob": 0.2, "impact_coeff": 0.9, "type": "Техногенная"}
        ]
        self.vulnerability_level = 4  # V в формуле (Задание 2)

        self.countermeasures = {
            "Firewall": {"prob_red": 0.3, "vuln_red": 0.0, "imp_red": 0.0},
            "Patching": {"prob_red": 0.0, "vuln_red": 0.4, "imp_red": 0.0},
            "Backup": {"prob_red": 0.0, "vuln_red": 0.0, "imp_red": 0.5}
        }

    def calculate_risk(self, asset, threat, v_level, measures=None):
        # R = A * P * V * I * K
        A = asset['value']
        P = threat['prob']
        V = v_level
        I = threat['impact_coeff']
        K = asset['criticality']

        if measures:
            for m_name in measures:
                m = self.countermeasures[m_name]
                P *= (1 - m['prob_red'])
                V *= (1 - m['vuln_red'])
                I *= (1 - m['imp_red'])

        return A * P * V * I * K

    def get_category(self, risk, max_risk):
        norm = (risk / max_risk) * 100
        if norm > 75: return "Критический"
        if norm > 50: return "Высокий"
        if norm > 25: return "Средний"
        return "Низкий"

    def run(self):
        results = []
        all_base_risks = []

        for a in self.assets:
            for t in self.threats:
                all_base_risks.append(self.calculate_risk(a, t, self.vulnerability_level))
        
        max_r = max(all_base_risks)

        for a in self.assets:
            for t in self.threats:
                base_r = self.calculate_risk(a, t, self.vulnerability_level)
                applied = ["Firewall", "Backup"]
                resid_r = self.calculate_risk(a, t, self.vulnerability_level, applied)
                
                results.append({
                    "Актив": a['name'],
                    "Угроза": t['name'],
                    "Базовый риск": round(base_r, 2),
                    "Остаточный риск": round(resid_r, 2),
                    "Снижение %": round((1 - resid_r/base_r)*100, 1),
                    "Категория": self.get_category(base_r, max_r)
                })

        df = pd.DataFrame(results)
        print("\n--- ТАБЛИЦА РИСКОВ ---")
        print(df.sort_values(by="Базовый риск", ascending=False).head(5)) # ТОП-5 (Задание 4)

        sim_results = []
        for _ in range(1000):

            rand_threat = random.choice(self.threats).copy()
            rand_threat['prob'] *= random.uniform(0.8, 1.2)
            rand_asset = random.choice(self.assets)
            
            sim_results.append(self.calculate_risk(rand_asset, rand_threat, self.vulnerability_level))

        print("\n--- СТАТИСТИКА (1000 итераций) ---")
        print(f"Средний риск: {np.mean(sim_results):.2f}")
        print(f"Стандартное отклонение: {np.std(sim_results):.2f}")
    
        df.to_csv("risk_report.csv", index=False, encoding='utf-8-sig')
        
        plt.figure(figsize=(10, 6))
        plt.hist(sim_results, bins=30, color='skyblue', edgecolor='black')
        plt.title("Распределение рисков (Моделирование Монте-Карло)")
        plt.xlabel("Величина риска")
        plt.ylabel("Частота")
        plt.savefig("risk_distribution.png")
        print("\nОтчет сохранен в risk_report.csv, график в risk_distribution.png")
        plt.show()

if __name__ == "__main__":
    app = RiskManagementSystem()
    app.run()