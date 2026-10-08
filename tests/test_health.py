from app import create_app


def test_health_endpoint_returns_service_status():
    app = create_app(
        {
            "TESTING": True,
            "SECRET_KEY": "test-secret",
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
    )

    response = app.test_client().get("/api/health")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {
        "status": "ok",
        "service": "flask-final-assignment",
    }
