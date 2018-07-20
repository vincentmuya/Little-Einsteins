from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name ='index'),
    url(r'^program/$',views.program,name='program'),
    url(r'^about/$',views.about,name='about'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^enroll/$',views.enroll,name='enroll'),
    url(r'^sponsor/$',views.sponsor,name='sponsor'),
    url(r'^location/$',views.location,name='location'),
    url(r'^annual/$',views.annual,name='annual'),
    url(r'^annual2018/$',views.annual2018,name='annual2018'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    ]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
