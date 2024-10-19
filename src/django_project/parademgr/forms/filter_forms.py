from django import forms
from handyhelpers.forms import HtmxForm

# import models
from parademgr.models import (Award, AwardType, Category, Division, Organization, Parade)


base_choices = [(None, "--------")]


class AwardFilterForm(HtmxForm):
    """ """
    modal_url = "/parademgr/awards/filter/"
    hx_post_url = "/parademgr/awards/"

    def __init__(self, *args, **kwargs):
        super(AwardFilterForm, self).__init__(*args, **kwargs)

    name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Name"
    )
    award_type = forms.ModelChoiceField(
        queryset=AwardType.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Award Type",
    )
    division = forms.ModelChoiceField(
        queryset=Division.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Division",
    )


class DivisionFilterForm(HtmxForm):
    modal_url = "/parademgr/divisions/filter/"
    hx_post_url = "/parademgr/divisions/"

    def __init__(self, *args, **kwargs):
        super(DivisionFilterForm, self).__init__(*args, **kwargs)

    name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Name"
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
        label="Category",
    )


class OrganizationFilterForm(HtmxForm):
    modal_url = "/parademgr/organizations/filter/"
    hx_post_url = "/parademgr/organizations/"

    def __init__(self, *args, **kwargs):
        super(OrganizationFilterForm, self).__init__(*args, **kwargs)

    name__icontains = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}), required=False, label="Name"
    )