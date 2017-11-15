from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from models import *
# the index function is called when root is visited
def index(request):
    # Books.objects.create(name='C sharp',desc='')
    # Books.objects.create(name='Ruby')
    # Books.objects.create(name='Java',desc='')
    # Books.objects.create(name='Python',desc='')
    # Books.objects.create(name='PhP',desc='')
    # Authors.objects.all().delete()
    # Authors.objects.create(first_name='Mike')
    # Authors.objects.create(first_name='Speros',last_name='',email='')
    # Authors.objects.create(first_name='John',last_name='',email='')
    # Authors.objects.create(first_name='Jadee',last_name='',email='')
    # Authors.objects.create(first_name='Jay',last_name='',email='')

    # b5=Books.objects.filter(name='C sharp')[0]
    # b5.name='C#'
    # b5.save()
    # a5=Authors.objects.last()
    # a5.first_name='Ketul'
    # a5.save()
    b1=Books.objects.filter(id=1)[0]
    b2=Books.objects.filter(id=2)[0]
    b3=Books.objects.filter(id=3)[0]
    b4=Books.objects.filter(id=4)[0]
    b5=Books.objects.filter(id=5)[0]
    a1=Authors.objects.filter(id=16)[0]
    a2=Authors.objects.get(id=17)
    a3=Authors.objects.get(id=18)
    a4=Authors.objects.get(id=19)
    a5=Authors.objects.get(id=20)

    # b1.authors.add(a1)
    # b2.authors.add(a1)
    # b1.authors.add(a2)
    # b2.authors.add(a2)
    # b3.authors.add(a2)
    # b1.authors.add(a3)
    # b2.authors.add(a3)
    # b3.authors.add(a3)
    # b4.authors.add(a3)
    # b1.authors.add(a4)
    # b2.authors.add(a4)
    # b3.authors.add(a4)
    # b4.authors.add(a4) 
    # b5.authors.add(a4)
    print Books.objects.get(id=3).authors.all()

    # authors=Authors.objects.all()
    # authors=Books.objects.get(id=3).authors.all()
    # authors=[Books.objects.get(id=3).authors.first()]

            # ax=Books.objects.get(id=3).authors.first()

    # b3.authors.remove(a1)
    # b3.save
    # b2.authors.add(a5)
    # b2.save()
    # authors=b2.authors.all()
    authors=Authors.objects.all()
    books=a3.books.all()
    context={
        'authors': authors,
        'books': books
    }
    #return HttpResponse(response)
    return render(request,'books_authors/index.html',context)
