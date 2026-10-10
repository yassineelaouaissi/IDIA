import math

# درس: العمليات الحسابية في بايثون
# مثال بسيط: 10 + 3 = 13
x = 10
y = 3

# جمع: نضيف رقمين معًا
print("Sum:", x + y)
# النتيجة: 13

# طرح: نطرح رقمًا من رقم آخر
print("Difference:", x - y)
# النتيجة: 7

# ضرب: نضرب رقمين معًا
print("Product:", x * y)
# النتيجة: 30

# قسمة: نقسم رقمًا على آخر
print("Division:", x / y)
# النتيجة: 3.3333333333333335

# قسمة صحيحة: نأخذ الجزء الصحيح فقط من القسمة
print("Floor division:", x // y)
# النتيجة: 3

# باقي القسمة: نأخذ الباقي من القسمة
print("Modulus:", x % y)
# النتيجة: 1

# الأس: نرفع الرقم إلى أس معين
print("Exponentiation:", x ** y)
# النتيجة: 1000

# الإشارة الموجبة: لا تغيّر القيمة
print("Unary plus:", +x)
# النتيجة: 10

# الإشارة السالبة: تغير إشارة الرقم
print("Unary minus:", -x)
# النتيجة: -10

# المقارنة: يساوي
print("Equal:", x == y)
# النتيجة: False

# المقارنة: لا يساوي
print("Not equal:", x != y)
# النتيجة: True

# المقارنة: أكبر من
print("Greater than:", x > y)
# النتيجة: True

# المقارنة: أصغر من
print("Less than:", x < y)
# النتيجة: False

# المقارنة: أكبر من أو يساوي
print("Greater than or equal:", x >= y)
# النتيجة: True

# المقارنة: أصغر من أو يساوي
print("Less than or equal:", x <= y)
# النتيجة: False

# التعيين: z = 5
z = 5
z += 2
# الآن z = 7
print("z after +=:", z)
# النتيجة: 7

z -= 1
# الآن z = 6
print("z after -=:", z)
# النتيجة: 6

z *= 3
# الآن z = 18
print("z after *=:", z)
# النتيجة: 18

z /= 2
# الآن z = 9.0
print("z after /=:", z)
# النتيجة: 9.0

z //= 2
# الآن z = 4.0
print("z after //=:", z)
# النتيجة: 4.0

z %= 3
# الآن z = 1.0
print("z after %=:", z)
# النتيجة: 1.0

z **= 2
# الآن z = 1.0
print("z after **=:", z)
# النتيجة: 1.0

# الدوال الرياضية المدمجة
# abs: القيمة المطلقة
print("Absolute value:", abs(-25))
# النتيجة: 25

# round: التقريب
print("Rounded value:", round(3.14159, 2))
# النتيجة: 3.14

# pow: الأس
print("Power:", pow(2, 5))
# النتيجة: 32

# max: أكبر قيمة
print("Maximum:", max(12, 45, 7))
# النتيجة: 45

# min: أصغر قيمة
print("Minimum:", min(12, 45, 7))
# النتيجة: 7

# sum: جمع عناصر القائمة
print("Sum of list:", sum([1, 2, 3, 4, 5]))
# النتيجة: 15

# الدوال من مكتبة math
# sqrt: الجذر التربيعي
print("Square root:", math.sqrt(81))
# النتيجة: 9.0

# floor: تقريب لأسفل
print("Floor:", math.floor(7.9))
# النتيجة: 7

# ceil: تقريب لأعلى
print("Ceil:", math.ceil(7.1))
# النتيجة: 8

# pi: قيمة باي
print("Pi:", math.pi)
# النتيجة: 3.141592653589793

# e: عدد أويلر
print("Euler's number:", math.e)
# النتيجة: 2.718281828459045

# factorial: مضروب العدد
print("Factorial:", math.factorial(5))
# النتيجة: 120

# fabs: القيمة المطلقة كرقم عشري
print("Absolute float value:", math.fabs(-8.5))
# النتيجة: 8.5

# gcd: القاسم المشترك الأكبر
print("GCD:", math.gcd(48, 18))
# النتيجة: 6

# log: لوغاريتم
print("Logarithm:", math.log(100, 10))
# النتيجة: 2.0

# sin: جيب الزاوية بالراديان
print("Sine:", math.sin(math.radians(90)))
# النتيجة: 1.0

# cos: جيب التمام للزاوية بالراديان
print("Cosine:", math.cos(math.radians(0)))
# النتيجة: 1.0

# مثال دالة مخصصة
# هذه الدالة تجمع رقمين

def add(a, b):
    return a + b

print("Function result:", add(10, 5))
# النتيجة: 15



# مثال أخير: تنسيق النص
format_string = f"The result of adding {1} and {5} is {0}"

