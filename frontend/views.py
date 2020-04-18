from django.shortcuts import render
from django.conf import settings
from frontend.models import Insight

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


# Create your views here.
def index_view(request):
    context = {
        'areas_of_practice': areas_of_practice_list
    }
    return render(request, 'frontend/index.html', context)


def about_view(request):
    return render(request, 'frontend/about.html')


def contact_view(request):
    return render(request, 'frontend/contact.html')


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


def rhema_team(request):
    return render(request, 'frontend/rhema_team.html')


def insights_view(request):
    context = {
        'insights': Insight.objects.filter(is_active=True)
    }
    return render(request, 'frontend/insights.html', context)
