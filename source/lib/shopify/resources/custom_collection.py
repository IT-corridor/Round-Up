from source.lib.shopify import mixins
from source.lib.shopify.base import ShopifyResource
from source.lib.shopify.resources import Product, Collect


class CustomCollection(ShopifyResource, mixins.Metafields, mixins.Events):

    def products(self):
        return Product.find(collection_id=self.id)

    def add_product(self, product):
        return Collect.create({'collection_id': self.id, 'product_id': product.id})

    def remove_product(self, product):
        collect = Collect.find_first(collection_id=self.id, product_id=product.id)
        if collect:
            collect.destroy()
