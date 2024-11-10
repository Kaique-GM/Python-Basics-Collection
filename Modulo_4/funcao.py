## lab 1
def is_year_leap(year):
 if year % 4 != 0:
    return False
 elif year % 100 != 0:
    return True
 elif year % 400 != 0:
    return False
 else:
    return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fracassado")

#Lab 2
def is_year_leap(year):
 if year % 4 != 0:
    return False
 elif year % 100 != 0:
    return True
 elif year % 400 != 0:
     return False
 else:
    return True

def days_in_month(year,month):
 if year < 1582 or month < 1 or month > 12:
    return None
 days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 res = days[month - 1]
 if month == 2 and is_year_leap(year):
    res = 29
    return res

test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
 yr = test_years[i]
 mo = test_months[i]
 print(yr,mo,"-> ",end="")
 result = days_in_month(yr, mo)
 if result == test_results[i]:
    print("OK")
else:
    print("Fracassado")


#lab 3
def is_year_leap(year):
 if year % 4 != 0:
    return False
 elif year % 100 != 0:
    return True
 elif year % 400 != 0:
    return False
 else:
    return True

def days_in_month(year, month):
 if year < 1582 or month < 1 or month > 12:
    return None
 days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 res = days[month - 1]
 if month == 2 and is_year_leap(year):
    res = 29
    return res

def day_of_year(year, month, day):
 days = 0
 for m in range(1, month):
    md = days_in_month(year, m)
    if md == None:
        return None
 days += md
 md = days_in_month(year, month)
 if day >= 1 and day <= md:
   return days + day
 else:
   return None

print(day_of_year(2000, 12, 31))

#lab 3

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True
for i in range(1, 20):
 if is_prime(i + 1):
    print(i + 1, end=" ")
print()

#lab 4
def liters_100km_to_miles_gallon(liters):
 gallons = liters / 3.785411784
 miles = 100 * 1000 / 1609.344
 return miles / gallons

def miles_gallon_to_liters_100km(miles):
 km100 = miles * 1609.344 / 1000 / 100
 litres = 3.785411784
 return litres / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
