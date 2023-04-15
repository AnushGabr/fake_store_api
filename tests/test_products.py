import json

from endpoints.productservice import ProductService
from json_models import create_json_model as model, create_json_model


def test_product(app_config):
    product_service = ProductService()

    assert product_service.get_products(app_config.base_url, app_config.token)


def test_get_in_category(app_config):
    product_service = ProductService()
    #category = "jewelery"
    response = product_service.get_products_by_category(app_config.base_url)

    products = json.loads(response.text)
    print(products, response.text)
    assert response.status_code == 200
    assert len(products) > 0
    assert products["category"] == "jewelery"


def test_create_product(app_config):
    product_service = ProductService()

    new_prod = create_json_model.create_product_json('test product', 13.5, 'lorem ipsum set', 'https://i.pravatar.cc', 'electronic')
    created_prod = product_service.create_new_product(app_config.base_url, new_prod)
    print(new_prod,  created_prod)
    assert product_service.check_status_code(created_prod, 200)



def test_update_product(app_config):
    product_service = ProductService()
    headers = product_service.get_auth_headers(app_config.base_url, app_config.token)
    json_for_update = model.update_product(
        "Adidas Daily 3.0 Shoes",
        65,
        "A fresh take on a classic",
        "i.sportisimo.com/products/images/1181/1181185/700x700/adidas-daily-3-0-dblu_6.jpg",
        "men's clothing"
    )
    response = product_service.update_product(app_config.base_url, 7, json_for_update, headers)
    assert product_service.check_status_code(response, 200)
    assert product_service.check_response_body_key(response, json_for_update, "title")
    assert product_service.is_product_entirely_updated(response, json_for_update)

def test_delete_product(app_config):
    product_service = ProductService()
    headers = product_service.get_auth_headers(app_config.base_url, app_config.token)
    response = product_service.delete_product(app_config.base_url, 6, headers)
    assert product_service.check_status_code(response, 200)
    assert product_service.check_response_time_in_seconds(response, 1)
    # The actual product is not deleted from the DB, that's why we can't further check the deletion.
