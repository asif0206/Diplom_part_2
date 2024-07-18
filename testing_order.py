# Асиф Мамедов, 18-я когорта — Финальный проект
import data
from sender_test_request import post_new_order, get_order_track


def get_order_status_code():
    response_request = post_new_order(data.order_body)
    # сохранение track номера заказа
    track = response_request.json()["track"]
    return get_order_track(track).status_code

# Тест, что код ответа равен 200.
def test_get_order_track_code_200():
    assert get_order_status_code() == 200