from django.db import models

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plan_name
