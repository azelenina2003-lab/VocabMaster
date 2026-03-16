import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .factories import UserFactory

@pytest.mark.django_db
def test_register_view_get(client):
    """GET запрос на регистрацию возвращает форму."""
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200
    assert 'form' in response.context

@pytest.mark.django_db
def test_register_view_post_success(client):
    """Успешная регистрация создаёт пользователя и выполняет вход."""
    url = reverse('register')
    data = {
        'username': 'newuser',
        'email': 'new@example.com',
        'password1': 'TestPass123',
        'password2': 'TestPass123',
    }
    response = client.post(url, data)
    # После успешной регистрации должен быть переход на category_list
    assert response.status_code == 302
    assert response.url == reverse('category_list')
    # Проверка, что пользователь создан
    assert User.objects.filter(username='newuser').exists()
    # Проверка, что пользователь аутентифицирован 
    assert '_auth_user_id' in client.session

@pytest.mark.django_db
def test_register_view_post_password_mismatch(client):
    """Если пароли не совпадают, форма не валидна."""
    url = reverse('register')
    data = {
        'username': 'newuser',
        'email': 'new@example.com',
        'password1': 'TestPass123',
        'password2': 'DifferentPass',
    }
    response = client.post(url, data)
    assert response.status_code == 200  # в этом случае остаёмся на странице регистрации
    assert 'form' in response.context
    assert response.context['form'].errors  # есть ошибки

@pytest.mark.django_db
def test_login_view_get(client):
    """GET запрос на логин возвращает форму."""
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    assert 'form' in response.context

@pytest.mark.django_db
def test_login_view_post_success(client):
    """Успешный вход."""
    user = UserFactory(username='testuser', password='testpass123')
   
    url = reverse('login')
    data = {
        'username': 'testuser',
        'password': 'testpass123',
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse('category_list')
    assert '_auth_user_id' in client.session

@pytest.mark.django_db
def test_login_view_post_invalid(client):
    """Неверные учётные данные."""
    user = UserFactory(username='testuser', password='testpass123')
    url = reverse('login')
    data = {
        'username': 'testuser',
        'password': 'wrongpass',
    }
    response = client.post(url, data)
    assert response.status_code == 200  # остаёмся на странице
    assert 'form' in response.context
    assert response.context['form'].errors

@pytest.mark.django_db
def test_logout_view(client):
    """Выход из системы."""
    user = UserFactory()
    client.force_login(user)
    url = reverse('logout')
    response = client.get(url)  # logout через GET 
    assert response.status_code == 302
    assert response.url == reverse('login')
    assert '_auth_user_id' not in client.session

@pytest.mark.django_db
def test_protected_view_redirects_anonymous(client):
    """Неавторизованный пользователь перенаправляется на страницу входа."""
    protected_urls = [
        reverse('category_list'),
        reverse('category_create'),
        reverse('entry_create', args=[1]),  

        # другие защищённые URL
    ]
    for url in protected_urls:
        response = client.get(url)
        assert response.status_code == 302
        assert response.url.startswith(reverse('login'))