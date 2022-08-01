from storage import storage_1, storage_2, shop_1, Request

while True:
    print("в наличие:")
    print(f"storage_1: {storage_1}")
    print(f"storage_2: {storage_2}")
    print(f"shop_1: {shop_1}")
    user_text = input("введите команду:\n")       # Забрать 4 телефон из storage_2
    if user_text == "стоп":
        break
    else:
        try:
            req = Request(user_text)
            req.move()
        except Exception as e:
            print("произошла ошибка")