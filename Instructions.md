# Инструкции по запуску микросервиса

Каждая инструкция выполняется из директории репозитория mle-project-sprint-3-v001
Если необходимо перейти в поддиректорию, напишите соотвесвтующую команду

## 1. FastAPI микросервис в виртуальном окружение
```python
# команды создания виртуального окружения
# и установки необходимых библиотек в него

# Перейдите в домашнюю директорию репозитория mle-project-sprint-3-v001:
cd mle-project-sprint-3-v001
# Инициализируйте создание виртуального пространства, используя конкретную версию Python.
# установка расширения для виртуального пространства
sudo apt-get install python3.10-venv
# создание виртуального пространства
python3.10 -m venv .mle-sprint3-venv
# Перед началом работы активируйте виртуальное пространство
source .mle-sprint3-venv/bin/activate
# Находясь внутри виртуального пространства, установите все необходимые библиотеки
pip install -r requirements.txt
# команда перехода в директорию запуска микросервиса (~/mle-project-sprint-3-v001/services)
cd services
# команда запуска сервиса с помощью uvicorn
uvicorn ml_service.price_app:app --reload --port 8081 --host 0.0.0.0
# команда запуска тест-файла с помощью .py-скрипта
python test_app.py
# команда остановки микросервиса в терминале - нажатие клавиш Ctrl+C
```

### Пример curl-запроса к микросервису, 'item_id' по выбору пользователя

```bash
curl -X 'POST' \
  'http://localhost:8081/api/predict/?item_id=100' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "floor": 2,
  "kitchen_area": 10.5,
  "living_area": 20,
  "rooms": 1,
  "is_apartment": false,
  "studio": false,
  "total_area": 44.5,
  "build_year": 2007,
  "building_type_int": 4,
  "latitude": 55.72275161743164,
  "longitude": 37.89551162719727,
  "ceiling_height": 2.7,
  "flats_count": 368,
  "floors_total": 24,
  "has_elevator": true
}'
```


## 2. FastAPI микросервис в Docker-контейнере

```bash
# директория запуска микросервиса без изменений (~/mle-project-sprint-3-v001/services)
# команда для запуска микросервиса в режиме docker-контейнера
# сборка образа
docker image build . --tag ml_service_image -f Dockerfile_ml_service
# запуск контейнера
docker container run --publish 8081:8081 --env-file .env --name ml_service_container ml_service_image
# команда запуска тест-файла с помощью .py-скрипта
python test_docker.py
# проверка статуса контейнера
docker container ls -a | grep ml_service_container
# остановка контейнера
docker stop ml_service_container
# удаление контейнера
docker rm ml_service_container
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:8081/api/predict/?item_id=100' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "floor": 2,
  "kitchen_area": 10.5,
  "living_area": 20,
  "rooms": 1,
  "is_apartment": false,
  "studio": false,
  "total_area": 44.5,
  "build_year": 2007,
  "building_type_int": 4,
  "latitude": 55.72275161743164,
  "longitude": 37.89551162719727,
  "ceiling_height": 2.7,
  "flats_count": 368,
  "floors_total": 24,
  "has_elevator": true
}'
```

## 3. Docker compose для микросервиса и системы моониторинга

```bash
# директория запуска микросервиса без изменений (~/mle-project-sprint-3-v001/services)
# команда для запуска микросервиса в режиме docker compose
docker compose up --build
# команда запуска тест-файла с помощью .py-скрипта
python test_docker.py
# команда остановки микросервиса
docker compose down
# перед повторным запуском микросервиса убедитесь в том, что микросервис остановлен
docker compose ls
```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:8081/api/predict/?item_id=100' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "floor": 2,
  "kitchen_area": 10.5,
  "living_area": 20,
  "rooms": 1,
  "is_apartment": false,
  "studio": false,
  "total_area": 44.5,
  "build_year": 2007,
  "building_type_int": 4,
  "latitude": 55.72275161743164,
  "longitude": 37.89551162719727,
  "ceiling_height": 2.7,
  "flats_count": 368,
  "floors_total": 24,
  "has_elevator": true
}'
```

## 4. Скрипт симуляции нагрузки
Скрипт генерирует 40 запросов в течение 140 секунд с итерацией индекса запроса (item_id++) и увеличением жилой площади (living_area++) и общей площади (total_area++)

```bash
# команда запуска .py-скрипта для симуляции нагрузки
python test_prometheus.py
```

Адреса сервисов:
- микросервис: http://localhost:8081
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000