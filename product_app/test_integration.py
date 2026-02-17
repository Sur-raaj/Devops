from django.test import TestCase
from django.urls import reverse
from product_app.models import Products

#python manage.py test product_app.test_integration

class ProductIntegrationTestCase(TestCase):
    def test_create_cheap_product(self):
        #Test that a cheap  product (price < 1000) is NOT saved via the 
        response = self.client.post(
            reverse("home"),
            {"name": "Cheap Product",
             "price":"50"}
                     )
        self.assertEqual(response.status_code,302) 

        #Cheap product should NOT exist due to save() logic
        with self.assertRaises(Products.DoesNotExist):
            Products.objects.get(name="Cheap Product")

