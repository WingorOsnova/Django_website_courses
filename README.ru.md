Магазин курсов (Django)

Admin name: guest
password: g123456g

Обзор
- Простой каталог/магазин курсов на Django и Bootstrap.
- REST‑подобный API реализован через django-tastypie.
- Чтение по API открыто; запись требует API‑ключ.
- Админка с инлайнами и необязательной темой django-jet.

Ключевой функционал
- Модели данных: `Category` и `Course` (связь `ForeignKey` из Course к Category).
- Веб‑интерфейс: список всех курсов и страница курса.
- Админка: колонки списка, инлайны курсов в категориях, базовый брендинг.
- API: `GET` открыт; `POST/PUT/DELETE` защищены API‑ключом.
- В API настраивается hydrate/dehydrate для работы с `category_id`.

Технологии
- Python 3.10+
- Django 4.0.8
- django-tastypie 0.15.1
- Bootstrap 5.3 (CDN)
- SQLite (по умолчанию)
- Опционально: django-jet (тема админки)

Структура проекта
- `base/` — настройки, роутинг, WSGI/ASGI.
- `shop/` — предметная логика: модели, вью, урлы, админ, миграции.
- `api/` — ресурсы tastypie, аутентификация, урлы.
- `templates/` — базовый шаблон и шаблоны раздела shop.
- `manage.py`, `requirements.txt`, `db.sqlite3`.

Запуск локально
1) Создать и активировать виртуальное окружение
   - `python -m venv .venv`
   - macOS/Linux: `source .venv/bin/activate`
   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`

2) Установить зависимости
   - `pip install -r requirements.txt`
   - Опционально (тема админки): `pip install django-jet`

3) Применить миграции
   - `python manage.py migrate`

4) Создать суперпользователя
   - `python manage.py createsuperuser`

5) Запустить сервер разработки
   - `python manage.py runserver`
   - Веб‑интерфейс: http://127.0.0.1:8000/
   - Админка: http://127.0.0.1:8000/admin/
   - API‑корень: http://127.0.0.1:8000/api/v1/

Веб‑интерфейс
- Список курсов: `/` (клик по названию — детали)
- Страница курса: `/<course_id>`

Админка
- Кастомные заголовки и инлайновое редактирование курсов внутри категорий.
- Если `django-jet` не установлен, удалите `jet` и `jet.dashboard` из `INSTALLED_APPS` в `base/settings.py` или установите пакет.

API (Tastypie)
- Корень: `/api/v1/`
- Ресурсы:
  - `GET /api/v1/categories/`
  - `GET /api/v1/courses/`
  - `POST /api/v1/courses/` (нужен API‑ключ)
  - `PUT /api/v1/courses/<id>/` (нужен API‑ключ)
  - `DELETE /api/v1/courses/<id>/` (нужен API‑ключ)

Аутентификация
- Чтение (`GET`) открыто для всех.
- Запись (`POST/PUT/DELETE`) требует API‑ключ Tastypie.
- Передавайте `username` и `api_key` в query‑параметрах или через заголовок `Authorization` (согласно ApiKeyAuthentication из Tastypie).
- Ключи привязаны к пользователям Django. Если у пользователя нет ключа, откройте его в админке и сохраните — ключ создастся сигналом Tastypie (или используйте имеющуюся management‑команду, если она доступна).

Поля курса (API)
- Обязательные при создании/обновлении: `title` (str), `price` (float), `students_qty` (int), `reviews_qty` (int), `category_id` (int)
- В ответе исключены: `created_at`, `reviews_qty`
- Особенности:
  - hydrate: проставляет `category_id` в объект `Course`
  - dehydrate: возвращает `category_id` и упрощённое поле `category`

Примеры
- Список курсов (публично):
  - `curl http://127.0.0.1:8000/api/v1/courses/?format=json`

- Создание курса (нужен API‑ключ):
  - `curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"title":"Django Basics","price":49.0,"students_qty":100,"reviews_qty":10,"category_id":1}' \
    'http://127.0.0.1:8000/api/v1/courses/?username=<USER>&api_key=<API_KEY>&format=json'`

Акценты проекта
- Разделение веб‑вью и API‑ресурсов.
- Простая и наглядная модель данных + удобство в админке (инлайны, списки).
- Пример Tastypie с кастомным правилом аутентификации: открытое чтение, защищённая запись.
- Чистая структура шаблонов с Bootstrap и навигацией.

Примечания
- При смене БД обновите `DATABASES` в `base/settings.py`.
- В `requirements.txt` указан Django 4.0.8; убедитесь, что версия Python совместима.

