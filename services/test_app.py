import requests

base_url = "http://0.0.0.0:8081/api/predict/"

# Определяем item_id и параметры модели
item_id = "12345"
model_params = {
    "floor": 2,
    "kitchen_area": 10.5,
    "living_area": 20.0,
    "rooms": 1,
    "is_apartment": False,
    "studio": False,
    "total_area": 44.5,
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

# Печатаем URL и полезную нагрузку для отладки
print("URL:", url)
print("Payload:", {"model_params": model_params})

# Отправка POST-запроса
response = requests.post(url, json=model_params)

# Печатаем статус-код ответа и JSON-ответ для отладки
print("Response Status Code:", response.status_code)
print("Response JSON:", response.json())
