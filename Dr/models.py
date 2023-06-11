from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Dr(models.Model):
    name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class VisitPlan(models.Model):
    plan_name = models.CharField(max_length=200)
    business_day = models.IntegerField()
    dr = models.ForeignKey(
        Dr, on_delete=models.CASCADE, related_name="visit_plans")
    zip_code_regex = RegexValidator(
        regex=r'^[0-9]+$', message=("郵便番号の入力規則例: 123-4433 →'1234567'"))
    zip_code = models.CharField(
        validators=[zip_code_regex], max_length=7, verbose_name='郵便番号', null=True)
    pref = models.CharField(max_length=50, verbose_name='都道府県')
    city = models.CharField(max_length=100, verbose_name='市区町村')
    address = models.CharField(max_length=100, verbose_name="番地")
    Buil_name = models.CharField(max_length=100, verbose_name="建物名・部屋番号")
    longitude = models.FloatField(blank=True, null=True, verbose_name="緯度")
    latitude = models.FloatField(blank=True, null=True, verbose_name="経度")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plan_name
