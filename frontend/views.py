from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

from frontend.forms import ContactForm

areas_of_practice_list = [
    {
        'title': 'Commercial Law',
        'texts': [
            'Mergers and acquisitions',
            'Corporate and commercial contracts',
            'Shareholders agreements',
            'Partnership agreements',
            'Joint ventures',
            'Franchising agreements',
            'Business restructuring',
            'Start-ups',
            'Energy',
            'Oil and Gas'
        ],
        'slug': 'commercial-law'
    },
    {
        'title': 'Employment Law',
        'texts': [
            'Negotiation of terms of employment',
            'Drafting of contracts of employment',
            'Drafting of employee manuals',
            'Negotiation and drafting of collective bargaining agreements',
            'Severance',
            'Redundancies',
            'Representation at the Labour Commission',
        ],
        'slug': 'employment-law'
    },
    {
        'title': 'Conveyancing',
        'texts': [
            'Land sales and acquisition',
            'Residential Conveyancing',
            'Commercial Conveyancing',
            'Landlord and Tenant'
        ],
        'slug': 'conveyancing'
    },
    {
        'title': 'Wills and Probate',
        'texts': [
            'Wills and estate planning',
            'Probate and administration of estates',
            'Vesting assents',
            'Letters of administration'
        ],
        'slug': 'wills-and-probate'
    },
    {
        'title': 'Other services',
        'texts': [
            {
                'text': 'Entities Registration',
                'link': f'{settings.OXFORD_HOST}/services/entities-registration'
            },
            {
                'text': 'Company Secretarial',
                'link': f'{settings.OXFORD_HOST}/services/company-secretarial'
            },
            {
                'text': 'Tax Advisory & Allied Services',
                'link': f'{settings.OXFORD_HOST}/services/tax-advisory-allied-services'
            },
            {
                'text': 'Corporate Governance',
                'link': f'{settings.OXFORD_HOST}/services/corporate-governance'
            },
            {
                'text': 'Compliance',
                'link': f'{settings.OXFORD_HOST}/services/compliance'
            },
            {
                'text': 'Immigration',
                'link': f'{settings.OXFORD_HOST}/services/immigration'
            },
            {
                'text': 'Shelf companies',
                'link': f'{settings.OXFORD_HOST}/services/shelf-companies'
            },
            {
                'text': 'Liquidation',
                'link': f'{settings.OXFORD_HOST}/services/liquidation'
            },
            {
                'text': 'Translation',
                'link': f'{settings.OXFORD_HOST}/services/translation'
            },
            {
                'text': 'Nominee Services',
                'link': f'{settings.OXFORD_HOST}/services/nominee-services'
            },
            {
                'text': 'Human Resources',
                'link': f'{settings.OXFORD_HOST}/services/human-resources'
            },
        ],
        'slug': 'other-services'

    },
]


def get_areas_of_practice_list():
    for area in areas_of_practice_list:
        yield area['slug']


def index_view(request):
    context = {
        'index': True,
        'areas_of_practice': areas_of_practice_list
    }
    return render(request, 'frontend/index.html', context)


def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            send_mail(
                f"[ContactPage] {contact_form.cleaned_data.get('subject')}",
                f"Name: {contact_form.cleaned_data.get('name')}\n"
                f"Email: {contact_form.cleaned_data.get('email')}\n"
                f"Phone: {contact_form.cleaned_data.get('phone')}\n\n"
                f"Message: {contact_form.cleaned_data.get('message')}\n",
                'contact-us-page@rhemalawgh.com',
                ['akuaa@rhemalawgh.com'],
                fail_silently=False,
            )
            messages.success(request, 'Message has successfully been submitted')
        pass
    else:
        contact_form = ContactForm()
    context = {
        'contact_form': contact_form
    }
    return render(request, 'frontend/contact.html', context)


def areas_of_practice(request, slug=None):
    current_area = areas_of_practice_list[0]
    try:
        for area in areas_of_practice_list:
            if area['slug'] == slug:
                current_area = area
    except:
        pass
    context = {
        'areas_of_practice': areas_of_practice_list,
        'current_area': current_area
    }
    return render(request, 'frontend/areas_of_practice.html', context)


def about(request):
    return render(request, 'frontend/about.html')


def our_team(request):
    return render(request, 'frontend/our_team.html')


def insights(request):
    insights = []
    return render(request, 'frontend/insights.html', {'insights': insights})