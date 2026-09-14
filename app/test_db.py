from app.database import engine



try:
    with engine.connect():
        print("connected")
except Exception as e:
    print(e)