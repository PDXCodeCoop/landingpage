from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.
def index(request):
    args = {}
    return render_to_response("landingpage/index.html", RequestContext(request, args))
