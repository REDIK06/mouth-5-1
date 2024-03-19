from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title


STARS = (
    (star, star * '*') for star in range(1, 6)
)


class Review(models.Model):
    text = models.TextField()
    stars = stars = models.IntegerField(choices=STARS, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')

    def __str__(self):
        return self.text[:50]
