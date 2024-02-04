from .models import *

def contactInfo(request):
    g_contactInfo = ContactInfo.objects.all()

    context = {
        'g_contactInfo':g_contactInfo
    }

    return context 