import graphene
from graphene_django import DjangoObjectType

from .models import Gato


class GatoType(DjangoObjectType):
    class Meta:
        model = Gato


class Query(graphene.ObjectType):
    gatos = graphene.List(GatoType)

    def resolve_gatos(self, info, **kwargs):
        return Gato.objects.all()
    

class CreateGato(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    tipo = graphene.String()
    velocidad = graphene.Int()
    ataque = graphene.Int()
    defensa = graphene.Int()
    counter = graphene.String()
    strong = graphene.String()
    image = graphene.String()

    #2
    class Arguments:
        name = graphene.String()
        tipo = graphene.String()
        velocidad = graphene.Int()
        ataque = graphene.Int()
        defensa = graphene.Int()
        counter = graphene.String()
        strong = graphene.String()
        image = graphene.String()

    #3
    def mutate(self, info, name,tipo,velocidad,ataque,defensa,counter,strong,image):
        gato = Gato(name=name,tipo=tipo,image=image,velocidad=velocidad,ataque=ataque,defensa=defensa,counter=counter,strong=strong)
        gato.save()

        return CreateGato(
            id=gato.id,
            name=gato.name,
            tipo=gato.tipo,
            ataque=gato.ataque,
            defensa=gato.defensa,
            image=gato.image,
            velocidad=gato.velocidad,
            strong=gato.strong,
            counter=gato.counter,

        )


#4
class Mutation(graphene.ObjectType):
    create_gato = CreateGato.Field()


