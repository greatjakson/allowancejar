# === Stage 2: Проверка полей ===
# Project: AllowanceJar
def normalize_input(text):
    return text.strip().lower()


def normalize_amount(text):
    cleaned = text.replace(',', '.', 1).replace(' ', '').strip()
    try:
        value = float(cleaned)
    except ValueError:
        return None
    if value <= 0:
        return None
    return value


def validate_child(name, age, weekly_amount, goal):
    errors = []

    if not name or not name.strip():
        errors.append("Имя не может быть пустым")
    else:
        name = name.strip()
        if len(name) > 50:
            errors.append("Имя слишком длинное (максимум 50 символов)")

    if age is None or str(age).strip() == "":
        errors.append("Укажите возраст")
    else:
        try:
            age = int(str(age).strip())
            if age < 0:
                errors.append("Возраст не может быть отрицательным")
            elif age > 150:
                errors.append("Возраст нереалистичный")
        except ValueError:
            errors.append("Возраст должен быть целым числом")

    if weekly_amount is None or str(weekly_amount).strip() == "":
        errors.append("Укажите сумму карманных денег в неделю")
    else:
        amount = normalize_amount(str(weekly_amount))
        if amount is None:
            errors.append("Сумма должна быть положительным числом")
        else:
            weekly_amount = amount

    if goal is None or str(goal).strip() == "":
        errors.append("Укажите цель")
    else:
        goal = normalize_input(str(goal))
        if len(goal) > 100:
            errors.append("Цель слишком длинная (максимум 100 символов)")

    return name, age, weekly_amount, goal, errors
