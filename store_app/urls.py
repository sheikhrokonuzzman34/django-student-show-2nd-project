from django.urls import path
from .views import *

urlpatterns = [
# path('',index,name='index_page'),
path('',index,name='index_page'),
path('about',about,name='about'),
path('blog',blog,name='blog'),
path('cart',cart,name='cart'),
path('category-4col',category_4col,name='category-4col'),
path('category-5col',category_5col,name='category-5col'),
path('category-6col',category_6col,name='category-6col'),
path('category-7col',category_7col,name='category-7col'),
path('category-8col',category_8col,name='category-8col'),
path('category-banner-boxed-image',category_banner_boxed_image,name='category-banner-boxed-image'),
path('category-banner-boxed-slider',category_banner_boxed_slider,name='category-banner-boxed-slider'),
path('category-horizontal-filter1',category_horizontal_filter1,name='category-horizontal-filter1'),
path('category-horizontal-filter2',category_horizontal_filter2,name='category-horizontal-filter2'),
path('category-infinite-scroll',category_infinite_scroll,name='category-infinite-scroll'),
path('category-list',category_list,name='category-list'),
path('category-off-canvas',category_off_canvas,name='category-off-canvas'),
path('category-sidebar-right',category_sidebar_right,name='category-sidebar-right'),
path('category',category,name='category'),
path('checkout',checkout,name='checkout'),
path('contact',contact,name='contact'),
path('demo1-about',demo1_about,name='demo1-about'),
path('demo1-contact',demo1_contact,name='demo1-contact'),
path('demo1-product',demo1_product,name='demo1-product'),
path('demo1-shop',demo1_shop,name='demo1-shop'),
path('element-accordions',element_accordions,name='element-accordions'),
path('element-alerts',element_alerts,name='element-alerts'),
path('element-animations',element_animations,name='element-animations'),
path('element-buttons',element_buttons, name='element-buttons'),
path('element-banners',element_banners,name='element-banners'),
path('element-call-to-action',element_call_to_action,name='element-call-to-action'),
path('element-countdown',element_countdown,name='element-countdown'),
path('element-counters',element_counters,name='element-counters'),
path('element-headings',element_headings,name='element-headings'),
path('element-icons',element_icons,name='element-icons'),
path('cart',cart,name='cart'),
path('element-info-box',element_info_box,name='element-info-box'),
path('element-posts',element_posts,name='element-posts'),
path('element-product-categories',element_product_categories,name='element-product-categories'),
path('element-products',element_products,name='element-products'),
path('element-tabs',element_tabs,name='element-tabs'),
path('element-testimonial',element_testimonial,name='element-testimonial'),
path('product-addcart-sticky',product_addcart_sticky,name='product-addcart-sticky'),
path('product-center-vertical',product_center_vertical,name='product-center-vertical'),
path('product-custom-tab',product_custom_tab,name='product-custom-tab'),
path('product-extended-layout',product_extended_layout,name='product-extended-layout'),
path('product-full-width',product_full_width,name='product-full-width'),
path('product-grid-layout',product_grid_layout,name='product-grid-layout'),
path('product-sidebar-left',product_sidebar_left,name='product-sidebar-left'),
path('product-sidebar-right',product_sidebar_right,name='product-sidebar-right'),
path('product-sticky-both',product_sticky_both,name='product-sticky-both'),
path('product-sticky-info',product_sticky_info,name='product-sticky-info'),
path('product-transparent-image',product_transparent_image,name='product-transparent-image'),
path('product-variable',product_variable,name='product-variable'),
path('product',product,name='product'),
path('single',single,name='single'),
path('wishlist',wishlist,name='wishlist'),
path('search',search,name='search'),

]