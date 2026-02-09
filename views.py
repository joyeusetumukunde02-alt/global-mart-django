from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import RegisterForm, LoginForm, orderForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AvailableProduct, order
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import employee, department, Comment,Product
from .forms import employeeForm


# REGISTER
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


# LOGIN
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("product")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# PROFILE

def profile_view(request):
    return render(request, 'profile.html')


# PRODUCT LIST
def avilableProduct_view(request):
    products = AvailableProduct.objects.all()
    return render(request, 'AvailablePoduct.html', {'products': products})


# ORDER CREATE
@login_required(login_url='/login/') 
def order_view(request):
    if request.method == "POST":
        form = orderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = orderForm()
    return render(request, 'order.html', {'form': form})


# ORDER LIST FOR ADMIN/EMPLOYEES
def order_list(request):
    orders = order.objects.all()

    if 'responded_orders' not in request.session:
        request.session['responded_orders'] = {}

    if request.method == "POST":
        order_id = request.POST.get('order_id')
        if order_id:
            request.session['responded_orders'][order_id] = True
            request.session.modified = True

    return render(request, 'order_list.html', {
        'orders': orders,
        'responded_orders': request.session['responded_orders']
    })


# ========== EMPLOYEE VIEWS (PROTECTED) ==========

class EmployeeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = employee
    template_name = "employee/list.html"
    context_object_name = "employees"
    permission_required = "yourapp.view_employee"
    raise_exception = True


class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = employee
    form_class = employeeForm
    template_name = "employee/form.html"
    success_url = reverse_lazy('employee_list')
    permission_required = "yourapp.add_employee"
    raise_exception = True


class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = employee
    form_class = employeeForm
    template_name = "employee/form.html"
    success_url = reverse_lazy('employee_list')
    permission_required = "yourapp.change_employee"
    raise_exception = True


class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = employee
    template_name = "employee/delete.html"
    success_url = reverse_lazy('employee_list')
    permission_required = "yourapp.delete_employee"
    raise_exception = True


# ========= OTHER VIEWS =========

def overView(request):
    return render(request, 'overView.html', {})


def dep(request):
    dep = department.objects.all()
    return render(request, 'employee/depaterment.html', {'dep': dep})



def add_comment(request, product_id):
    product = get_object_or_404(AvailableProduct, id=product_id)
    if request.method == 'POST':
        Comment.objects.create(
            user=request.user,
            product=product,
            text=request.POST['comment']
        )
    return redirect(request.META.get('HTTP_REFERER'))



def like_product(request, product_id):
    product = get_object_or_404(AvailableProduct, id=product_id)
    product.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))


def contact(request):
    return render(request, 'contact.html')
def phone_products(request):
    products = Product.objects.filter(category="phone")
    return render(request, "phones.html", {
        "products": products,
        "title": "Phones"
    })

def computer_products(request):
    products = Product.objects.filter(category="computer")
    return render(request, "computer.html", {
        "products": products,
        "title": "Computers"
    })

def accessories_products(request):
    products = Product.objects.filter(category="accessory")
    return render(request, "Accessories.html", {
        "products": products,
        "title": "Accessories"
    })
