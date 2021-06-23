import graphene
import api.schema

class Query(api.schema.Query,graphene.ObjectType):
    pass
class Mutation(api.schema.mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)