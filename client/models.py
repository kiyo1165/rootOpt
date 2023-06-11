from django.db import models
from django.core.validators import RegexValidator
from Dr.models import VisitPlan
# Create your models here.

PRIORITY = (
    ("1", "高"),
    ("2", "中"),    ("3", "低"),
)



class Client(models.Model):
    client_name = models.CharField(max_length=100)
    zip_code_regex = RegexValidator(
        regex=r'^[0-9]+$', message=("郵便番号の入力規則例: 123-4433 →'1234567'"))
    zip_code = models.CharField(
        validators=[zip_code_regex], max_length=7, verbose_name='郵便番号')
    pref = models.CharField(max_length=50, verbose_name='都道府県')
    city = models.CharField(max_length=100, verbose_name='市区町村')
    address = models.CharField(max_length=100, verbose_name="番地")
    Buil_name = models.CharField(max_length=100, verbose_name="建物名・部屋番号")
    priority = models.CharField(choices=PRIORITY, max_length=1)
    longitude = models.FloatField(blank=True, null=True, verbose_name="緯度")
    latitude = models.FloatField(blank=True, null=True, verbose_name="経度")
    visitplan = models.ForeignKey(
        VisitPlan, on_delete=models.CASCADE, related_name="clients")

    def __str__(self) -> str:
        return self.client_name
