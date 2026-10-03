def diagnose_cow_temperature(current_ma) -> str:
    try:
        current_ma = float(current_ma)
    except (ValueError, TypeError):
        return f"Ошибка. Ожидалось число."

    pv_min = 0.0
    pv_max = 75.0

    if current_ma == 0:
        return "Статус: Датчик отключен."

    if 3.9 <= current_ma <= 20.1:
        sensor_status = "исправен"
    elif (0 < current_ma < 3.9) or (current_ma > 20.1):
        return "Статус: Датчик неисправен."
    else:
        return "Статус: Некорректный (отрицательный) сигнал."

    temperature = (current_ma - 4) * (pv_max - pv_min) / 16.0 + pv_min

    if 37.5 <= temperature <= 39.0:
        cow_status = "с коровой все ок."
    elif 35.0 <= temperature <= 37.4:
        cow_status = "корова замерзла, требуется обогрев."
    elif 39.1 <= temperature <= 39.5:
        cow_status = "корова перегрелась, требуется охлаждение."
    elif temperature <= 34.9:
        cow_status = "требуется внимание (датчик свалился или корова плохо себя чувствует)."
    elif temperature >= 39.6:
        cow_status = "срочно вызывайте ветеринара, корова заболела."
    else:
        cow_status = "температура на грани допустимых порогов, требуется проверка."

    return (
        f"Получен сигнал датчика {current_ma:.2f}mA, датчик {sensor_status}, "
        f"температура {temperature:.1f} °C, {cow_status}"
    )


print(diagnose_cow_temperature(12.11))
print(diagnose_cow_temperature("12.11"))
print(diagnose_cow_temperature("не число"))
print(diagnose_cow_temperature(None))
