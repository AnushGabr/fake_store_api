import json


def create_product_json(title, price, description, image, category):

    data = {
        'title': title,
        'price': price,
        'description': description,
        'image': image,
        'category': category
    }

    json_data = json.dumps(data)
    return json_data

def update_product(title, price, description, image, category):

    data = {
        'title': title,
        'price': price,
        'description': description,
        'image': image,
        'category': category
    }

    return data


