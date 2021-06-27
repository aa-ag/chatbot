############----------- IMPORTS -----------############
from django.http import HttpResponse


############----------- VIEW(S) -----------############
def test(request):
    return HttpResponse("Hello, world")