from django.shortcuts import render, reverse
from django.views.generic import DetailView, View, TemplateView
from django.http import HttpResponse

from handyhelpers.permissions import InAnyGroup
from handyhelpers.views import HandyHelperIndexView, HandyHelperListPlusCreateAndFilterView
from handyhelpers.views.htmx import (HtmxOptionMultiView, HtmxOptionDetailView, HtmxOptionMultiFilterView, HtmxItemizedView, HtmxPostForm, BuildBootstrapModalView, CreateModelModalView)

# import models
from parademgr.models import (Award, AwardType, Category, Division, Organization, Parade)

# import forms
from parademgr.forms.create import (AwardForm, AwardTypeForm, CategoryForm, DivisionForm, OrganizationForm, ParadeForm)


class Admin(HtmxItemizedView):
    """render the project index page"""
    template_name = "parademgr/full/custom/admin.html"
    htmx_template_name = "parademgr/partial/component/admin.htm"

    title = """<span class="text-primary">Parade Planner</span> <span class="text-secondary">Admin</span>"""
    subtitle = "Select an option below"
    item_list = [
        {
            "url": "/parademgr/create_award/",
            "icon": "fa-solid fa-award",
            "title": "Add Award",
            "description": "Add a new award",
        },
        {
            "url": "/parademgr/create_awardtype/",
            "icon": "fa-solid fa-certificate",
            "title": "Add Award Type",
            "description": "Add a new reward type",
        },
        {
            "url": "/parademgr/create_category/",
            "icon": "fas fa-table-list",
            "title": "Add Category",
            "description": "Add a new parade category",
        },
        {
            "url": "/parademgr/create_division",
            "icon": "fa-solid fa-users-rectangle",
            "title": "Add Division",
            "description": "Add a new parade division",
        },
        {
            "url": "/parademgr/create_parade/",
            "icon": "fa-regular fa-map",
            "title": "Create Parade",
            "description": "Create a new parade",
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


class CreateAwardModalView(CreateModelModalView):
    """Create a new Award entry"""
    form = AwardForm


class CreateAwardTypeModalView(CreateModelModalView):
    """Create a new AwardType entry"""
    form = AwardTypeForm


class CreateCategoryModalView(CreateModelModalView):
    """Create a new Category entry"""
    form = CategoryForm


class CreateDivisionModalView(CreateModelModalView):
    """Create a new Division entry"""
    form = DivisionForm


class CreateOrganization(CreateModelModalView):
    """Create a new Organization entry"""
    form = OrganizationForm


class CreateParadeModalView(CreateModelModalView):
    """Create a new Parade entry"""
    form = ParadeForm
