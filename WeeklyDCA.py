import json,urllib.request,time

data = json.loads(urllib.request.urlopen("https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000&api_key={c634ba3a5dad68a98f2935902b0f74eed3bdbf10bb87f7c44b3a2636ecb36afa}").read())

tuesday = 0
wednesday = 0
thursday = 0
friday = 0
saturday = 0
sunday = 0
monday = 0
list = []
days = []
m = 0

while m <= 2000:
    price = float(data["Data"]["Data"][m]["open"])
    wday = int(time.gmtime(int(data["Data"]["Data"][m]["time"]))[6])
    list.append(price)
    days.append(wday)

    m +=1

x = 0
mo = 0
tu = 0
we = 0
th = 0
fr = 0
sa = 0
su = 0
disposable = []

while x <= 2000:
    price = list[x]
    wday = days[x]

    if wday == 0:
        mo = price
        disposable.append(mo)
        x += 1
    elif wday == 1:
        tu = price
        disposable.append(tu)
        x += 1
    elif wday == 2:
        we = price
        disposable.append(we)
        x += 1
    elif wday == 3:
        th = price
        disposable.append(th)
        x += 1
    elif wday == 4:
        fr = price
        disposable.append(fr)
        x += 1
    elif wday == 5:
        sa = price
        disposable.append(sa)
        x += 1
    elif wday == 6:
        su = price
        disposable.append(su)

    if len(disposable) == 7:
        minimum = min(disposable)

        if minimum == mo:
            monday += 1
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

        x += 1
        disposable = []


print("Monday: " + str(monday))
print("Tuesday: " + str(tuesday))
print("Wednesday: " + str(wednesday))
print("Thursday: " + str(thursday))
print("Friday: " + str(friday))
print("Saturday: " + str(saturday))
print("Sunday: " + str(sunday))
