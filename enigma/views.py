from django.shortcuts import render
from cryptography.fernet import Fernet
from django.conf import settings
from .forms import EnterCode
# Create your views here.
def HomePage(request):
    return render(request,'home.html')

def Enc(request):
    if request.method == 'POST':
        form = EnterCode(request.POST)
        if form.is_valid():
            text = form.cleaned_data['code']
            f=Fernet(settings.ENCRYPT_KEY)
            token = f.encrypt(bytes(text,'utf-8'))
            token=str(token)
            context = {'form': form, 'text': token}
            return render(request, 'encrypt.html', context)
    else:
        form = EnterCode()
        return render(request,'getcode.html',{'form':form})

