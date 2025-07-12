from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
# Create your views here.

# books_list = [ 
#    {
#       "index" :0,
#       "id" : 1,
#       "name" : "Head first python",
#       "priority" :1,
#       "description":"Learning python "

#    },
#       {
#       "index" :1,
#       "id" : 2,
#       "name" : "Head first java",
#       "priority" :2,
#       "description":"Learning java "

#    },    
#        {
#       "index" :2,
#       "id" : 3,
#       "name" : "Head first kotlin",
#       "priority" :3,
#       "description":"Learning kotlin "

#    },
# ]

def index (request):
   print(request)
   return render(request,'books/index.html',context={'name':'Ahmed','age':24})


def show_books_list(request):
   all_books=Book.objects.all()
   print(all_books)
   return render(request,"books/books_list.html", context={
       "books" : all_books
   })





def book_details(request,pk):
   book = Book.objects.get(pk=pk)
   return render(request,'books/book_details.html',context={"book":book})

def delete_book (request,pk):

   Book.objects.get(pk=pk).delete()

   return redirect("bookstore:book_store-index")


# def update_book(request, pk):
#     book = Book.objects.get(pk=pk)
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return HttpResponse("Book not found", status=404)

#     if request.method == "POST":
   
#             book.name = request.POST.get("name")
#             book.description =  request.POST.get("description")
#             book.rate =  request.POST.get("rate")
#             book.save
#             return redirect("bookstore:book_store-index")
              
#     return render(request, "books/book_update.html", {"book": book})



# def add_book(request):

#     if request.method == "POST":
#            name = request.POST.get("name")
#            description =  request.POST.get("description")
#            rate =  request.POST.get("rate")
         
#            Book.objects.create(name=name,description=description,views=2222,rate=rate)
#            return redirect("bookstore:book_store-index")

#     return render(request, "books/book_update.html")

def add_book(request):
   form=BookForm()
   if request.method == "POST":
      form=BookForm(data=request.POST)
      if form.is_valid():
           form.save()
           return redirect("bookstore:book_store-index")

   return render(request, "books/book_update.html",context={
         "form":form
   })

def update_book(request, pk):
    book = Book.objects.get(pk=pk)

    form = BookForm(instance=book)
    if request.method == "post":
         form = BookForm(instance=book,data=request.POST)
         if form.is_valid():
             form.save()
             return redirect("bookstore:book_store-index")
              
    return render(request, "books/book_update.html",
                   {"form":form,
                                                      "book": book})

