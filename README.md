# Проект. Релиз модели в продакшен

Здесь укажите имя вашего бакета: s3-student-mle-20240227-ebfcdc15b4

## Описание задачи

Вывести в продакшен ML-модель для оценки цен на недвижимость.
Cоблюсти следующие условия:
- У коллег должна быть возможность получать предсказания модели онлайн.
- Сервис с моделью должен быть устроен гибко — так, чтобы его можно было разворачивать на разных виртуальных машинах, где уже работают другие сервисы.
- Предусмотреть мониторинг работы сервиса, чтобы своевременно узнавать о потенциальных рисках.

## Задача инженера машинного обучения

- Разработать FastAPI-микросервис.
- Контейнеризовать его с помощью Docker.
- Развернуть систему мониторинга, используя Prometheus и Grafana.
- Разработать дашборд для мониторинга в Grafana.
- Используйте модель, которую вы получили по результатам выполнения проекта второго спринта.

## Инфраструктура и инструменты

Для выполнения проекта вам понадобятся следующие инструменты:
- Visual Studio Code;
- FastAPI, Uvicorn;
- Docker и Docker Compose;
- Prometheus;
- Grafana;
- Python-библиотеки для экспортеров: prometheus_client, prometheus_fastapi_instrumentator;
- Рекомендуется использовать виртуальную машину для проведения всех этапов.