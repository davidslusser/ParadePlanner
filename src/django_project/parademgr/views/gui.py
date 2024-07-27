from django.shortcuts import render
from django.views.generic import DetailView, View, TemplateView

from handyhelpers.permissions import InAnyGroup
from handyhelpers.views import HandyHelperIndexView, HandyHelperListPlusCreateAndFilterView
from handyhelpers.views.htmx import HtmxOptionMultiView, HtmxOptionDetailView

# import models
from parademgr.models import (Award, AwardType, Category, Division, Organization, Parade)

# import forms
# from parademgr.forms import ()


class Test(TemplateView):
    template_name = "parademgr/full/custom/test.html"


class Index(HandyHelperIndexView):
    """render the parademgr index page"""

    title = """Parademgr"""
    subtitle = "Select an option below"
    item_list = [
        {
            "url": "/parademgr/dashboard",
            "icon": "fas fa-tachometer-alt",
            "title": "Dashboard",
            "description": "Dashboard for Parademgr ",
        },
        {
            "url": "/parademgr/rest",
            "icon": "fas fa-download",
            "title": "APIs",
            "description": "List RESTful APIs for Parademgr",
        },
    ]
    protected_item_list = []
    protected_group_name = "admin"


class DetailParade(HtmxOptionDetailView):
    model = Parade
    htmx_template_name = "parademgr/partial/detail/parade.htm"
    template_name = "parademgr/full/detail/parade.html"


class DetailOrganization(HtmxOptionDetailView):
    model = Organization
    htmx_template_name = "parademgr/partial/detail/organization.htm"
    template_name = "parademgr/full/detail/organization.html"


class ListAwards(HtmxOptionMultiView):
    """list available Award entries"""
    queryset = Award.objects.all().select_related("division", "division__category")
    model = Award
    htmx_table_template_name = "parademgr/partial/table/awards.htm"
    template_name = "parademgr/full/list/awards.html"


class ListAwardTypes(HtmxOptionMultiView):
    """list available AwardType entries"""
    model = AwardType
    htmx_table_template_name = "parademgr/partial/table/award_types.htm"
    template_name = "parademgr/full/list/award_types.html"


class ListCategories(HtmxOptionMultiView):
    """list available Category entries"""
    model = Category
    htmx_table_template_name = "parademgr/partial/table/categories.htm"
    template_name = "parademgr/full/list/categories.html"


class ListDivisions(HtmxOptionMultiView):
    """list available Division entries"""
    model = Division
    htmx_table_template_name = "parademgr/partial/table/divisions.htm"
    template_name = "parademgr/full/list/divisions.html"


class ListOrganizations(HtmxOptionMultiView):
    """list available Organization entries"""
    model = Organization
    htmx_table_template_name = "parademgr/partial/table/organizations.htm"
    template_name = "parademgr/full/list/organizations.html"


class ListParades(HtmxOptionMultiView):
    """list available Parade entries"""
    model = Parade
    htmx_table_template_name ="parademgr/partial/table/parades.htm"
    template_name = "parademgr/full/list/parades.html"
