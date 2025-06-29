from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.

books_list = [ 
   {
      "index" :0,
      "id" : 1,
      "name" : "Head first python",
      "priority" :1,
      "description":"Learning python "

   },
      {
      "index" :1,
      "id" : 2,
      "name" : "Head first java",
      "priority" :2,
      "description":"Learning java "

   },    
       {
      "index" :2,
      "id" : 3,
      "name" : "Head first kotlin",
      "priority" :3,
      "description":"Learning kotlin "

   },
]

def index (request):
   print(request)
   return render(request,'books/index.html',context={'name':'Ahmed','age':24})


def show_books_list(request):
   context= {
      "books_list" : books_list
   }
   return render(request,"books/books_list.html", context=context)



def _get_book_id(book_id):
  for book in books_list:
     id= book.get('id')
     if id and id== book_id:
        return book 
  return None

def book_details(request,**kwargs):
   book_id=kwargs.get("book_id")
   book = _get_book_id(book_id)
  
   my_context=  {
      'book_id': book['id'],
      'book_name': book['name'],
   'book_priority': book['priority'],

      'book_description': book['description']
   }
   return render(request,'books/book_details.html',context=my_context)

def delete_book (request,**kwargs):
   book_id=kwargs.get("book_id")
   book= _get_book_id(book_id)
   if books_list:
      books_list.remove(book)
   return redirect("bookstore:book_store-index")


def update_book(request, book_id):
    book = _get_book_id(book_id)
    if not book:
        return HttpResponse("Book not found", status=404)

    if request.method == "POST":
        if form.is_valid():
            book["name"] = request.POST.get("name")
            book["description"] =  request.POST.get("description")
            book["priority"] =  request.POST.get("priority")
            return redirect("bookstore:book_store-index")

    return render(request, "books/book_update.html", {"book": book})
book_id_counter = 4  


def add_book(request):
    global book_id_counter 

    if request.method == "POST":
           name = request.POST.get("name")
           description =  request.POST.get("description")
           priority =  request.POST.get("priority")
           new_book={
               "index":len(books_list),
               "id":book_id_counter,
               "name":name,
               "description":description,
               "priority": priority
              }
           books_list.append(new_book)
           book_id_counter+=1
           return redirect("bookstore:book_store-index")

    return render(request, "books/book_update.html")
