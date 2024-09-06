import graphene
import firstbook.schemas

class Query(firstbook.schemas.Query, graphene.ObjectType):
  pass

class Mutation(firstbook.schemas.Mutation, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)