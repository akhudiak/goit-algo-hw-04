from pathlib import Path


def total_salary(path: Path) -> tuple[float, float]:

    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = [float(employee.strip().split(",")[1]) for employee in file.readlines()]
    except FileNotFoundError as error:
        print(error)
        return (0, 0)
    except (IndexError, ValueError):
        print("[Error] The file is corrupted")
        return (0, 0)
    
    return sum(salaries), sum(salaries) / len(salaries)


total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")