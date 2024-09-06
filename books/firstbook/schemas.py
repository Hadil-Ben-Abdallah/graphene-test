import graphene
import graphene_django
from .models import Book

class BookType(graphene_django.DjangoObjectType):
  class Meta:
    model = Book
    fields = '__all__'



class Query(graphene.ObjectType):
  books = graphene.List(BookType)

  def resolve_books(self, info):
    return Book.objects.all()



class CreateBook(graphene.Mutation):
  book = graphene.Field(BookType)

  class Arguments:
    title = graphene.String()
    author = graphene.String()

  def mutate(self, info, title, author):
    book = Book(title=title, author=author)
    book.save()
    return CreateBook(book=book)



class UpdateBook(graphene.Mutation):
  ok = graphene.Boolean()
  book = graphene.Field(BookType)

  class Arguments:
    book_id = graphene.ID()
    title = graphene.String()
    author = graphene.String()

  def mutate(self, info, book_id, title, author):
    book = Book.objects.get(book_id=book_id)
    book.title = title
    book.author = author
    book.save()
    return UpdateBook(ok=True, book=book)



class DeleteBook(graphene.Mutation):
  ok = graphene.Boolean()

  class Arguments:
    book_id = graphene.ID()

  def mutate(self, info, book_id):
    book = Book.objects.get(book_id=book_id)
    book.delete()
    return DeleteBook(ok=True)



class Mutation(graphene.ObjectType):
  create_book = CreateBook.Field()
  update_book = UpdateBook.Field()
  delete_book = DeleteBook.Field()
