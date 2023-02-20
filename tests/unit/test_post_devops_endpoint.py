import os

def test_check_response_payload_from_send_message(message, client):
    """test success operation on post method to devops endpoint"""
    api_key = os.getenv("API_KEY")

    response = client.get("/jwt/")
    token = response.json()["token"]

    headers = {
        "x-parse-rest-api-key" : api_key,
        "x-jwt-kwy": token,
        }
    response = client.post("/DevOps/", json=message, headers=headers)
    expected_message = f"Hello {message['to']} your message will be send"
    assert response.json()["message"] == expected_message
    assert response.status_code == 200


def test_check_token_is_valid_only_for_one_transaction_to_send_message(message, client):
    """check that token is valid only for one transaction"""
    api_key = os.getenv("API_KEY")

    response = client.get("/jwt/")
    token = response.json()["token"]

    headers = {
        "x-parse-rest-api-key" : api_key,
        "x-jwt-kwy": token,
        }
    response = client.post("/DevOps/", json=message, headers=headers)
    assert response.status_code == 200
    response2 = client.post("/DevOps/", json=message, headers=headers)
    assert response2.status_code == 401
