import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

import django
django.setup()

from faker import Faker
import random 
from Product.models import Product, Brand


def seed_brand(n):
    fake = Faker()
    images = ['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']

    for _ in range (n):
        name = fake.name() 
        image = f"brand/{images[random.randint(0,9)]}" 
        Brand.objects.create(name=name, image=image)
    print(f"seed {n} Brands ...")

def seed_product(n):
    fake = Faker()
    images = ['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg']
    flag_types = ['Sale','Feature','New']

    for _ in range(n):
        name = fake.name()
        sku = random.randint(1,100000)
        image = f"Products/{images[random.randint(0,7)]}" 
        brand = Brand.objects.get(id=random.randint(1,20))
        price = round (random.uniform(20.99,99.99),2)
        flag = flag_types[random.randint(0,2)]
        subtitle = fake.text(max_nb_chars=500)
        description = fake.text(max_nb_chars=2000)
        quantity = random.randint(2,30)

        Product.objects.create(
            name=name,
            image=image,
            flag=flag,
            price=price,
            sku=sku,
            brand=brand,
            subtitle=subtitle,
            description=description,
            quantity=quantity,

        )


#seed_brand(20)
seed_product(3000)