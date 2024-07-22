""" report like pages for app models and data """

# from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from handyhelpers.views.report import AnnualTrendView, AnnualStatView, AnnualProgressView

# from handyhelpers.views.report import get_colors

# import models
from parademgr.models import (Award, Organization, Parade)


class ParademgrDashboard(View):
    """parademgr dashboard"""

    template_name = "parademgr/custom/dashboard.html"

    def get(self, request):
        """render dashboard for parademgr specific data"""
        context = {"title": "Parademgr Dashboard"}
        return render(request, self.template_name, context=context)


class ParademgrAnnualProgressView(AnnualProgressView):
    """ """

    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/storemgr/list_models",
        # ),
    ]


class ParademgrAnnualStatView(AnnualStatView):
    """ """

    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/storemgr/list_models",
        # ),
    ]


class ParademgrAnnualTrendView(AnnualTrendView):
    """ """

    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/storemgr/list_models",
        # ),
    ]
