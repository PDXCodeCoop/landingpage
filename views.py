from django.shortcuts import render_to_response
from django.template.context import RequestContext

from models import Template
# Create your views here.
def index(request):
    try:
        template = Template.objects.filter(active=True)[0]
        args = {"template":template}
    except IndexError:
        args = {}
    return render_to_response("landingpage/index.html", RequestContext(request, args))
