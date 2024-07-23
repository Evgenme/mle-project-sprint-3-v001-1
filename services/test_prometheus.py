import requests
import time

# Определяем базовый URL для конечной точки предсказания
base_url = "http://localhost:8081/api/predict/"

for i in range(40):
    # Определяем item_id и параметры модели
    item_id = str(i)
    model_params = {
        "floor": 2,
        "kitchen_area": 10.5,
        "living_area": 20.0 + i,
        "rooms": 1,
        "is_apartment": False,
        "studio": False,
        "total_area": 44.5 + i,
        "build_year": 2007,
        "building_type_int": 4,
        "latitude": 55.72275161743164,
        "longitude": 37.89551162719727,
        "ceiling_height": 2.7,
        "flats_count": 368,
        "floors_total": 24,
        "has_elevator": True
    }

    # Конструируем полный URL с параметром запроса
    url = f"{base_url}?item_id={item_id}"

    # Отправляем POST-запрос на конечную точку предсказания с параметрами модели
    response = requests.post(url, json=model_params)
    if i == 15:
        time.sleep(30)
    time.sleep(2)
