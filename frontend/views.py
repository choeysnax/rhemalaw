from django.shortcuts import render

areas_of_practice_list = [
    {
        'title': 'Commercial Law',
        'texts': [
            '1. Mergers and acquisitions',
            '2. Corporate and commercial contracts',
            '3. Shareholders agreements',
            '4. Partnership agreements',
            '5. Joint ventures',
            '6. Franchising agreements',
            '7. Business restructuring',
            '8. Start - ups.',
            '9. Employment law issues.',
            '10. Penetration into the energy and oil and gas sectors.',
            '11. Liquidation.'
        ],
        'slug': 'commercial-law'
    },
    {
        'title': 'Employment Law',
        'texts': [
            '1. Negotiation of terms of employment',
            '2. Drafting of contracts of employment',
            '3. Drafting of employee manuals',
            '4. Negotiation and drafting of collective bargaining agreements',
            '5. Severance',
            '6. Representation at the Labour Commission',
        ],
        'slug': 'employment-law'
    },
    {
        'title': 'Conveyancing',
        'texts': [
            '1. Land sales and acquisition',
            '2. Residential Conveyancing',
            '3. Commercial Conveyancing',
            '4. Landlord and Tenant'
        ],
        'slug': 'conveyancing'
    },
    {
        'title': 'Wills and Probate',
        'texts': [
            '1. Wills and estate planning',
            '2. Probate and administration of estates',
            '3. Vesting assents.'
        ],
        'slug': 'wills-and-probate'
    },
    {
        'title': 'Immigration',
        'texts': [
            'We advise businesses and individuals on all aspects of Ghanaian and UK immigration law.'
        ],
        'slug': 'immigration'

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
