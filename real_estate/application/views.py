from django.shortcuts import render, get_object_or_404

from application.models import Property


def contact_info(request):
    return render(request, 'contact_info.html')


def property_list(request):
    properties = Property.objects.all()
    return render(request,
                  template_name="application_listing.html",
                  context={"properties": properties})


def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    return render(request,
                  template_name="detail.html",
                  context={"property": property_obj})
