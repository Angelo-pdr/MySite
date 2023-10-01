import pytest

from blog.factories import PostFactory

@pytest.fixture
def post_published():
    return PostFactory(title="pytest with factory")

@pytest.mak.django_db
def test_create_publised_post(post_published):
    assert post_published.title == "pytest with factory"
