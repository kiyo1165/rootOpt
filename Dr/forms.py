from django.forms import ModelForm
from Dr.models import VisitPlan


class VisitPlanForm(ModelForm):
    class Meta:
        model = VisitPlan
        fields = ["plan_name", "business_day", "dr", "pref","zip_code", "city", "address", "Buil_name"]

