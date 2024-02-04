from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    #  query = request.GET['query']
    # search_item = Q(product_name__icontains=query)
    # product_search = Products.objects.filter(search_item)


    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     products = Products.objects.filter(product_name__icontains=q)
    # else:
    products = Products.objects.all()

    
   

    context = {
        'products':products,
        
    }
    return render(request, 'store_app/index.html',context)

from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Cart, CartItem

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Check if the product is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')  # Redirect to the cart view

def cart_view(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()

    return render(request, 'cart/cart.html', {'cart_items': cart_items})



def about(request):
    return render(request, 'store_app/about.html')

def blog(request):
    return render(request, 'store_app/blog.html')

def cart(request):
    return render(request, 'store_app/cart.html')

def category_4col(request):
    return render(request, 'store_app/category-4col.html')

def category_5col(request):
    return render(request, 'store_app/category-5col.html')

def category_6col(request):
    return render(request, 'store_app/category-6col.html')

def category_7col(request):
    return render(request, 'store_app/category-7col.html')

def category_8col(request):
    return render(request, 'store_app/category-8col.html')

def category_banner_boxed_image(request):
    return render(request, 'store_app/category-banner-boxed-image.html')


def category_banner_boxed_slider(request):
    return render(request, 'store_app/category-banner-boxed-slider.html')


def category_horizontal_filter1(request):
    return render(request, 'store_app/category-horizontal-filter1.html')

def category_horizontal_filter2(request):
    return render(request, 'store_app/category-horizontal-filter2.html')

def category_infinite_scroll(request):
    return render(request, 'store_app/category-infinite-scroll.html')

def category_list(request):
    return render(request, 'store_app/category-list.html')

def category_off_canvas(request):
    return render(request, 'store_app/category-off-canvas.html')

def category_sidebar_right(request):
    return render(request, 'store_app/category-sidebar-right.html')

def category(request):
    return render(request, 'store_app/category.html')

def checkout(request):
    return render(request, 'store_app/cheakout.html')

def contact(request):
    form = Contact_f(request.POST)
    
    if request.method == 'POST':
        form = Contact_f(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('/')
        else:
            form = Contact_f()
            return render(request, 'store_app/contact.html')


    add = ContactInfo.objects.all()
    qstn = AskedQuestions.objects.all()
    context = {
        'add':add,
        'form':form,
        'qstn':qstn,
    }
    return render(request, 'store_app/contact.html',context)

def demo1_about(request):
    return render(request, 'store_app/demo1-about.html')

def demo1_contact(request):
    return render(request, 'store_app/demo1-contact.html')

def demo1_product(request):
    return render(request, 'store_app/demo1-product.html')

def demo1_shop(request):
    return render(request, 'store_app/demo1-shop.html')

def element_accordions(request):
    return render(request, 'store_app/element-accordions.html')

def element_alerts(request):
    return render(request, 'store_app/element-alerts.html')

def element_animations(request):
    return render(request, 'store_app/element-animations.html')

def element_banners(request):
    return render(request, 'store_app/element-banners.html')
def element_buttons(request):
    return render(request, 'store_app/element-buttons.html')

def element_call_to_action(request):
    return render(request, 'store_app/element-call-to-action.html')

def element_countdown(request):
    return render(request, 'store_app/element-countdown.html')

def element_counters(request):
    return render(request, 'store_app/element-counters.html')

def element_headings(request):
    return render(request, 'store_app/element-headings.html')

def element_icons(request):
    return render(request, 'store_app/element-icons.html')

def cart(request):
    return render(request, 'store_app/cart.html')

def element_info_box(request):
    return render(request, 'store_app/element-info-box.html')

def element_posts(request):
    return render(request, 'store_app/element-posts.html')

def element_product_categories(request):
    return render(request, 'store_app/element-product-categories.html')

def element_products(request):
    return render(request, 'store_app/element-products.html')

def element_tabs(request):
    return render(request, 'store_app/element-tabs.html')

def element_testimonial(request):
    return render(request, 'store_app/element-testimonial.html')

def product_addcart_sticky(request):
    return render(request, 'store_app/product-addcart-sticky.html')

def product_center_vertical(request):
    return render(request, 'store_app/product-center-vertical.html')

def product_custom_tab(request):
    return render(request, 'store_app/product-custom-tab.html')

def product_extended_layout(request):
    return render(request, 'store_app/product-extended-layout.html')

def product_full_width(request):
    return render(request, 'store_app/product-full-width.html')

def product_grid_layout(request):
    return render(request, 'store_app/product-grid-layout.html')

def product_sidebar_left(request):
    return render(request, 'store_app/product-sidebar-left.html')

def product_sidebar_right(request):
    return render(request, 'store_app/product-sidebar-right.html')

def product_sticky_both(request):
    return render(request, 'store_app/product-sticky-both.html')

def product_sticky_info(request):
    return render(request, 'store_app/product-sticky-info.html')

def product_transparent_image(request):
    return render(request, 'store_app/product-transparent-image.html')

def product_variable(request):
    return render(request, 'store_app/product-variable.html')

def product(request):
    return render(request, 'store_app/product.html')

def single(request):
    return render(request, 'store_app/single.html')

def wishlist(request):
    return render(request, 'store_app/wishlist.html')

def search(request):
    q = request.GET['q']
    products = Products.objects.filter(product_name__icontains=q)
    
    context = {
        'products':products
    }
    return render(request,'store_app/search.html',context)

# def base(request):
#     address = FooterAddress.objects.all()
#     context = {
#         'address':address
#     }
#     return render(request, 'store_app/base.html',context)

