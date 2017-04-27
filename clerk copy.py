def tickets(people):
  till = {100.0:0, 50.0:0, 25.0:0}

  for paid in people:
    till[paid] += 1
    change = paid-25.0

    for bill in (50,25):
      while (bill <= change and till[bill] > 0):
        till[bill] -= 1
        change -= bill

    if change != 0:
      return 'NO'

  return 'YES'

##############

def tickets(people):
    change = 'YES'
    twentyfive, fifty, onehundred = 0, 0, 0

    for cash in people:
        if change == 'NO':
            break

        if cash == 25:
            twentyfive += 1
        elif cash == 50 and twentyfive > 0:
            twentyfive -= 1
            fifty += 1
        elif cash == 100:
            if fifty > 0 and twentyfive > 0:
                fifty -= 1
                twentyfive -= 1
                onehundred += 1
            elif twentyfive > 2:
                twentyfive -= 3
                onehundred += 1
            else:
                change = 'NO'
        else:
            change = 'NO'

    return change

#######################

def tickets(a):
    n25 = n50 = n100 = 0
    for e in a:
        if   e==25            : n25+=1
        elif e==50            : n25-=1; n50+=1
        elif e==100 and n50>0 : n25-=1; n50-=1
        elif e==100 and n50==0: n25-=3
        if n25<0 or n50<0:
            return 'NO'
    return 'YES'


######################

def tickets(people):
    cashRegister = {25: 0, 50: 0, 100: 0};
    ticketPrice = 25;
    for paid in people:
        cashRegister[paid] += 1;
        while paid > ticketPrice:
            changeGiven = False;
            """ Check if we have a bill in the register that we use as change """
            for bill in sorted(cashRegister.keys(), reverse=True):
                """ Hand out hhange if possible and still needed """
                if (paid - ticketPrice >= bill) and (cashRegister[bill] > 0):
                    paid = paid - bill;
                    cashRegister[bill] -= 1;
                    changeGiven = True;
            """ Return "NO" if we were unable to give the change required """
            if (paid > ticketPrice) and (changeGiven == False):
                    return "NO";
    return "YES";


###################

def tickets(people, cost=25, bills=[100, 50, 25]):
    count = dict.fromkeys(bills, 0)
    for change in people:
        count[change] += 1
        change -= cost
        for bill in bills:
            if change >= bill:
                c = min(change // bill, count[bill])
                count[bill] -= c
                change -= c * bill
        if change: return "NO"
    return "YES"


