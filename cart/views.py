from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Cart, CartItem 
from django.views.generic import   UpdateView ,DeleteView , CreateView
from django.shortcuts import render, redirect
from store.models import Category ,Book
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User


@login_required
def cart_detail_view(request, pk):
    cart = Cart.objects.get(user_id=pk)
    items = CartItem.objects.filter(cart=cart)
    categories = Category.objects.all()

    if request.method == 'POST':
        return redirect('cart', pk=pk)  

    return render(request, 'core/cart.html', {'items': items, 'categories': categories , 'cart': cart})


class ItemUpdateView(UpdateView):
    model = CartItem
    fields = ['quantity']
    template_name = 'core/cart.html'

    def get_success_url(self):
        cart = self.object.cart 
        return reverse_lazy('cart', kwargs={'pk': cart.user.pk}) 
    def form_valid(self, form):
        item = form.save(commit=False) 
        if item.quantity == 0:
            item.delete() 
            return redirect('cart', pk=item.cart.user.pk)  

        item.save()
        return super().form_valid(form)



class ItemDeleteView(DeleteView):
    model = CartItem
    template_name = 'core/cart.html'

    def get_success_url(self):
        cart = self.object.cart 
        return reverse_lazy('cart', kwargs={'pk': cart.user.pk}) 
 
    
class ItemCreateView(LoginRequiredMixin,CreateView):
    model = CartItem
    template_name = 'core/cart.html'
    fields = [] 
    login_url = 'login'

    def form_valid(self, form):
        product = get_object_or_404(Book, id=self.kwargs['pk']) 
        
        cart, created = Cart.objects.get_or_create(user=self.request.user) 

        existing_item = CartItem.objects.filter(cart=cart, product=product).first()

        if existing_item:
            existing_item.quantity += 1
            existing_item.save()
            self.object = existing_item
            return redirect(self.get_success_url())  

        form.instance.cart = cart 
        form.instance.product = product  
        form.instance.quantity = 1  
        return super().form_valid(form)

    def get_success_url(self):
        cart = self.object.cart 
        return reverse_lazy('cart', kwargs={'pk': cart.user.pk}) 
    




class UserView(LoginRequiredMixin,UpdateView):
    model = User

    fields = [
        'first_name',
        'last_name',
        'phone',
        'email',
        'address',
        'countery',
        'city',
        'postcode',
    ]
    
    template_name = 'cart/checkout.html'
    def get_object(self, queryset=None):
        return self.request.user
  
    def get_success_url(self):
        return reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart = Cart.objects.filter(user=self.object).first()
        context['cart'] = cart

        context['cart_items'] = CartItem.objects.filter(cart=cart)

        return context
