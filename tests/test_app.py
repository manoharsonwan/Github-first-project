from app import index


def test_index():
    assert index() == "This is CI/CD"