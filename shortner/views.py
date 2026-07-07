from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL
import random
import string

domain_name = "http://127.0.0.1:8000/"

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))




def home(request):
    short_url = None
    if request.method == "POST":
        original = request.POST.get("url")
        if original: 
            short_code = generate_short_code()
            obj = ShortURL.objects.create(
                original_url=original,
                short_code=short_code
            )
            short_url = domain_name + short_code + "/"
    return render(request, "shortner/home.html", {
        "short_url": short_url
    })

    
def redirect_url(request, short_code):
    obj = get_object_or_404(ShortURL, short_code=short_code)
    obj.clicks += 1
    obj.save()
    if not obj.original_url.startswith("http"):
        obj.original_url = "https://" + obj.original_url
    return redirect(obj.original_url)



