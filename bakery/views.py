from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Contact

import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# ------------------------
# STATIC PAGES
# ------------------------
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

# ------------------------
# CONTACT FORM
# ------------------------
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if not re.match(r'^[A-Za-z\s]{3,}$', name):
            messages.error(request, "Name must contain only letters (min 3 chars).")
            return redirect("contact")
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email address.")
            return redirect("contact")
        if not re.match(r'^[0-9]{10}$', phone):
            messages.error(request, "Phone must be exactly 10 digits.")
            return redirect("contact")
        if len(subject) < 5:
            messages.error(request, "Subject must be at least 5 characters long.")
            return redirect("contact")
        if len(message) < 10:
            messages.error(request, "Message must be at least 10 characters long.")
            return redirect("contact")

        Contact.objects.create(
            name=name, email=email, phone=phone, subject=subject, message=message
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")
    return render(request, "contact.html")

# --------
# views.py
from django.shortcuts import render
from django.db.models import Count
from .models import Category


   # views.py
def category_list(request):
    categories_with_counts = []

    for cat in CATEGORIES:
        slug = cat['slug']
        products = category_products.get(slug, [])
        cat_copy = cat.copy()
        cat_copy['product_count'] = len(products)  # <-- compute count here
        categories_with_counts.append(cat_copy)

    return render(request, "product_list.html", {"categories": categories_with_counts})


# ------------------------
CATEGORIES = [
    {"name": "Cakes", "slug": "cakes", "image": "/static/images/p1.png"},
    {"name": "Pastries", "slug": "pastries", "image": "/static/images/p2.png"},
    {"name": "Sweets", "slug": "sweets", "image": "/static/images/p3.png"},
    {"name": "Gift Box", "slug": "gift-box", "image": "/static/images/p4.png"},
    {"name": "Savouries", "slug": "savouries", "image": "/static/images/p5.png"},
    {"name": "Breads", "slug": "breads", "image": "/static/images/p6.png"},
    {"name": "Cookies & Biscuits", "slug": "cookies-biscuits", "image": "/static/images/p7.png"},
    {"name": "Cream Roll", "slug": "cream-roll", "image": "/static/images/p8.png"},
    {"name": "Muffins & Fruit Cake", "slug": "muffins-fruit-cake", "image": "/static/images/p9.png"},
    {"name": "Chips", "slug": "chips", "image": "/static/images/p10.png"},
    {"name": "Chocolates", "slug": "chocolates", "image": "/static/images/p11.png"},
    {"name": "Rusk", "slug": "rusk", "image": "/static/images/p12.png"},
]


# Map slug -> image for convenience
category_images = {c['slug']: c['image'] for c in CATEGORIES}

# ------------------------
# HARDCODED PRODUCTS
# ------------------------
category_products = {
    "cakes": [
        {"name": "Vanilla Cake", "price": 400 , "image": "/static/images/p13.png" , "nutrition": "Energy 250 kcal, Carbohydrates 35g, Fat 10g, Protein 4g per 100g",
            "ingredients": "Refined flour, sugar, cocoa powder, fresh cream, butter, chocolate, baking powder",
            "allergies": "Contains gluten, milk, and soy. May contain traces of nuts."},
        {"name": "Strawberry Cake", "price": 480, "image": "/static/images/p14.png",  "nutrition": "Energy 250 kcal, Carbohydrates 35g, Fat 10g, Protein 4g per 100g",
            "ingredients": "Refined flour, sugar, cocoa powder, fresh cream, butter, chocolate, baking powder",
            "allergies": "Contains gluten, milk, and soy. May contain traces of nuts."},
        {"name": "Pineapple Cake", "price": 420, "image": "/static/images/p16.png",  "nutrition": "Energy 250 kcal, Carbohydrates 35g, Fat 10g, Protein 4g per 100g",
            "ingredients": "Refined flour, sugar, cocoa powder, fresh cream, butter, chocolate, baking powder",
            "allergies": "Contains gluten, milk, and soy. May contain traces of nuts."},
        {"name": "Coffee Cake", "price": 430, "image": "/static/images/p18.png",  "nutrition": "Energy 250 kcal, Carbohydrates 35g, Fat 10g, Protein 4g per 100g",
            "ingredients": "Refined flour, sugar, cocoa powder, fresh cream, butter, chocolate, baking powder",
            "allergies": "Contains gluten, milk, and soy. May contain traces of nuts."},
        {"name": "Butterscotch Cake", "price": 450, "image": "/static/images/p15.png",  "nutrition": "Energy 250 kcal, Carbohydrates 35g, Fat 10g, Protein 4g per 100g",
            "ingredients": "Refined flour, sugar, cocoa powder, fresh cream, butter, chocolate, baking powder",
            "allergies": "Contains gluten, milk, and soy. May contain traces of nuts."},
        {"name": "Lemon Cake", "price": 440, "image": "/static/images/p17.png",  "nutrition": "Energy 250 kcal, Carbohydrates 35g, Fat 10g, Protein 4g per 100g",
            "ingredients": "Refined flour, sugar, cocoa powder, fresh cream, butter, chocolate, baking powder",
            "allergies": "Contains gluten, milk, and soy. May contain traces of nuts."},
    ],
    "pastries": [
        {"name": "Red Velvet Pastry", "price": 150, "image": "/static/images/p68.png",  "nutrition": "Energy 250 kcal, Carbohydrates 35g, Fat 10g, Protein 4g per 100g",
            "ingredients": "Refined flour, sugar, cocoa powder, fresh cream, butter, chocolate, baking powder",
            "allergies": "Contains gluten, milk, and soy. May contain traces of nuts."},
        {"name": "Vanilla Pastry", "price": 130, "image": "/static/images/p69.png",  "nutrition": "Energy 250 kcal, Carbohydrates 35g, Fat 10g, Protein 4g per 100g",
            "ingredients": "Refined flour, sugar, cocoa powder, fresh cream, butter, chocolate, baking powder",
            "allergies": "Contains gluten, milk, and soy. May contain traces of nuts."},
        {"name": "Chocolate Pastry", "price": 140, "image": "/static/images/p67.png",  "nutrition": "Energy 250 kcal, Carbohydrates 35g, Fat 10g, Protein 4g per 100g",
            "ingredients": "Refined flour, sugar, cocoa powder, fresh cream, butter, chocolate, baking powder",
            "allergies": "Contains gluten, milk, and soy. May contain traces of nuts."},
        {"name": "Strawberry Pastry", "price": 135, "image": "/static/images/p68.png",  "nutrition": "Energy 250 kcal, Carbohydrates 35g, Fat 10g, Protein 4g per 100g",
            "ingredients": "Refined flour, sugar, cocoa powder, fresh cream, butter, chocolate, baking powder",
            "allergies": "Contains gluten, milk, and soy. May contain traces of nuts."},
        {"name": "Coffee Pastry", "price": 125, "image": "/static/images/p69.png",  "nutrition": "Energy 250 kcal, Carbohydrates 35g, Fat 10g, Protein 4g per 100g",
            "ingredients": "Refined flour, sugar, cocoa powder, fresh cream, butter, chocolate, baking powder",
            "allergies": "Contains gluten, milk, and soy. May contain traces of nuts."},
        {"name": "Pineapple Pastry", "price": 145, "image": "/static/images/p67.png",  "nutrition": "Energy 250 kcal, Carbohydrates 35g, Fat 10g, Protein 4g per 100g",
            "ingredients": "Refined flour, sugar, cocoa powder, fresh cream, butter, chocolate, baking powder",
            "allergies": "Contains gluten, milk, and soy. May contain traces of nuts."},
        {"name": "Almond Pastry", "price": 150, "image": "/static/images/p68.png",  "nutrition": "Energy 250 kcal, Carbohydrates 35g, Fat 10g, Protein 4g per 100g",
            "ingredients": "Refined flour, sugar, cocoa powder, fresh cream, butter, chocolate, baking powder",
            "allergies": "Contains gluten, milk, and soy. May contain traces of nuts."},
       
    ],
    "sweets": [
        {"name": "Rasgulla", "price": 250, "image": "/static/images/p19.png"},
        {"name": "Gulab Jamun", "price": 220, "image": "/static/images/p20.png"},
        {"name": "Kaju Katli", "price": 300, "image": "/static/images/p21.png"},
        {"name": "Motichoor Ladoo", "price": 280, "image": "/static/images/p22.png"},
        {"name": "Soan Papdi", "price": 200, "image": "/static/images/p27.png"},
        {"name": "Peda", "price": 240, "image": "/static/images/p28.png"},
        {"name": "Milk Barfi", "price": 260, "image": "/static/images/p29.png"},
        {"name": "Coconut Ladoo", "price": 230, "image": "/static/images/p30.png"},
        {"name": "Chocolate Ladoo", "price": 270, "image": "/static/images/p31.png"},
    ],
    "gift-box": [
        {"name": "Assorted Sweets Box", "price": 600, "image": "/static/images/p64.png"},
        {"name": "Dry Fruit Box", "price": 800, "image": "/static/images/p65.png"},
        {"name": "Premium Chocolate Box", "price": 900, "image": "/static/images/p66.png"},
        {"name": "Celebration Box", "price": 850, "image": "/static/images/p64.png"},
        {"name": "Festive Box", "price": 750, "image": "/static/images/p65.png"},
        {"name": "Luxury Box", "price": 950, "image": "/static/images/p66.png"},
        {"name": "Bakery Box", "price": 700, "image": "/static/images/p64.png"},
        {"name": "Mini Treat Box", "price": 650, "image": "/static/images/p65.png"},
    ],
    "savouries": [
        {"name": "Mixture", "price": 120, "image": "/static/images/p61.png"},
        {"name": "Murukku", "price": 90, "image": "/static/images/p62.png"},
        {"name": "Chivda", "price": 110, "image": "/static/images/p63.png"},
        {"name": "Sev", "price": 100, "image": "/static/images/p61.png"},
        {"name": "Masala Peanuts", "price": 95, "image": "/static/images/p62.png"},
        {"name": "Cheese Balls", "price": 130, "image": "/static/images/p63.png"},
        {"name": "Fried Dal", "price": 105, "image": "/static/images/p62.png"},

    ],
    "breads": [
        {"name": "Fresh Bread Loaf", "price": 60, "image": "/static/images/p56.png"},
        {"name": "Whole Wheat Bread", "price": 70, "image": "/static/images/p57.png"},
        {"name": "Multigrain Bread", "price": 80, "image": "/static/images/p58.png"},
        {"name": "Garlic Bread", "price": 85, "image": "/static/images/p59.png"},
        {"name": "Butter Bread", "price": 75, "image": "/static/images/p60.png"},
        {"name": "French Bread", "price": 95, "image": "/static/images/p58.png"},

    ],
    "cookie": [
        {"name": "Butter Cookies", "price": 150, "image": "/static/images/p23.png"},
        {"name": "Oatmeal Cookies", "price": 160, "image": "/static/images/p25.png"},
        {"name": "Almond Cookies", "price": 170, "image": "/static/images/p26.png"},
        {"name": "Cashew Cookies", "price": 175, "image": "/static/images/p27.png"},
        {"name": "Ginger Cookies", "price": 165, "image": "/static/images/p24.png"},
        {"name": "Peanut Cookies", "price": 180, "image": "/static/images/p25.png"},
        {"name": "Vanilla Cookies", "price": 160, "image": "/static/images/p26.png"},
    ],
    "cream": [
        {"name": "Vanilla Cream Roll", "price": 90, "image": "/static/images/p51.png"},
        {"name": "Chocolate Cream Roll", "price": 100, "image": "/static/images/p52.png"},
        {"name": "Strawberry Cream Roll", "price": 110, "image": "/static/images/p53.png"},
        {"name": "Coffee Cream Roll", "price": 95, "image": "/static/images/p54.png"},
        {"name": "Black Forest Roll", "price": 115, "image": "/static/images/p51.png"},
        {"name": "Butterscotch Roll", "price": 100, "image": "/static/images/p52.png"},
        {"name": "Mango Cream Roll", "price": 110, "image": "/static/images/p53.png"},
    ],
    "muffins": [
        {"name": "Blueberry Muffin", "price": 60, "image": "/static/images/p47.png"},
        {"name": "Fruit Cake Slice", "price": 80, "image": "/static/images/p48.png"},
        {"name": "Chocolate Muffin", "price": 70, "image": "/static/images/p49.png"},
        {"name": "Banana Muffin", "price": 65, "image": "/static/images/p47.png"},
        {"name": "Strawberry Muffin", "price": 75, "image": "/static/images/p48.png"},
        {"name": "Coffee Muffin", "price": 70, "image": "/static/images/p49.png"},
        {"name": "Pineapple Muffin", "price": 80, "image": "/static/images/p47.png"},
        {"name": "Mixed Fruit Cake", "price": 85, "image": "/static/images/p48.png"},
        {"name": "Walnut Fruit Cake", "price": 90},
    ],
    "chips": [
        {"name": "Potato Chips", "price": 50, "image": "/static/images/p44.png"},
        {"name": "Banana Chips", "price": 60, "image": "/static/images/p45.png"},
        {"name": "Masala Chips", "price": 55, "image": "/static/images/p46.png"},
        {"name": "Corn Chips", "price": 65, "image": "/static/images/p44.png"},
        {"name": "Cheese Chips", "price": 70, "image": "/static/images/p45.png"},
        {"name": "Spicy Potato Chips", "price": 60, "image": "/static/images/p46.png"},
        {"name": "Plain Banana Chips", "price": 55, "image": "/static/images/p44.png"},
        {"name": "Sweet Potato Chips", "price": 65, "image": "/static/images/p45.png"},
    ],
    "chocolates": [
        {"name": "Milk Chocolate", "price": 120, "image": "/static/images/p40.png"},
        {"name": "Dark Chocolate", "price": 150, "image": "/static/images/p41.png"},
        {"name": "White Chocolate", "price": 140, "image": "/static/images/p42.png"},
        {"name": "Almond Chocolate", "price": 160, "image": "/static/images/p43.png"},
        {"name": "Hazelnut Chocolate", "price": 170, "image": "/static/images/p40.png"},
        {"name": "Caramel Chocolate", "price": 150, "image": "/static/images/p41.png"},
        {"name": "Fruit & Nut Chocolate", "price": 165, "image": "/static/images/p42.png"},
        {"name": "Coffee Chocolate", "price": 155, "image": "/static/images/p43.png"},
    ],
    "rusk": [
        {"name": "Crispy Rusk", "price": 90, "image": "/static/images/p36.png"},
        {"name": "Elaichi Rusk", "price": 100, "image": "/static/images/p37.png"},
        {"name": "Butter Rusk", "price": 95, "image": "/static/images/p38.png"},
        {"name": "Chocolate Rusk", "price": 105, "image": "/static/images/p39.png"},
        {"name": "Almond Rusk", "price": 110, "image": "/static/images/p36.png"},
        {"name": "Pista Rusk", "price": 115, "image": "/static/images/p37.png"},
        {"name": "Coconut Rusk", "price": 100, "image": "/static/images/p38.png"},
        {"name": "Honey Rusk", "price": 105, "image": "/static/images/p39.png"},
  
    ],
}

# ------------------------
# HELPER FUNCTION
# ------------------------
def get_product_by_slug(slug):
    slug = slug.lower().replace(" ", "-")
    for plist in category_products.values():
        for p in plist:
            product_slug = p['name'].lower().replace(" ", "-")
            if product_slug == slug:
                if 'id' not in p:
                    p['id'] = product_slug  # use slug as ID
                if 'image' not in p:
                    p['image'] = "/static/images/default.png"
                return p
    return None

def cakes(request):
    products = category_products.get("cakes", [])
    for i, p in enumerate(products):
        p.setdefault("id", i + 1)
        p.setdefault("image", "/static/images/default.png")
        p.setdefault("in_wishlist", False)
        p.setdefault("slug", p["name"].lower().replace(" ", "-"))
    return render(request, "cake.html", {"cakes": products})
def chips(request):
    products = category_products.get("chips", [])
    for i, p in enumerate(products):
        p.setdefault("id", i + 1)
        p.setdefault("image", "/static/images/default.png")
        p.setdefault("in_wishlist", False)
        p.setdefault("slug", p["name"].lower().replace(" ", "-"))
    return render(request, "chips.html", {"chips": products})
def breads(request):
    products = category_products.get("breads", [])
    for i, p in enumerate(products):
        p.setdefault("id", i + 1)
        p.setdefault("image", "/static/images/default.png")
        p.setdefault("in_wishlist", False)
        p.setdefault("slug", p["name"].lower().replace(" ", "-"))
    return render(request, "bread.html", {"breads": products})
def sweets(request):
    products = category_products.get("sweets", [])
    for i, p in enumerate(products):
        p.setdefault("id", i + 1)
        p.setdefault("image", "/static/images/default.png")
        p.setdefault("in_wishlist", False)
        p.setdefault("slug", p["name"].lower().replace(" ", "-"))
    return render(request, "sweets.html", {"sweets": products})
def savouries(request):
    products = category_products.get("savouries", [])
    for i, p in enumerate(products):
        p.setdefault("id", i + 1)
        p.setdefault("image", "/static/images/default.png")
        p.setdefault("in_wishlist", False)
        p.setdefault("slug", p["name"].lower().replace(" ", "-"))
    return render(request, "savouries.html", {"savouries": products})
def rusk(request):
    products = category_products.get("rusk", [])
    for i, p in enumerate(products):
        p.setdefault("id", i + 1)
        p.setdefault("image", "/static/images/default.png")
        p.setdefault("in_wishlist", False)
        p.setdefault("slug", p["name"].lower().replace(" ", "-"))
    return render(request, "rusk.html", {"rusk": products})
def pastries(request):
    products = category_products.get("pastries", [])
    for i, p in enumerate(products):
        p.setdefault("id", i + 1)
        p.setdefault("image", "/static/images/default.png")
        p.setdefault("in_wishlist", False)
        p.setdefault("slug", p["name"].lower().replace(" ", "-"))
    return render(request, "pastries.html", {"pastries": products})
def muffins(request):
    products = category_products.get("muffins", [])
    for i, p in enumerate(products):
        p.setdefault("id", i + 1)
        p.setdefault("image", "/static/images/default.png")
        p.setdefault("in_wishlist", False)
        p.setdefault("slug", p["name"].lower().replace(" ", "-"))
    return render(request, "muffins.html", {"muffins": products})
def gift(request):
    products = category_products.get("gift-box", [])
    for i, p in enumerate(products):
        p.setdefault("id", i + 1)
        p.setdefault("image", "/static/images/default.png")
        p.setdefault("in_wishlist", False)
        p.setdefault("slug", p["name"].lower().replace(" ", "-"))
    return render(request, "gift.html", {"gift-box": products})
def cream(request):
    products = category_products.get("cream", [])
    for i, p in enumerate(products):
        p.setdefault("id", i + 1)
        p.setdefault("image", "/static/images/default.png")
        p.setdefault("in_wishlist", False)
        p.setdefault("slug", p["name"].lower().replace(" ", "-"))
    return render(request, "cream.html", {"cream": products})
def cookie(request):
    products = category_products.get("cookie", [])
    for i, p in enumerate(products):
        p.setdefault("id", i + 1)
        p.setdefault("image", "/static/images/default.png")
        p.setdefault("in_wishlist", False)
        p.setdefault("slug", p["name"].lower().replace(" ", "-"))
    return render(request, "cookie.html", {"cookie": products})
def chocolates(request):
    products = category_products.get("chocolates", [])
    for i, p in enumerate(products):
        p.setdefault("id", i + 1)
        p.setdefault("image", "/static/images/default.png")
        p.setdefault("in_wishlist", False)
        p.setdefault("slug", p["name"].lower().replace(" ", "-"))
    return render(request, "chocolates.html", {"chocolates": products})



# ------------------------
# PRODUCT LIST
# ------------------------
def product_list(request):
    """Show all categories with product counts"""
    categories_with_counts = []
    for cat in CATEGORIES:
        slug = cat['slug']
        products = category_products.get(slug, [])
        cat_copy = cat.copy()
        cat_copy['product_count'] = len(products)
        categories_with_counts.append(cat_copy)
    return render(request, "product_list.html", {"categories": categories_with_counts})

# ------------------------
# CATEGORY VIEW
# ------------------------
def category_view(request, category_name):
    category = next((c for c in CATEGORIES if c["slug"] == category_name), None)
    if not category:
        raise Http404("Category not found")

    products = category_products.get(category_name, [])
    wishlist = request.session.get("wishlist", [])

    for i, p in enumerate(products):
        p.setdefault("id", i + 1)
        p.setdefault("image", category["image"])
        p["slug"] = p["name"].lower().replace(" ", "-")
        p["in_wishlist"] = p["slug"] in wishlist

    # Context
    context = {"category": category, "products": products}
    context[category_name] = products   # so template can loop like {% for item in cakes %}

    # Template mapping
    template_map = {
        "cakes": "cake.html",
        "chips": "chips.html",
        "sweets": "sweets.html",
        "savouries": "savouries.html",
        "muffins": "muffins.html",
        "cream": "cream.html",
        "cookie": "cookie.html",
        "breads": "bread.html",
        "chocolates": "chocolates.html",
        "rusk": "rusk.html",
        "pastries": "pastries.html",
        "gift-box": "gift.html",
        
        

    }

    template_name = template_map.get(category_name, "product_list.html")
    return render(request, template_name, context)


# ------------------------
# PRODUCT DETAIL
# ------------------------
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Product

# ------------------------
# PRODUCT DETAIL
# ------------------------
# def product_detail(request, product_slug):
#     # Fetch by slug for product detail page
#     product = get_object_or_404(Product, slug=product_slug)
#     return render(request, "product_detail.html", {"product": product})

# ------------------------
# DELIVERY & PAYMENT
# ------------------------
from django.db.models import F
from .models import Product
import random

import random
from django.shortcuts import render, get_object_or_404
from .models import Product, Wishlist

def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    
    # Fetch 3 random products excluding the current one
    all_products = Product.objects.exclude(id=product.id)
    recommended_products = random.sample(list(all_products), min(3, all_products.count()))
    
    # Mark which recommended products are in the wishlist
    if request.user.is_authenticated:
        user_wishlist_product_ids = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
        for p in recommended_products:
            p.in_wishlist = p.id in user_wishlist_product_ids
    else:
        for p in recommended_products:
            p.in_wishlist = False

    context = {
        "product": product,
        "recommended_products": recommended_products,
    }
    return render(request, "product_detail.html", context)


def delivery_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        # messages.success(request, "Order placed successfully!")
        return redirect("payment", product_id=product_id)
    return render(request, "delivery_detail.html", {"product": product})

@login_required
def payment_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        messages.success(request, "ORDER SUCCESSFULLY PLACED!")
        return redirect('payment', product_id=product_id)
    return render(request, "payment.html", {"product": product})

# ------------------------
# USER REGISTRATION
# ------------------------
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect("home")
    return render(request, "register.html")

# ------------------------
# WISHLIST
# ------------------------
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Product, Wishlist

@login_required
def wishlist_view(request):
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
    return render(request, "wishlist.html", {"wishlist_items": wishlist_items})

@login_required
def add_to_wishlist(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    messages.success(request, f"{product.name} added to your wishlist ❤️")
    return redirect("wishlist")

@login_required
def remove_from_wishlist(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    messages.success(request, f"{product.name} removed from wishlist 🗑️")
    return redirect("wishlist")

# ----------------------------
# AJAX toggle for wishlist
# ----------------------------
@login_required
def toggle_wishlist(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if not created:
        wishlist_item.delete()
        status = "removed"
    else:
        status = "added"
    return JsonResponse({"status": status})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.shortcuts import render, redirect
from django.contrib import messages

def cart_view(request):
    cart = request.session.get('cart', {})

    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        cart[product_id] = cart.get(product_id, 0) + quantity
        request.session['cart'] = cart
        messages.success(request, "Product added to cart!")
        return redirect('cart')  # redirect to cart page after adding

    # For GET request, render the cart page
    # Fetch product details from DB if needed
    from .models import Product
    cart_items = []
    total = 0
    for pid, qty in cart.items():
        product = Product.objects.get(id=pid)
        subtotal = product.price * qty
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': qty,
            'subtotal': subtotal
        })

    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'cart.html', context)


def add_to_cart(request, product_id):
    """Add a product to the session cart."""
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})  # Get existing cart or empty dict

    if str(product_id) in cart:
        cart[str(product_id)] += 1  # Increment quantity if already in cart
    else:
        cart[str(product_id)] = 1   # Add new product with quantity 1

    request.session['cart'] = cart  # Save cart back to session
    return redirect('cart')  # Redirect to cart page

def remove_from_cart(request, product_id):
    """Remove a product from the session cart."""
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart')
