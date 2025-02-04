from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from movies.models import Movie
def add(request, id):
    get_object_or_404(Movie, id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('home.index')
