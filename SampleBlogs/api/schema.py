import graphene
from graphene_django.types import DjangoObjectType
from .models import Blogs


class BlogType(DjangoObjectType):
    class Meta:
        model = Blogs

# class AutherType(DjangoObjectType):
#     class Meta:
#         model = Auther


class Query(graphene.ObjectType):
    all_blogs=graphene.List(BlogType)
    blog=graphene.Field(BlogType,title=graphene.String())

    # all_authers = graphene.List(AutherType)
    #
    # def resolve_all_authers(self, info, **kwargs):
    #     return Auther.objects.all()

    def resolve_all_blogs(self,info,**kwargs):
        return Blogs.objects.all()

    def resolve_blog(self,info,**kwargs):

        title=kwargs.get('id')


        if id is not  None:
            return Blogs.object.get(id=id)
        else:
            return None


class BlogCreateMutation(graphene.Mutation):
    class Arguments:
        title=graphene.String(required=True)
        description= graphene.String(required=True)
        published_date = graphene.Date(required=True)
        auther=graphene.String(required=True)

    blog=graphene.Field(BlogType)
    def mutate(self,info,title,description,published_date,auther):
        blog=Blogs.objects.create(title=title,description=description,published_date=published_date,auther=auther)

        return BlogCreateMutation(blog=blog)

class BlogUpdateMutation(graphene.Mutation):
    class Arquments:
        title=graphene.String(required=True)
        description=graphene.String(required=True)
        published_date = graphene.Date(required=True)
        auther = graphene.String(required=True)
        id=graphene.ID(required=True)

    blog=graphene.Field(BlogType)
    def mutate(self,info,title,description,published_date):
        blog=Blogs.objects.get(pk=id)

        if title is not None:
            blog.title=title
        if description is not None:
            blog.description=description
        if published_date is not None:
            blog.published_date = published_date
        blog.save()

        return BlogUpdateMutation(blog=blog)

class BlogDeleteMutation(graphene.Mutation):
    class Arquments:
        id=graphene.ID(required=True)

    blog=graphene.Field(BlogType)
    def mutate(self,info,id):
        blog=Blogs.objects.get(pk=id)
        blog.delete()

        return BlogDeleteMutation(blog=blog)
class mutation:
    create_blog=BlogCreateMutation.Field()
    update_blog=BlogUpdateMutation.Field()
    delete_blog=BlogDeleteMutation.Field()