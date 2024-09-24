from pathlib import Path


def get_cats_info(path: Path) -> list[dict]:
    
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for cat in file.readlines():
                info = cat.strip().split(",")
                cats_info.append({
                    "id": info[0],
                    "name": info[1],
                    "age": info[2]
                })
    except FileNotFoundError as error:
        print(error)
        return []
    except IndexError:
        print("[Error] The file is corrupted")
        return []
    
    return cats_info


cats_info = get_cats_info("cats.txt")
print(cats_info)