import data
import sender_stand_request

def get_track_of_order():
    response = sender_stand_request.create_order(data.body)
    return response.json()["track"]
def positive_assert_get_order():
    track = get_track_of_order()
    response = sender_stand_request.get_order(track)
    assert response.status_code == 200

def test_get_order():
    positive_assert_get_order()