from source.lib.shopify.base import ShopifyResource


class Province(ShopifyResource):
    _prefix_source = "/admin/countries/$country_id/"
