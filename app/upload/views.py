from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse


def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return render(request, "upload.html")


def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    print('x_forwarded_for:', x_forwarded_for)

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    print('X_FORWARDED_FOR:', x_forwarded_for)
    print('IP:', ip)
    print('META:', request.META)
    # remote_host = request.META['REMOTE_HOST']
    # http_host = request.META['HTTP_HOST']

    secure_str = 'secure' if request.is_secure() else 'insecure'
    msg = f'Your ip is {ip}. Your connection is {secure_str} Meta: {request.META}'
    return HttpResponse(msg)