months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def get_number(_month):
    return months.index(_month) + 1

def validate_date(_m,_d):
    return (int(_m) > 0 and int(_m) < 13) and (int(_d) > 0 and int(_d) < 32)


while True:
    date = input("Date: ").strip()
    try:
        month, day, year = date.split("/")
        if validate_date(month, day):break

    except Exception:
        try:
            _m, _d, year=date.split(" ")

            if "," in date:
                day=_d.replace(",","")

                month=get_number(_m)

                if validate_date(month,day):break
        except Exception:
            pass

print(f"{year}-{int(month):02}-{int(day):02}")

