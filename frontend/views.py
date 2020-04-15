from django.shortcuts import render

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
                'link': 'Entities Registration'
            },
            {
                'text': 'Company Secretarial',
                'link': ''
            },
            {
                'text': 'Tax Advisory & Allied Services',
                'link': ''
            },
            {
                'text': 'Corporate Governance',
                'link': ''
            },
            {
                'text': 'Compliance',
                'link': ''
            },
            {
                'text': 'Immigration',
                'link': ''
            },
            {
                'text': 'Shelf companies',
                'link': ''
            },
            {
                'text': 'Liquidation',
                'link': ''
            },
            {
                'text': 'Translation',
                'link': ''
            },
            {
                'text': 'Nominee Services',
                'link': ''
            },
            {
                'text': 'Human Resources',
                'link': ''
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
    return render(request, 'frontend/insights.html')
