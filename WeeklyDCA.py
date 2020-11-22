#import
import json,urllib.request
data = urllib.request.urlopen("https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000&api_key={09ee84755c171057c01d4ac7f4910271fb2dc48d39efc3a421960629a9afb0ff}").read()
output = json.loads(data)


tuesday = 0
wednesday = 0
thursday = 0
friday = 0
saturday = 0
sunday = 0
monday = 0
list = []

m = 0
while m <= 2000:
    price = float(output["Data"]["Data"][m]["open"])
    list.append(price)
    m +=1

day = 0
x = 0
tu = 0
we = 0
th = 0
fr = 0
sa = 0
su = 0
po = 0

disposable = []
while x <= 2000:
    price = list[x]
    if day == 0:
        tu = price
        disposable.append(tu)
        x += 1
        day += 1
    elif day == 1:
        we = price
        disposable.append(we)
        x += 1
        day += 1
    elif day == 2:
        th = price
        disposable.append(th)
        x += 1
        day += 1
    elif day == 3:
        fr = price
        disposable.append(fr)
        x += 1
        day += 1
    elif day == 4:
        sa = price
        disposable.append(sa)
        x += 1
        day += 1
    elif day == 5:
        su = price
        disposable.append(su)
        x += 1
        day += 1
    elif day == 6:
        po = price
        disposable.append(po)


        minimum = min(disposable)

        if minimum == tu:
            tuesday += 1
        if minimum == we:
            wednesday += 1
        if minimum == th:
            thursday += 1
        if minimum == fr:
            friday += 1
        if minimum == sa:
            saturday += 1
        if minimum == su:
            sunday += 1
        if minimum == po:
            monday += 1
        x += 1
        day = 0
        disposable = []
        tu = 0
        we = 0
        th = 0
        fr = 0
        sa = 0
        su = 0
        po = 0



print("Monday: " + str(monday))
print("Tuesday: " + str(tuesday))
print("Wednesday: " + str(wednesday))
print("Thursday: " + str(thursday))
print("Friday: " + str(friday))
print("Saturday: " + str(saturday))
print("Sunday: " + str(sunday))
