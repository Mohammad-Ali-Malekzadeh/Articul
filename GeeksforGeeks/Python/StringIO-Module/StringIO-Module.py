""" Persian description 

است in-memory file-like object یک StringIo
.read() اگر به این تابع ورودی استرینگی بدیم، داخل شی ما قرار خواهد گرفت اما اگر ورودی ندیم، و فایل را با کمک متد
بخوانیم یک استرینگ خالی خواهیم داشت 
که بصورت دیفالت فایل آبجکتی ما از ایندکس صفر شروع به خوندن میشه  initial cursor on the file starts at zeroمنظور از 
دارد یا نهsupport random access مشخص میشه که میشه از یه ایندکس دیگه شروع به خواندن کرد یا به عبارتی قابلیت  .seekable() که البته جلوتر با کمک 


@ methods of StringIO:
1. StringIO.getvalue(): محتوای داخل فایل رو به صورت استرینگ بر میگردونه

2. functions of StringIO which returns Boolean:
---StringIO.isatty():
------این است که در مهندسی کامپیوتر فایل یا دستگاهی که در هر زمان می توان یک کاراکتر از آن خواند یا نوشتstream منظور از
------.مثلاً مانیتور و صفحه کلید می توانند چنین باشند 
------open("demofile.txt", "r").isatty() برمیگردونه False در این مثال
------کار این تابع اینکه بررسی میکنه آیا فایل به یک ترمینال متصل شده است یا نه
---StringIO.readable()
---StringIO.writable() 
---StringIO.seekable():
------برای فهمیدن اینکه آیا میشه دسترسی رندوم به فایل داشت یا نه، از این تابع استفادهیکنیم
------برای اینکه مشخص کنیم از کجای فایل متن رو باید بخونیم میتونیم ازش استفاده میکنیم seek() یه تابع دیگه ای داریم به اسم
------این تابع هم برای اینکه بهمیم آیا میشه اینکار رو کرد تو فایل مون یا نه؟
---StringIO.closed:
------برمیگردونه False و اگر فایل باز باشه True اگر فایل بسته باشه 

3. StringIO.seek(): روی فایل انجام بدیم write و read  میکنه. به عبارتی اگر ما کار set  رو cursor position این تابع میاد برامون 
کردن فایل لازم داریم از این تابع استفاده کنیم write و read فایل قرار میگیره، پس برای دوباره  index روی آخرین cursor position بعد اینکار
len(file) حالا یا میتونیم بهش آرگومان صفر بدیم که از اول فایل شروع میشه یا هر ایندکس کمتری نسبت به

4. StringIO.truncate(): به درد میخوره به طوری که بعد ایندکس که بصورت آرگومان بهش میدیم  stream فایل size کردن resize  برای
به بعد رو کات میکنه

5. StringIO.tell(): فایل رو برامون مشخص میکنه current stream or cursor position میاد
کنیم write و read به عبارتی میگه در حال حاضر تو کدوم ایندکس فایل هستیم و طبیعتا از اون به بعد میتونیم 

6. StringIO.close(): فایلمون رو میبنده ،بعد اینکه این تابع رو برای فایلی اجرا کنیم دیگه نمیتونیم روش کاری اعمال کنیم
بهمون میده ValueError اگر هم بکنیم 

"""

select_ex = "n_" + input("Please Select one of the Examples: ")
from io import StringIO

def ex1 ():
    # !First Example:
    print("~~~~~~~~~~~~~~First EX~~~~~~~~~~~~~~")

    # The arbitrary string.
    string = "This is initial string."

    # Using the StringIO method to set
    # as file object. Now we have an
    # object file that we will able to
    # treat just like a file.
    file = StringIO(string)

    # this will read the file
    print(file.read())

    # We can also write this file.
    file.write(" Welcome to geeksforgeeks.")

    # This will make the cursor at
    # index 0.
    file.seek(0)
    # برای اینکه مشخص کنیم از کجای فایل متن رو باید بخونیم میتونیم ازش استفاده میکنیم seek() تابع

    # This will print the file after
    # writing in the initial string.
    print("The string after writing is:", file.read())

    print(StringIO().read())

