from handyhelpers.forms import HtmxModelForm

# import models
from parademgr.models import Award, AwardType, Category, Division, Organization, Parade


class AwardForm(HtmxModelForm):
    hx_post = "/award"
    hx_target = "award-form"
    submit_button_text = "create"

    class Meta:
        model = Award
        fields = ["award_type", "division", "name", "description", "amount"]


class AwardTypeForm(HtmxModelForm):
    hx_post = "/awardtype"
    hx_target = "awardtype-form"
    submit_button_text = "create"

    class Meta:
        model = AwardType
        fields = ["name", "description"]


class CategoryForm(HtmxModelForm):
    hx_post = "/category"
    hx_target = "category-form"
    submit_button_text = "create"

    class Meta:
        model = Category
        fields = ["name", "label", "description"]


class DivisionForm(HtmxModelForm):
    hx_post = "/division"
    hx_target = "division-form"
    submit_button_text = "create"

    class Meta:
        model = Division
        fields = ["category", "name", "label", "description"]


class OrganizationForm(HtmxModelForm):
    hx_post = "/organization"
    hx_target = "organization-form"
    submit_button_text = "create"

    class Meta:
        model = Organization
        fields = ["name", "description"]

        labels = {
            "name": "Name",
            "description": "Description",
        }


class ParadeForm(HtmxModelForm):
    hx_post = "/parade"
    hx_target = "parade-form"
    submit_button_text = "create"

    class Meta:
        model = Parade
        fields = ["year", "title"]

        labels = {
            "year": "Year",
            "title": "Title",
        }
