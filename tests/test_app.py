import pytest
from flask import Flask

# テスト用のFlaskアプリを作成するフィクスチャ
@pytest.fixture
def client():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, Flask!"

    with app.test_client() as client:
        yield client

# ホームページのテスト
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, Flask!"
