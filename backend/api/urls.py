from django.conf.urls import url
from api.views import movie_views
from api.views import auth_views
from api.views import rating_views
from api.views import jinsooTest
from api.views import jjy_view
    # , recommend_views
from api.views import rating_views
from api.views import km_algo_views
from api.views import recommend_views

urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('auth/signin/$', auth_views.signin, name='sign_in'),
    url('auth/signup/$', auth_views.signup, name='sign_up'),
    url('movies/$', movie_views.movies, name='movie_list'),
    url('ratings/$', rating_views.ratings, name='rating_list'),
    url('recommends/$', recommend_views.recommends, name='recommend_list'),
    url('test/$', jinsooTest.test, name='jinsooTest'),
    # url('test_jjy/$', jjy_view.test, name='jjyTest'),
    url('km_algo/$', km_algo_views.km_algo, name='km_algo'),
    url('delete/user/$', auth_views.delete, name='delete_user'),
    url('update/user/$', auth_views.update, name='update_user'),
    url('delete/movie/$', movie_views.delete, name='delete_movie'),
    url('update/movie/$', movie_views.update, name='update_movie'),
]
