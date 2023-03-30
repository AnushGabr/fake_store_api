from endpoints.productservice import ProductService


def test_product(app_config):
    product_service = ProductService()

    assert product_service.get_products(app_config.base_url, app_config.token, 200)
