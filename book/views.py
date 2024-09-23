from rest_framework.response import Response
from rest_framework.decorators import api_view

from book.serializer import BookSerializer
from book.models import Book

@api_view(['GET'])
def book_list(request):
    # Tüm kitapları modelden çekiyoruz
    books = Book.objects.all()
    
    # Kitapları serialize ediyoruz
    result = BookSerializer(books, many=True)
    
    # Serialize edilmiş veriyi dönüyoruz
    return Response(result.data)


@api_view(['POST'])
def book_create(request):
    print("request.data: ", request.data)
    
    # Gelen veriyi serialize ediyoruz
    serializer = BookSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()  # Veriyi kaydediyoruz
        return Response(serializer.data)  # Başarılı veriyi döndürüyoruz
    return Response(serializer.errors)  # Hataları döndürüyoruz


@api_view(['GET'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=404)
    
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['PUT'])
def book_update(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=404)
    
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def book_delete(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=404)
    
    book.delete()
    return Response(status=204)