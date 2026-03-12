import pytest
from flashcards.models import Category, Entry
from .factories import CategoryFactory, EntryFactory

@pytest.mark.django_db
def test_category_str():
    category = CategoryFactory(name="Test Category")
    assert str(category) == "Test Category"

@pytest.mark.django_db
def test_entry_str():
    entry = EntryFactory(term="Apple")
    assert str(entry) == "Apple"

@pytest.mark.django_db
def test_category_entries_relation():
    category = CategoryFactory()
    entry1 = EntryFactory(category=category)
    entry2 = EntryFactory(category=category)
    assert category.entries.count() == 2
    assert entry1.category == category
    assert entry2.category == category