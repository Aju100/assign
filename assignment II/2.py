def check_year(year):
    if(year%4)==0:
        if(year%100)==0:
            if(year%4000)==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Enter year: "))
if(check_year(year)):
    print("It's a Leap Year")
else:
    print("It's not a leap year")