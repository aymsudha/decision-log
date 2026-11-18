from app.main import health


def test_smoke():
    assert health()["status"] == "ok"
