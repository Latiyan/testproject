from django.db import models


# Products Model
class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField(max_length=10)
    date_created = models.DateField()

    def  __str__(self):
        return self.name
