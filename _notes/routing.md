## URL dispatcher Root_URLconf
    map URL patterns to Views
    
## URL Patterns
    urls.py
    urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^item/(?P<id>\d+)', views.item_detail, name='item_detail'),
    
        url(r'^admin/', admin.site.urls),
    ]
## Online python regex tool
    pythex.org