""" Persian description 
! ابهامات مقاله:
$ exception handling 

مدریت استثنا) استفاده میشه تا کد را پاک‌تر و خواناتر کند)exception handling استفاده میشه در with در پایتون، دستور 
رو راحت میکنه file stream resource منابع) رایج مثل)resources مدریت
نداریم یابه عبارتی خودش فایل رو میبنده .close() استفاده کنیم، نیازی به  with توجه داشته باشیم که اگر از
یعنی استفاده و آزادسازی مناسب منابع، رو تضمین میکنه proper acquisition and release of resources میاد  with statement
میتونه کاری کنه که از بسته شدن صحیح فایل جلوگیری شه که باعث میشه چند تاباگ تو کد ایجادشه file.write() در طول  exception در مثال اول، حالت اول، یک استثنا یا
که معنیش اینکه بسیاری از تغییرات در فایل ها، تا زمانی که فایل به درستی بسته نشه، اعمال نمیشه
استفاده کنیم کد فشرده و خواناتر می شود with statement یا استثناها جلوگیری میکند اما اگر از  exception مثال اول، حالت دوم، از تمامی
استفاده میکنه به طور کامل اجرا خواهد شد resource میشه و زمانی که کدی از release یا منبع به درستی resource هم جلوی باگ ها رو میگیرم و هم with پس با
ها استفاده میشه file streams معمولا برای with
قابل استفاده کند with وجود ندارد که آن را با دستور open() هیچ چیز خاصی در 
“with” statement in user defined objects بریم سراغ 

@ Supporting the “with” statement in user defined objects - اشیاء تعریف شده توسط کاربر
ی باز نگذارید resource تضمین میکند که هیچ  object در with statement ساپورت شدن از 
اضافه کنیم object در متد های __enter__() and __exit__() استفاده کرد، باید از متد های with بشه از user defined objects برای اینکه در

! بررسی مثال دوم:
است MessageWriter میآید سازنده  with اگر متوجه شده باشید، چیزی که پس از
رو اجرا میکنه __enter__() میشه آبجکت ساخته میشه و پایتون متد with statement هcontext  به محض اینکه اجرای کد وارد
ی که میخوایم در آبجکت استفاده کنیم رو مقداردهی اولیه میکنه resource میاد  __enter__() متد
منبع حاصل شده) رو برمیگردونه)acquired resource توصیف گر) از)descriptor  این متد همیشه یک
What are resource descriptors? توصیف گر منابع چیست
درخواستی ارائه شده resources هایی هستن که توسط سیستم عامل به  handles  اینها
است file stream resource توصیف گر descriptor یک  file در قطعه کد زیر
file = open('hello.txt')
توصیف گر) ایجاد میکنه و اون رو برمیگردونه)descriptor یک  __enter__() متد MessageWriter بنابر این در مثال
(البته در این مثال به کد نگاه کن)
استفاده شده __enter__() برای ارجاع دادن توصیفگر فایل برگردانده شده توسط متد xfile  اسم
نوشته شده with استفاده میکنه داخل بلاک کد acquired resource بلاک کدی که از
اجرا میشه __exit__() اجرا شد و تمام شد متد with به محض اینکه کد داخل 
"""

select_ex = "n_" + input("Please Select one of the Examples: ")


def ex1():
    # !First Example:
    print("~~~~~~~~~~~~~~First EX~~~~~~~~~~~~~~")
    # file handling

    # 1) without using with statement
    file = open("./files/ex1-1.txt", "w")
    file.write("hello world !\nwithout using with statement")
    file.close()

    # 2) without using with statement
    file = open("./files/ex1-2.txt", "w")
    try:
        file.write(
            "hello world\nwas used try and finally statements instead of with statement"
        )
    finally:
        file.close()

    # using with statement
    with open("./files/ex1-3.txt", "w") as file:
        file.write("hello world !\nusing with statement")

    print('to see the output of this example, please check files Folder in this directory')
    print('closed the file stream after \'with statement file handling\'?',file.closed)
    
    # فایل بسته میشه with statement پس جالبیش اینجاست که بعد

def ex2():
    # !Second Example:
    print("~~~~~~~~~~~~~~Second EX~~~~~~~~~~~~~~")

    # a simple file writer object
    class MessageWriter(object):
        def __init__(self, file_name):
            self.file_name = file_name

        def __enter__(self):
            # creates a file descriptor and returns it
            self.file = open(self.file_name, 'w')
            return self.file
    
        def __exit__(self, *args):
            self.file.close()
 
    # using with statement with MessageWriter
    
    with MessageWriter('my_file.txt') as xfile:
        xfile.write('hello world')


examples = {
    "n_1": ex1,
    "n_2": ex2,
    # "n_3": ex3,
}

if not (select_ex in examples):
    print("Please Enter a Valid input!!!")
    quit()
else:
    examples[select_ex]()
