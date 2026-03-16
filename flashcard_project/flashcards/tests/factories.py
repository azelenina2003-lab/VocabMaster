import factory
from django.contrib.auth.models import User
from flashcards.models import Category, Entry

# новая фабрика для пользователя
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    description = factory.Faker('sentence')

class EntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Entry

    term = factory.Faker('word')
    definition = factory.Faker('sentence')
    category = factory.SubFactory(CategoryFactory)