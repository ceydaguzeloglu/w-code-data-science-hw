'''1. soru'''
x = 3
x = float(x)
print(type(x))
y = 4.5
y = int(y)
print(type(y))
z = "8"
z = int(z)
print(type(z))
a = "12"
a = float(int(a))
print(type(a))
b = "46.8"
b = int(float(b))
print(type(b))

'''2. soru'''
zeynep = 17
asya = 21
arda = 22
print("zeynep asyadan büyük mü? ", zeynep > asya)
print("asya ardadan küçük mü? ", asya < arda)
print("arda zeynepten büyük mü? ", arda > zeynep)
print("arda zeynepten ve asyadan büyük mü? ", (arda > zeynep) and (arda > asya))
print("asya zeynepten büyük veya ardadan küçük mü? ", (asya > zeynep) or (asya < arda))
print("zeynep asyadan büyük değil ve ardadan küçük mü? ", not(zeynep > asya) and (zeynep < arda))

'''3. soru'''
num1 = int(input("please enter the first integer: "))
num2 = int(input("please enter the second integer: "))

print(num1, " - ", num2, " = ", num1 - num2)
print(num1, " + ", num2, " = ", num1 + num2)
print(num1, " * ", num2, " = ", num1 * num2)

if num2 == 0:
   print("you cannot devide a number with 0")
else:
   print(num1, " / ", num2, " = ", num1 / num2)

'''4. soru'''
isim = str(input("please enter your name: "))
yas = str(input("please enter your age: "))
sehir = str(input("please enter the city: "))
meslek = str(input("please enter your major: "))

print("name : ", isim, "\nage : ", yas, "\ncity : ", sehir, "\nmajor : ", meslek)

'''5. soru'''

string = "Hi-Kod Veri Bilimi Atölyesi"

words = string.split()
print("kelimeler:", words)

print("büyük harf:", string.upper()) 

print("küçük harf:", string.lower())

sayilar = "0123456789"
cift = sayilar[0::2]   # 0'dan başlayıp 2'şer atla → "02468"
tek = sayilar[1::2]    # 1'den başlayıp 2'şer atla → "13579"

print("çift sayılar:", cift)
print("tek sayılar:", tek)