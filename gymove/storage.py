import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
STORAGE_DIR = BASE_DIR / "storage"


class Storage:

    @staticmethod
    def _file(filename):
        return STORAGE_DIR / filename

    @staticmethod
    def read(filename):
        file = Storage._file(filename)

        if not file.exists():
            return []

        try:
            with open(file, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    @staticmethod
    def write(filename, data):
        file = Storage._file(filename)

        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    @staticmethod
    def add(filename, item):
        data = Storage.read(filename)
        data.append(item)
        Storage.write(filename, data)

    @staticmethod
    def update(filename, key, value, new_item):
        data = Storage.read(filename)

        for i, item in enumerate(data):
            if item.get(key) == value:
                data[i] = new_item
                break

        Storage.write(filename, data)

    @staticmethod
    def delete(filename, key, value):
        data = Storage.read(filename)

        data = [
            item
            for item in data
            if item.get(key) != value
        ]

        Storage.write(filename, data)



        