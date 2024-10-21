def is_leap(year):
    if 1900<=year<=10**5:
        if year%4==0 and year%100==0:
            if year%400==0:
                return True
            else:
                return False
        elif year%4==0:
            return True
        else: return False
    else:
        raise ValueError("kimu")

year = int(input())
print(is_leap(year))