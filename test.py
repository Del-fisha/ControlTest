import json
import datetime


# Функция для создания заметки
def create_note():
    note_id = input("Введите идентификатор заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }

    return note


# Функция для сохранения заметки в файл
def save_note(note, file):
    with open(file, "a") as f:
        f.write(json.dumps(note) + "\n")


# Функция для чтения списка заметок из файла
def read_notes(file):
    notes = []
    with open(file, "r") as f:
        for line in f:
            note = json.loads(line)
            notes.append(note)
    return notes


# Функция для редактирования заметки
def edit_note(note):
    new_title = input("Введите новый заголовок заметки: ")
    new_body = input("Введите новое тело заметки: ")
    note["title"] = new_title
    note["body"] = new_body
    note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return note


# Функция для удаления заметки
def delete_note(note_id, file):
    notes = read_notes(file)
    filtered_notes = [note for note in notes if note["id"] != note_id]
    with open(file, "w") as f:
        for note in filtered_notes:
            f.write(json.dumps(note) + "\n")


# Главная функция приложения
def main():
    file = "notes.txt"
    while True:
        command = input("Введите команду (add, read, edit, delete, quit): ")

        if command == "add":
            note = create_note()
            save_note(note, file)
            print("Заметка успешно сохранена")

        elif command == "read":
            notes = read_notes(file)
            for note in notes:
                print("ID:", note["id"])
                print("Заголовок:", note["title"])
                print("Тело:", note["body"])
                print("Время создания:", note["timestamp"])
                print()

        elif command == "edit":
            note_id = input("Введите ID заметки для редактирования: ")
            notes = read_notes(file)
            for note in notes:
                if note["id"] == note_id:
                    edited_note = edit_note(note)
                    delete_note(note["id"], file)
                    save_note(edited_note, file)
                    print("Заметка успешно отредактирована")
                    break
            else:
                print("Заметка с таким ID не найдена")

        elif command == "delete":
            note_id = input("Введите ID заметки для удаления: ")
            delete_note(note_id, file)
            print("Заметка успешно удалена")

        elif command == "quit":
            break

        else:
            print("Неверная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()