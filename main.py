
from task_manager import TaskManager



if __name__ == "__main__":
    manager = TaskManager("tasks.json")

    while True:
        print("\n--- Система управління завданнями ---")
        print("1. Додати завдання")
        print("2. Видалити завдання")
        print("3. Список завдань (за пріоритетом)")
        print("4. Список завдань (за датою)")
        print("5. Позначити як виконане (видалити)")
        print("6. Вихід")
        
        choice = input("Оберіть дію: ")

        try:
            if choice == "1":
                desc = input("Опис: ")
                priority = int(input("Пріоритет (1-5): "))
                date = input("Дата (YYYY-MM-DD): ")
                manager.add_task(desc, priority, date)
                print("Завдання додано!")

            elif choice == "2":
                task_id = int(input("ID завдання для видалення: "))
                manager.delete_task(task_id)
                print("Завдання видалено!")

            elif choice == "3":
                print("\nСортування за пріоритетом:")
                for t in manager.list_tasks(sort_by="priority"):
                    print(f"[{t.id}] {t.description} | Пріоритет: {t.priority} | Дата: {t.created_at}")

            elif choice == "4":
                print("\nСортування за датою:")
                for t in manager.list_tasks(sort_by="date"):
                    print(f"[{t.id}] {t.description} | Дата: {t.created_at} | Пріоритет: {t.priority}")

            elif choice == "5":
                task_id = int(input("ID виконаного завдання: "))
                manager.complete_task(task_id)
                print("Завдання позначено як виконане та видалено!")

            elif choice == "6":
                print("Вихід з програми!")
                break
            else:
                print("Невірний вибір, спробуйте ще раз.")

        except ValueError as e:
            print(f" Помилка: {e}")
        except Exception as e:
            print(f"Сталася помилка: {e}")