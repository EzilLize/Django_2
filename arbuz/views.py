from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    host = request.META['HTTP_HOST']
    browser = request.META['HTTP_USER_AGENT']
    ip_adress = request.META['REMOTE_ADDR']
    return HttpResponse(f"""Host: {host}<br>
                            Browser: {browser}<br>
                            IP address: {ip_adress}<br>
                        """)


def error(request):
    return HttpResponse("Произошла ошибка", status=400, reason="Incorrect data")


def user(request, login='Arbuz', name='About Arbuz', number='666'):
    return HttpResponse(f"""Login: {login}<br>
                            Post name: {name}<br>
                            Number of post: {number}<br>
                        """)
