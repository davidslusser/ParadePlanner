""" report like pages for app models and data """

# from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from handyhelpers.views.report import (
    AnnualProgressView,
    AnnualStatView,
    AnnualTrendView,
)

# import models

# from handyhelpers.views.report import get_colors


class ParademgrDashboard(View):
    """parademgr dashboard"""

    template_name = "parademgr/custom/dashboard.html"

    def get(self, request):
        """render dashboard for parademgr specific data"""
        context = {"title": "Parademgr Dashboard"}
        return render(request, self.template_name, context=context)


class ParademgrAnnualProgressView(AnnualProgressView):
    """ """

    dataset_list: list = [
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

    dataset_list: list = [
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

    dataset_list: list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/storemgr/list_models",
        # ),
    ]
