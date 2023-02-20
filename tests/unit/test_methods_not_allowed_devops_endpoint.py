def test_error_message_from_get_method(client):
    """test get method that is not allowed"""
    reponse = client.get("/DevOps/")
    assert reponse.json()["detail"] == "ERROR"


def test_error_messages_from_put_method(client):
    """test put method that is not allowed"""
    reponse = client.put("/DevOps/")
    assert reponse.json()["detail"] == "ERROR"


def test_error_message_from_delete_method(client):
    """test delete method that is not allowed"""
    reponse = client.delete("/DevOps/")
    assert reponse.json()["detail"] == "ERROR"

def test_error_message_from_patch_method(client):
    """test patch method that is not allowed"""
    reponse = client.patch("/DevOps/")
    assert reponse.json()["detail"] == "ERROR"
