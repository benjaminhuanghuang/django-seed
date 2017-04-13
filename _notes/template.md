## settings
    TEMPLATES = [
        {
            ...
            'DIRS': ['django_proj/templates'],
        },
    ]
    
## Use template in views
    items = Items.objects.exclude(quantity=0)
    return render(request, 'django_app/index.html', {'items': items})
