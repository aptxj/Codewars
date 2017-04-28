"""
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8
    The new "Avengers" movie has just been released!
    There are a lot of people at the cinema box office standing in a huge line.
    Each of them has a single 100, 50 or 25 dollars bill.
    A "Avengers" ticket costs 25 dollars.
    Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
    Can Vasya sell a ticket to each person and give the change
    if he initially has no money and sells the tickets strictly in the order people follow in the line?
    Return YES, if Vasya can sell a ticket to each person and give the change.
    Otherwise return NO.
    Examples:
    ### Python ###
    tickets([25, 25, 50]) # => YES
    tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
"""

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

####################

def tickets(self, people):
    bills_kept = {25: 0, 50: 0, 100: 0}
    for bill in people:
        bill_give = bill - 25
        for bill_ in (50, 25):
            while bill_give >= bill_ and bills_kept[bill_] >= 1:
                bills_kept[bill_] -= 1
                bill_give -= bill_

        if bill_give != 0:
            return "NO"

        bills_kept[bill] += 1

    return "YES"

#####################

def tickets_01(self, people):
    def isSubList(sublist, baselist):
        c = Counter(sublist)
        for change in c:
            if c[change] > baselist.count(change):
                return False
        return True

    changes_kept = []
    for cash in people:
        if cash == 25:
            changes_kept.append(cash)
        if cash == 50:
            if 25 in changes_kept:
                changes_kept.remove(25)
                changes_kept.append(50)
            else:
                return 'NO'
        elif cash == 100:
            changes_togive_set = [[25, 50], [25, 25, 25]]
            checklst = [isSubList(changes_togive, changes_kept)
                        for changes_togive in changes_togive_set]
            if True in checklst:
                for change in changes_togive_set[checklst.index(True)]:
                    changes_kept.remove(change)
            else:
                return "NO"
    return "YES"


