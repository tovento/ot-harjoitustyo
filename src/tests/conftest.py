from initialize_database import reinitialize_database

def pytest_configure():
    reinitialize_database()
