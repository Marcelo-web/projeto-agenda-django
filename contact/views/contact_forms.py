from django.shortcuts import render


def create(request):
    if request.method == 'POST':
        print(request.method)
        print(request.POST.get('first_name'))

    context = {
    }

    print(request.method)

    return render(
        request,
        'contact/create.html',
        context
    )
