# Employee Directory

Employee Directory — это веб-приложение на Django, которое отображает древовидную структуру отделов компании с сотрудниками. Приложение поддерживает CRUD операции для сотрудников и отделов через административную панель.

## Структура проекта

- **employees/**: Основное приложение проекта, содержащее модели, представления, шаблоны и админ-конфигурации.
  - **migrations/**: Миграции базы данных.
  - **models.py**: Определение моделей `Department` и `Employee`.
  - **views.py**: Представления для отображения древовидной структуры.
  - **admin.py**: Конфигурация админ-панели.
  - **templates/**: HTML-шаблоны для отображения структуры отделов и сотрудников.
    - **department_tree.html**: Основной шаблон для отображения древовидной структуры.
    - **department_node.html**: Вспомогательный шаблон для рекурсивного отображения вложенных отделов.
- **manage.py**: Основной файл управления проектом.
- **populate_db.py**: Скрипт для заполнения базы данных департаментами и сотрудниками.
- **requirements.txt**: Зависимости проекта.

## Установка

Для начала работы с проектом выполните следующие шаги:

1. Клонируйте репозиторий:

    ```bash
    git clone <ссылка на репозиторий>
    cd employee_directory
    ```

2. Создайте виртуальное окружение и активируйте его:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Для Windows: .venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Примените миграции:

    ```bash
    python manage.py migrate
    ```

5. Создайте суперпользователя для доступа в админ-панель:

    ```bash
    python manage.py createsuperuser
    ```

6. Заполните базу данных примерными данными:

    ```bash
    python populate_db.py
    ```

7. Запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

8. Перейдите по адресу `http://127.0.0.1:8000/`, чтобы увидеть приложение.

## Основные функции

- **Древовидная структура отделов**: Отделы компании представлены в виде дерева с вложенностью до 5 уровней.
- **Список сотрудников**: Каждый отдел содержит список сотрудников с их должностями, датой приема на работу и размером заработной платы.
- **Административная панель**: Полный доступ к CRUD операциям для управления отделами и сотрудниками через стандартную админку Django.

## Используемые технологии

- **Django 3.5+**: Основной фреймворк для разработки приложения.
- **Python 3.5+**: Язык программирования.
- **Bootstrap 4.5**: Для стилизации интерфейса.
