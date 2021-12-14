from django.db import models


# Abstract base classes
class ContactInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    address = models.TextField(max_length=20)

    class Meta:
        abstract = True


class Customer(ContactInfo):
    phone = models.IntegerField(max_length=15)

    def __str__(self):
        return str(self.phone)


class Staff(ContactInfo):
    position = models.CharField(max_length=10)

    def __str__(self):
        return self.position


# Proxy model
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MyPerson(Person):
    class Meta:
        proxy = True


# Multi table inheritance
class Place(models.Model):
    name_place = models.CharField(max_length=20)
    address = models.TextField(max_length=20)

    def __str__(self):
        return self.name_place


class Restaurant(Place):
    name_restaurant = models.CharField(max_length=20)
    serves_pizza = models.BooleanField(default=False)
    serves_pasta = models.BooleanField(default=False)

    def __str__(self):
        return self.name_restaurant
