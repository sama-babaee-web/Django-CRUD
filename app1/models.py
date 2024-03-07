from django.db import models



# MorakhsiDetailView ======= مرخصی پرسنل

class MorakhsiDetailView(models.Model):
    id =  models.AutoField(primary_key=True,verbose_name='شماره درخواست')
    fullname = models.CharField(max_length=50 , verbose_name='نام و نام خانوادگی')
    fromdate = models.CharField(max_length=10 , verbose_name = 'از تاریخ')
    todate = models.CharField(max_length=10 , verbose_name='تا تاریخ')
    Comment = models.TextField(verbose_name='توضیحات ')
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return self.fullname
    
    
    
    
    
# PersonalInfromation   =============  اطلاعات پرسنلی
    
class PersonalInfromation(models.Model):
    
    GENDER = (
        ('M','مرد'),
        ('F','زن')
    )
    
    
    CONDITION=(
    ('Single','مجرد'),
    ('married','متاهل'),
    )
    id = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=50 , verbose_name='نام و نام خانوادگی')
    jensiyat = models.CharField(max_length=8,verbose_name="جنسیت",null=True,choices= GENDER)
    semat = models.CharField(max_length=50,verbose_name='سمت')
    start_date = models.CharField(max_length=10 ,verbose_name="تاریخ شروع به کار")
    vaziyat = models.CharField(max_length=8,verbose_name="وضعیت تاهل",null=True,choices= CONDITION)
    farzand = models.IntegerField(verbose_name="تعداد اولاد")
    created_at = models.DateTimeField(auto_now_add=True)

    
    
    def __str__(self):
        return self.fullname
    





# PersonelPresenceAbsence  ===================  حضور و غیاب پرسنل

class PersonelPresenceAbsence(models.Model):
    date = models.DateTimeField(verbose_name="تاریخ",blank=True)
    rozhafte = models.CharField(max_length=10,verbose_name="روز هفته")
    personnel_id = models.IntegerField( verbose_name='کد پرسنلی')
    fullname = models.CharField(max_length=50 , verbose_name='نام و نام خانوادگی')
    vaziyat = models.CharField(max_length=10,verbose_name="وضعیت")
    vorod = models.TimeField(verbose_name="ساعت ورود")
    khoroj = models.TimeField(verbose_name="ساعت خروج")
    morakhasi_saati = models.TimeField(verbose_name="میزان مرخصی ساعتی")
    takhir = models.TimeField(verbose_name=" تاخیر")
    ezafe_kari = models.TimeField(verbose_name="اضافه کاری")
    
    def __str__(self):
        return self.fullname
    
    
    
    
class Number(models.Model):
    username = models.CharField(max_length=10, blank=False, null=True)
    number = models.PositiveIntegerField(blank=False, null=True)

    def __str__(self):
        return self.username