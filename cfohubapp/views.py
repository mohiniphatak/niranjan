from django.shortcuts import render, redirect

from cfohubapp.forms import SignUpForm
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'cfohubapp/signup.html', {'form': form})

def home(request):
    return render(request, 'cfohubapp/main.html', {})

def one_person_company(request):
    return render(request, 'cfohubapp/one-person-company.html', {})

def limited_liability_company(request):
    return render(request, 'cfohubapp/limited-liability-company.html', {})

def private_limited_company(request):
    return render(request, 'cfohubapp/private-limited-company.html', {})

def pf_esi_payroll(request):
    return render(request, 'cfohubapp/pf-esi-payroll.html', {})

def board_membership(request):
    return render(request, 'cfohubapp/board-membership.html', {})

def company_lifecycle_compliance(request):
    return render(request, 'cfohubapp/company-lifecycle-compliance.html', {})

def copyright_registration(request):
    return render(request, 'cfohubapp/copyright-registration.html', {})

def corporate_governance(request):
    return render(request, 'cfohubapp/corporate-governance.html', {})

def digital_accounting(request):
    return render(request, 'cfohubapp/digital-accounting.html', {})

def digital_record_keeping(request):
    return render(request, 'cfohubapp/digital-record-keeping.html', {})

def financial_advisory(request):
    return render(request, 'cfohubapp/financial-advisory.html', {})

def funding_advisory(request):
    return render(request, 'cfohubapp/funding-advisory.html', {})

def gst_advisory_board(request):
    return render(request, 'cfohubapp/gst-advisory-board.html', {})

def patent_and_design_registration(request):
    return render(request, 'cfohubapp/patent-and-design-registration.html', {})

def reporting_and_audits(request):
    return render(request, 'cfohubapp/reporting-and-audits.html', {})

def roc_compliance(request):
    return render(request, 'cfohubapp/roc-compliance.html', {})

def tax_compliance(request):
    return render(request, 'cfohubapp/tax-compliance.html', {})

def trademark_registration(request):
    return render(request, 'cfohubapp/trademark-registration.html', {})

def registered_transfer_agent_service(request):
    return render(request, 'cfohubapp/registered-transfer-agent-service.html', {})