def ex2 ():
    # !Second Example:
    print("~~~~~~~~~~~~~~Second EX~~~~~~~~~~~~~~")

    # The arbitrary string.
    string = "Hello and welcome to GeeksForGeeks."

    # Using the StringIO method to
    # set as file object.
    file = StringIO(string)

    # Retrieve the entire content of the file.
    print(file.getvalue())

def ex3 ():
    # !third Example:
    print('~~~~~~~~~~~~~~Third EX~~~~~~~~~~~~~~')

    # The arbitrary string.
    string ='Hello and welcome to GeeksForGeeks.'
    
    # Using the StringIO method to 
    # set as file object.
    file = StringIO(string) 
    
    # This will returns whether the file
    # is interactive or not.
    print("Is the file stream interactive?", file.isatty()) 
    # print(StringIO(string))
    
    # This will returns whether the file is
    # readable or not.
    print("Is the file stream readable?", file.readable())
    
    # This will returns whether the file supports 
    # writing or not.
    print("Is the file stream writable?", file.writable())
    
    # This will returns whether the file is
    # seekable or not.
    print("Is the file stream seekable?", file.seekable())
    
    # This will returns whether the file is 
    # closed or not.
    print("Is the file closed?", file.closed)

def ex4 ():
    # !Fourth Example:
    print('~~~~~~~~~~~~~~Fourth EX~~~~~~~~~~~~~~')
       
    # The arbitrary string.
    string ='Hello and welcome to GeeksForGeeks.'
    
    # Using the StringIO method 
    # to set as file object.
    file = StringIO(string) 
    
    # Reading the file:
    print(file.read())
    
    # Now if we again want to read
    # the file it shows empty file
    # because the cursor is set to 
    # the last index.
    
    
    # This does not print anything
    # because the function returns an
    # empty string.
    print(file.read()) 
    
    # Hence to set the cursor position
    # to read or write the file again
    # we use seek().We can pass any index
    # here from(0 to len(file))
    file.seek(0) 
    
    # Now we can able to read the file again()
    print(file.read())
  
def ex5 ():
    # !Fifth Example:
    print('~~~~~~~~~~~~~~Fifth EX~~~~~~~~~~~~~~')

    # The arbitrary string.
    string ='Hello and welcome to GeeksForGeeks.'
    
    # Using the StringIO method
    # to set as file object.
    file = StringIO(string) 
    
    # Reading the initial file:
    print(file.read())
    
    # To set the cursor at 0.
    file.seek(0) 
    
    
    # This will drop the file after 
    # index 18.
    file.truncate(18)
    
    # File after truncate.
    print(file.read())

def ex6 ():
    # !Sixth Example:
    print('~~~~~~~~~~~~~~Sixth EX~~~~~~~~~~~~~~')

    # The arbitrary string.
    string ='Hello and welcome to GeeksForGeeks.'
    
    # Using the StringIO method to 
    # set as file object.
    file = StringIO(string)
    
    # Here the cursor is at index 0.
    print(file.tell())
    
    # Cursor is set to index 20.
    file.seek(20)
    
    # Print the index of cursor
    print(file.tell())

def ex7 ():
    # !Seventh Example:
    print('~~~~~~~~~~~~~~Seventh EX~~~~~~~~~~~~~~')

    # The arbitrary string.
    string ='Hello and welcome to GeeksForGeeks.'
    
    # Using the StringIO method to
    # set as file object.
    file = StringIO(string)
    
    # Reading the file.
    print(file.read()) 
    
    # Closing the file.
    file.close() 
    
    # If we now perform any operation on the file 
    # it will raise an ValueError.
    
    # This is to know whether the
    # file is closed or not.
    print("Is the file closed?", file.closed) 

examples = {
    "n_1": ex1,
    "n_2": ex2,
    "n_3": ex3,
    "n_5": ex5,
    "n_6": ex6,
    "n_7": ex7
}

if not (select_ex in examples):
    print("Please Enter a Valid input!!!")
    quit()
else:
    examples[select_ex]()