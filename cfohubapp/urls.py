"""pim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from . import views

urlpatterns = [
    path(
        '',
        views.home,
        name='home'),
    path(
        'one_person_company/',
        views.one_person_company),
    path(
        'limited_liability_company/',
        views.limited_liability_company),
    path(
        'private_limited_company/',
        views.private_limited_company),
    path(
        'pf_esi_payroll/',
        views.pf_esi_payroll),
    path(
        'board_membership/',
        views.board_membership),
    path(
        'board_membership/',
        views.board_membership),
    path(
        'company_lifecycle_compliance/',
        views.company_lifecycle_compliance),
    path(
        'copyright_registration/',
        views.copyright_registration),
    path(
        'corporate_governance/',
        views.corporate_governance),
    path(
        'digital_accounting/',
        views.digital_accounting),
    path(
        'digital_record_keeping/',
        views.digital_record_keeping),
    path(
        'financial_advisory/',
        views.financial_advisory),
    path(
        'funding_advisory/',
        views.funding_advisory),
    path(
        'gst_advisory_board/',
        views.gst_advisory_board),
    path(
        'patent_and_design_registration/',
        views.patent_and_design_registration),
    path(
        'reporting_and_audits/',
        views.reporting_and_audits),
    path(
        'roc_compliance/',
        views.roc_compliance),
    path(
        'tax_compliance/',
        views.tax_compliance),
    path(
        'trademark_registration/',
        views.trademark_registration)
    
]