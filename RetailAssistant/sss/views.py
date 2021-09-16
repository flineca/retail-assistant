from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.decorators.csrf import csrf_exempt #包装csrf请求，避免django认为其实跨站攻击脚本 

from sss.models import Product, Customer, Supplier, Technician, SaleHistory, StockHistory, ServiceHistory

from django.utils import timezone

class IndexView(ListView):
    template_name = 'sss/index.html'
    model = Product
    # context_object_name = 'storage_list'

    def get_queryset(self):
        """Return the recently updated products and their storage"""
        return Product.objects.order_by('-update_date')[:5]

class DetailView(DetailView):
    template_name = 'sss/detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

@csrf_exempt
def query_storage(request):
    if request.method == "GET":
        try:
            product_brand = request.GET['product_brand']
            product_category = request.GET['product_category']
            product_warehousee = request.GET['product_warehousee']
        except (KeyError):
            return HttpResponse('NECESSARY VALUE MISS')

        product_set = Product.objects.filter(brand=product_brand, category=product_category, warehouse = product_warehousee)
        
        return HttpResponse(content=str(product_set))


@csrf_exempt
def query_history(request):
    if request.method == "GET":
        try:
            product_id = request.GET['product_id']
            product = Product.objects.get(id=product_id)
        except (DoesNotExist):
            return HttpResponse('NO SUCH A PRODUCT')
            
        try:
            stockhistory_set = StockHistory.objects.filter(product=product)
            salehistory_set = SaleHistory.objects.filter(product=product)
        except:
            return HttpResponse('ERROR')

        return HttpResponse(stockhistory_set)
   
   
@csrf_exempt
def query_service(request):
    if request.method == "GET":
        try:
            salehistory_id = request.GET['salehistory_id']
            salehistory = SaleHistory.objects.get(id=salehistory_id)
            servicehistory = ServiceHistory.objects.get(sale_history=salehistory)
        except (DoesNotExist):
            return HttpResponse('NO SUCH A HISTORY')
        return HttpResponse(servicehistory)


@csrf_exempt
def add_warehouse(request):
    if request.method == "POST":
        try:
            warehouse = Warehouse(name=request.POST['name'], address=request.POST['address'], remarks=request.POST['remarks'])
            warehouse.save()
        except Exception:
            return HttpResponse(status=404, content='ERROR')
        return HttpResponse('SUCCESSFUL')

@csrf_exempt
def add_product(request):
    if request.method == "POST":
        try:
            warehouse = Warehouse(name=request.POST['name'], address=request.POST['address'], remarks=request.POST['remarks'])
            warehouse.save()
        except Exception:
            return HttpResponse('ERROR')
        else:
            return HttpResponse('SUCCESSFUL')

@csrf_exempt
def add_customer(request):
    if request.method == "POST":
        try:
            warehouse = Warehouse(name=request.POST['name'], address=request.POST['address'], remarks=request.POST['remarks'])
            warehouse.save()
        except Exception:
            return HttpResponse('ERROR')
        else:
            return HttpResponse('SUCCESSFUL')


@csrf_exempt
def add_supplier(request):
    if request.method == "POST":
        try:
            warehouse = Warehouse(name=request.POST['name'], address=request.POST['address'], remarks=request.POST['remarks'])
            warehouse.save()
        except Exception:
            return HttpResponse('ERROR')
        else:
            return HttpResponse('SUCCESSFUL')

@csrf_exempt
def add_technician(request):
    if request.method == "POST":
        try:
            warehouse = Warehouse(name=request.POST['name'], address=request.POST['address'], remarks=request.POST['remarks'])
            warehouse.save()
        except (KeyError, Product.DoesNotExist):
            return HttpResponse('ERROR')
        else:
            return HttpResponse('SUCCESSFUL')

@csrf_exempt
def add_stock(request):
    pass


@csrf_exempt
def add_service(request):
    pass


@csrf_exempt
def add_sale(request):
    if request.method == "POST":
        storage = get_object_or_404(Storage, pk=request.POST['storage_id'])
        try:
            sale_history = SaleHistory.create()
        except:
            return render(request, 'sss/detail.html', {
                'question': question,
                'error_message': "您没有选择选项",
            })
        else:
            sale_history.save()
            # Always return an HttpResponseRedirect after successfully dealing with POST data. 
            # This prevents data from being posted twice if a user hits the Back button.
            return HttpResponseRedirect(reverse('sss:', args=(question.id,)))
            # 在这个例子中，我们在 HttpResponseRedirect 的构造函数中使用 reverse() 函数。
            # 这个函数避免了我们在视图函数中硬编码 URL。
            # 它需要我们给出我们想要跳转的视图的名字和该视图所对应的 URL 模式中需要给该视图提供的参数。 
            # 在本例中，使用在 教程第 3 部分 中设定的 URLconf， reverse() 调用将返回一个这样的字符串：
            # '/polls/3/results/'
            # 其中 3 是 question.id 的值。重定向的 URL 将调用 'results' 视图来显示最终的页面。

