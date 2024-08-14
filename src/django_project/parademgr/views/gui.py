from django.shortcuts import render, reverse
from django.views.generic import DetailView, View, TemplateView

from handyhelpers.permissions import InAnyGroup
from handyhelpers.views import HandyHelperIndexView, HandyHelperListPlusCreateAndFilterView
from handyhelpers.views.htmx import (HtmxOptionMultiView, HtmxOptionDetailView, HtmxOptionMultiFilterView, HtmxItemizedView)

# import models
from parademgr.models import (Award, AwardType, Category, Division, Organization, Parade)

# import forms
# from parademgr.forms import ()


class Admin(HtmxItemizedView):
    """render the project index page"""

    title = """<span class="text-primary">Parade Planner</span> <span class="text-secondary">Admin</span>"""
    subtitle = "Select an option below"
    item_list = [
        {
            "url": "/dashboard",
            "icon": "fa-regular fa-map",
            "title": "Create Parade",
            "description": "Create a new parade",
        },
        {
            "url": "/rest",
            "icon": "fa-solid fa-award",
            "title": "Add Award",
            "description": "Add a new award",
        },
        {
            "url": "/rest",
            "icon": "fa-solid fa-certificate",
            "title": "Add Award Type",
            "description": "Add a new reward type",
        },
        {
            "url": "/rest",
            "icon": "fas fa-table-list",
            "title": "Add Category",
            "description": "Add a new parade category",
        },
        {
            "url": "/rest",
            "icon": "fa-solid fa-users-rectangle",
            "title": "Add Division",
            "description": "Add a new parade division",
        },
    ]


class Test(TemplateView):
    template_name = "parademgr/full/custom/test.html"


class DetailParade(HtmxOptionDetailView):
    model = Parade
    htmx_template_name = "parademgr/partial/detail/parade.htm"
    template_name = "parademgr/full/detail/parade.html"


class DetailOrganization(HtmxOptionDetailView):
    model = Organization
    htmx_template_name = "parademgr/partial/detail/organization.htm"
    template_name = "parademgr/full/detail/organization.html"


class ListAwards(HtmxOptionMultiFilterView):
    """list available Award entries"""
    queryset = Award.objects.all().select_related("division", "division__category")
    model = Award
    htmx_table_template_name = "parademgr/partial/table/awards.htm"
    template_name = "parademgr/full/list/awards.html"


class ListAwardTypes(HtmxOptionMultiFilterView):
    """list available AwardType entries"""
    model = AwardType
    htmx_table_template_name = "parademgr/partial/table/award_types.htm"
    template_name = "parademgr/full/list/award_types.html"


class ListCategories(HtmxOptionMultiFilterView):
    """list available Category entries"""
    model = Category
    htmx_table_template_name = "parademgr/partial/table/categories.htm"
    template_name = "parademgr/full/list/categories.html"


class ListDivisions(HtmxOptionMultiFilterView):
    """list available Division entries"""
    model = Division
    htmx_table_template_name = "parademgr/partial/table/divisions.htm"
    template_name = "parademgr/full/list/divisions.html"


class ListOrganizations(HtmxOptionMultiFilterView):
    """list available Organization entries"""
    model = Organization
    # htmx_list_template_name = "parademgr/partial/list/organizations.htm"
    htmx_table_template_name = "parademgr/partial/table/organizations.htm"
    template_name = "parademgr/full/list/organizations.html"


class ListParades(HtmxOptionMultiFilterView):
    """list available Parade entries"""
    model = Parade
    htmx_table_template_name ="parademgr/partial/table/parades.htm"
    template_name = "parademgr/full/list/parades.html"
