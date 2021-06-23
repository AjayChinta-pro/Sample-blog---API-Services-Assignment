import sys
from typing import Any, BinaryIO, Callable, Generator, IO, Iterable, Iterator, List, Optional, Protocol, Text, TextIO, Tuple, Type, TypeVar, Union

from abc import abstractmethod
import types

# TODO: this only satisfies the most common interface, where
# bytes (py2 str) is the raw form and str (py2 unicode) is the cooked form.
# In the long run, both should become template parameters maybe?
# There *are* bytes->bytes and str->str encodings in the standard library.
# They are much more common in Python 2 than in Python 3.

from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/',GraphQLView.as_view(graphiql=True))
]
