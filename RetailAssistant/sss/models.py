from django.db import models

# 产品
class Product(models.Model):
    brand = models.CharField('品牌', max_length=50)
    category = models.CharField('产品', max_length=50)
    code = models.CharField('型号', max_length=50)
    purchase_cost = models.FloatField('进价成本', default=0.0)
    reference_price = models.FloatField('参考售价', default = 0.0)
    unit = models.CharField('单位', max_length=4, blank=True)
    warehouse = models.CharField('仓库', max_length=50)
    current_storage = models.IntegerField('当前库存', default = 0)
    original_number = models.IntegerField('初期库存', default = 0)
    update_date = models.DateTimeField('更新日期', auto_now = True) # 则每次更新都会更新这个时间
    remarks = models.CharField('备注', max_length=50, blank=True)
    def __str__(self):
        return self.brand + self.category + self.code


# 虚拟类：业务对象
class Counterparty(models.Model):
    name = models.CharField('名称', max_length=50)
    phone = models.CharField('联系方式', max_length=50)
    remarks = models.CharField('备注', max_length=50, blank=True)
    address = models.CharField('地址', max_length=50, blank=True)
    class Meta:
        abstract = True

# 顾客
class Customer(Counterparty):
    def __str__(self):
            return '顾客：' + self.name + self.phone

# 供货商
class Supplier(Counterparty):
    def __str__(self):
            return '供货商：' + self.name + self.phone

# 安装师傅/技工
class Technician(Counterparty):
    def __str__(self):
        return self.name + self.phone



# 虚拟类：业务记录
class History(models.Model):
    occur_date = models.DateTimeField('发生时间')
    record_time = models.DateTimeField('记录时间')
    remarks = models.CharField('备注', max_length=50, blank=True)
    class Meta:
        abstract = True

# 销售记录
class SaleHistory(History):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    number = models.IntegerField('交易数量', default = 1)
    price = models.FloatField('成交价格', default = 0.0)
    def __str__(self):
        return self.occur_date.strftime('%Y-%m-%d') + ' - ' + self.product.category + ' - ' + self.customer.person_name

# 进货记录
class StockHistory(History):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    number = models.IntegerField('交易数量', default = 1)
    price = models.FloatField('成交价格', default = 0.0)
    def __str__(self):
        return self.occur_date.strftime('%Y-%m-%d') + self.product.category

# 上门服务记录
class ServiceHistory(History):
    sale_history = models.ForeignKey(SaleHistory, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    def __str__(self):
        return self.occur_date.strftime('%Y-%m-%d') + self.technician.name + self.sale_history.product