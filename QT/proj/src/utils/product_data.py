def get_product_data(category="Все модели"):
    all_products = [
        {"name": "Кроссовки Nike Air", "price": 5990, "gender": "Мужчинам"},
        {"name": "Ботинки Timberland", "price": 8990, "gender": "Мужчинам"},
        {"name": "Туфли Clarks", "price": 7490, "gender": "Мужчинам"},
        {"name": "Кеды Converse", "price": 4990, "gender": "Мужчинам"},
        {"name": "Лоферы Gucci", "price": 15990, "gender": "Мужчинам"},
        {"name": "Балетки Zara", "price": 2990, "gender": "Женщинам"},
        {"name": "Босоножки Mango", "price": 3490, "gender": "Женщинам"},
        {"name": "Сапоги Ecco", "price": 9990, "gender": "Женщинам"},
        {"name": "Туфли на каблуке", "price": 5990, "gender": "Женщинам"},
        {"name": "Сникерсы Adidas", "price": 5490, "gender": "Женщинам"},
        {"name": "Сандалии Reebok", "price": 4290, "gender": "Мужчинам"},
        {"name": "Кроссовки Puma RS-X", "price": 6290, "gender": "Мужчинам"},
        {"name": "Мокасины Geox", "price": 6790, "gender": "Мужчинам"},
        {"name": "Босоножки H&M", "price": 1990, "gender": "Женщинам"},
        {"name": "Угги UGG", "price": 10990, "gender": "Женщинам"},
        {"name": "Эспадрильи Tommy Hilfiger", "price": 4590, "gender": "Женщинам"},
        {"name": "Тапочки домашние", "price": 990, "gender": "Женщинам"},
        {"name": "Кеды Vans Old Skool", "price": 5890, "gender": "Мужчинам"},
        {"name": "Треккинговые ботинки Columbia", "price": 8490, "gender": "Мужчинам"},
        {"name": "Ботильоны Calvin Klein", "price": 7890, "gender": "Женщинам"},
    ]

    if category == "Все модели":
        return all_products
    elif category == "Мужчинам":
        return [p for p in all_products if p["gender"] == "Мужчинам"]
    elif category == "Женщинам":
        return [p for p in all_products if p["gender"] == "Женщинам"]
    return []
