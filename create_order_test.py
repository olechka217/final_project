import sender_stand_request
import data

def get_new_order_track():
    create_order_body = data.create_order_body.copy()
    user_response = sender_stand_request.post_new_order_kit(create_order_body)
    return user_response.json()["track"]

def positive_assert(kit_body):
    new_order_track = get_new_order_track()
    kit_response = sender_stand_request.get_order( new_order_track)
    assert kit_response.status_code == 200 

#positive test case for new order
def test_new_order_success_response():
    positive_assert(get_new_order_track())
