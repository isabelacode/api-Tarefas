from django.http import HttpResponse

def simple_test(request):
    return HttpResponse("Test OK", content_type="text/plain")
