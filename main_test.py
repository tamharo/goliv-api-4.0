import main


def test_hello():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get("/")
    assert r.status_code == 200
    response_text = r.data.decode("utf-8")
    assert "Hello, world!" in response_text
