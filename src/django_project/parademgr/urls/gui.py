from django.urls import path, re_path
from parademgr.views import gui
from parademgr.views import report


urlpatterns = [
    # GUI views
    # path("", gui.Index.as_view(), name=""),
    # path("index", gui.Index.as_view(), name="index"),
    # path("default", gui.Index.as_view(), name="default"),
    # path("home", gui.Index.as_view(), name="home"),
    # list views
    # path("list_mymodels/", gui.ListMymodels.as_view(), name="list_mymodels"),

    path("admin/", gui.Admin.as_view(), name="admin"),

    # list views
    path("awards/filter/", gui.FilterAwardModalView.as_view(), name="filter_awards"),
    re_path("^awards/(?P<display>\w+)?/$", gui.ListAwards.as_view(), name="list_awards"),
    path("awards/", gui.ListAwards.as_view(), name="awards"),

    re_path("^award_types/(?P<display>\w+)?/$", gui.ListAwardTypes.as_view(), name="list_award_types"),
    path("award_types/", gui.ListAwardTypes.as_view(), name="award_types"),

    re_path("^categories/(?P<display>\w+)?/$", gui.ListCategories.as_view(), name="list_categories"),
    path("categories/", gui.ListCategories.as_view(), name="categories"),

    path("divisions/filter/", gui.FilterDivisionModalView.as_view(), name="filter_divisions"),
    re_path("^divisions/(?P<display>\w+)?/$", gui.ListDivisions.as_view(), name="list_divisions"),
    path("divisions/", gui.ListDivisions.as_view(), name="divisions"),

    path("organizations/filter/", gui.FilterOrganizationModalView.as_view(), name="filter_organizations"),
    re_path("^organizations/(?P<display>\w+)?/$", gui.ListOrganizations.as_view(), name="list_organizations"),
    path("organizations/", gui.ListOrganizations.as_view(), name="organizations"),

    re_path("^parades/(?P<display>\w+)?/$", gui.ListParades.as_view(), name="list_parades"),
    path("parades/", gui.ListParades.as_view(), name="list_parades"),

    # detail views
    # path("detail_mymodel/<int:pk>", gui.DetailMymodel.as_view(), name="detail_mymodel"),
    path("parades/<int:pk>", gui.DetailParade.as_view(), name="detail_parade"),
    path("organizations/<int:pk>", gui.DetailOrganization.as_view(), name="detail_organization"),


    # hmtx partials (modals)
    path("create_award/", gui.CreateAwardModalView.as_view(), name="create_award"),
    path("create_awardtype/", gui.CreateAwardTypeModalView.as_view(), name="create_awardtype"),
    path("create_category/", gui.CreateCategoryModalView.as_view(), name="create_category"),
    path("create_division/", gui.CreateDivisionModalView.as_view(), name="create_division"),
    path("create_parade/", gui.CreateParadeModalView.as_view(), name="create_parade"),

    # path("filter_awards/", gui.FilterAwardModalView.as_view(), name="filter_awards"),
    # path("filter_organizations/", gui.FilterOrganizationModalView.as_view(), name="filter_organizations"),


    # report views
    path("dashboard/", report.ParademgrDashboard.as_view(), name="dashboard"),
    path("annual_progress/", report.ParademgrAnnualProgressView.as_view(), name="annual_progress"),
    path("annual_stats/", report.ParademgrAnnualStatView.as_view(), name="annual_stats"),
    path("annual_trends/", report.ParademgrAnnualTrendView.as_view(), name="annual_trends"),

    path("test/", gui.Test.as_view(), name="test"),

]
