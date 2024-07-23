# services/ml_service/price_app.py

from fastapi import FastAPI, Body
from ml_service.fast_api_handler import FastApiHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram
import time

app = FastAPI()

# инициализируем и запускаем экспортёр метрик
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

# создаем гистограмму для предсказаний
main_app_predictions = Histogram(
    # имя метрики
    "main_app_predictions",
    #описание метрики
    "Histogram of predictions",
    #указаываем корзины для гистограммы
    buckets=(1e6, 2.5e6, 5e6, 7.5e6, 1e7, 2.5e7, 5e7, 1e8)
)

# создаем гистограмму для времени выполнения
main_app_prediction_latency = Histogram(
    "main_app_prediction_latency_seconds",
    "Histogram of prediction latency in seconds",
    buckets=(0.1, 0.5, 1, 2, 5, 10)
)

# создаём обработчик запросов для API
app.handler = FastApiHandler()

@app.post("/api/predict/")
def get_prediction_for_item(
    item_id: str,
    model_params: dict = Body(
        default={
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
    )
):
    # Debugging: печать запроса
    print("Received item_id:", item_id)
    print("Received model_params:", model_params)

    all_params = {
        "item_id": item_id,
        "model_params": model_params
    }

    # измеряем время выполнения
    start_time = time.time()
    resp = app.handler.handle(all_params)
    duration = time.time() - start_time

    # фиксируем значение предсказаний в метрике
    main_app_predictions.observe(resp['prediction'])

    # фиксируем время выполнения в метрике
    main_app_prediction_latency.observe(duration)

    print("Ответ:", resp)
    print("Время выполнения:", duration, "секунд")
    
    return resp

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
