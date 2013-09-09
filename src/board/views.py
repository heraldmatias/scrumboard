from django.shortcuts import render_to_response
from django.template.context import RequestContext
from core.decorators import render_template
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/')
@render_template
def app(request):
    return "board/app.html"

@login_required(login_url='/admin/')
@render_template
def home(request):
    return "index.html"