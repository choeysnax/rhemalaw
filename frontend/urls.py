from django.urls import path, include
from django_distill import distill_path

from frontend import views
from frontend.types import UrlMap

app_name = 'frontend'

urls_maps: list[UrlMap] = [{
    'url': '',
    'view': views.index_view,
    'name': 'index',
    'distill_file': 'index.html',
}, {
    'url': 'about',
    'view': views.about,
    'name': 'about',
    'distill_file': 'about.html'
}, {
    'url': 'contact',
    'view': views.contact_view,
    'name': 'contact',
    'distill_file': 'contact.html'
}, {
    'url': 'our-team',
    'view': views.our_team,
    'name': 'our-team',
    'distill_file': 'our-team.html'
}, {
    'url': 'insights',
    'view': views.insights,
    'name': 'insights',
    'distill_file': 'insights.html'
}, {
    'url': 'areas-of-practice/',
    'view': views.areas_of_practice,
    'name': 'areas-of-practice-index',
    'distill_file': 'areas-of-practice/index.html'
}, {
    'url': 'areas-of-practice/<slug:slug>',
    'view': views.areas_of_practice,
    'name': 'areas-of-practice-tab',
    'distill_file': 'areas-of-practice/{}.html',
    'distill_func': views.get_areas_of_practice_list,
}]

static_page_urlpatterns = []

for url_map in urls_maps:
    static_page_urlpatterns.append(path(url_map['url'], url_map['view'], name=url_map['name']))

    distill_path_kwargs = {
        'name': url_map['name'],
    }
    if url_map.get('distill_file'):
        distill_path_kwargs['distill_file'] = url_map['distill_file']
    if url_map.get('distill_func'):
        distill_path_kwargs['distill_func'] = url_map['distill_func']
    static_page_urlpatterns.append(
        distill_path(
            url_map['url'],
            url_map['view'],
            **distill_path_kwargs,
        )
    )


urlpatterns = [
    path('', include(static_page_urlpatterns)),
]