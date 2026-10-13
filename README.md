# Web App Healthcheck Lab

## Запуск прєкту
1. Клонуйте репозиторій.
2. Переконайтесь, що у вас встановлено Docker и Docker Compose.
3. Виконайте команду: `docker compose up --build`
4. Додаток буде доступний за адресою `http://localhost:8080`.

## Ендпоінти
* `http://localhost:8080/healthz/live`
* `http://localhost:8080/healthz/ready`