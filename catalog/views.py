from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductForm
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from .models import Category
from .services import get_products_by_category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user:
            return HttpResponseForbidden("Вы не являетесь владельцем этого продукта.")
        return super().dispatch(request, *args, **kwargs)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        is_owner = product.owner == request.user
        is_moderator = request.user.has_perm('catalog.can_unpublish_product')
        if not (is_owner or is_moderator):
            return HttpResponseForbidden("У вас нет прав на удаление этого продукта.")
        return super().dispatch(request, *args, **kwargs)

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

@login_required
@permission_required('catalog.can_unpublish_product', raise_exception=True)
def toggle_publish(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_published = not product.is_published
    product.save()
    return redirect('catalog:product_detail', pk=pk)

# === НОВЫЙ КОНТРОЛЛЕР ДЛЯ КАТЕГОРИЙ ===
def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = get_products_by_category(category_id)
    return render(request, 'catalog/category_products.html', {
        'category': category,
        'products': products,
    })
