from endpoints.productservice import ProductService
from json_models import create_json_model as model


def test_is_all_products_were_taken(app_config):
    product_service = ProductService()
    headers = product_service.get_auth_headers(app_config.base_url, app_config.token)
    response = product_service.get_products(app_config.base_url, headers)

    assert product_service.check_products_data_by_length(response) == 20
    assert product_service.check_status_code(response, 200)


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
