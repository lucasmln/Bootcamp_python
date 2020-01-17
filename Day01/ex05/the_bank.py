class Account(object):
    ID_COUNT = 1
    
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []
    
    def add(self, account):
        self.account.append(account)
    
    def transfer(self, origin, dest, amount):
        if (origin.name == None or origin.id == None or origin.value == None or
            origin.__dict__ == None):
            return False
        if (dest.name == None or dest.id == None or dest.value == None or
            dest.__dict__ == None):
            return False
        good_ori, good_dst, cmpt, cmpt2 = 0, 0, -3, -3
        for ori in origin.__dict__.values():
            if str(ori).startswith('b'):
                return False
            if str(ori).startswith("zip") or str(ori).startswith("addr"):
                good_ori = 1
            cmpt += 1
        for dst in dest.__dict__.values():
            if str(dst).startswith('b'):
                return False
            if str(dst).startswith("zip") or str(dst).startswith("addr"):
                good_dst = 1
            cmpt2 += 1
        if good_ori == 0 or good_dst == 0 or cmpt % 2 == 0 or cmpt2 % 2 == 0:
            return False
        if (origin.value - amount) < 0:
            return False
        origin.value -= amount
        dest.value += amount
        return True
        """
            @origin: int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return         True if success, False if an error occured
"""
    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
"""

myBank = Bank()
myAccount = Account('Lucas', value = 0, zap = "zipzip")
charlesAccount = Account('Charles', value = 0, zop = "addraddr", oub = "asf", yak = " sdgfs")

myBank.add(myAccount)
myBank.add(charlesAccount)
print(myBank.transfer(myAccount, charlesAccount, 1000))
myAccount.value = 1000
print(myBank.transfer(myAccount, charlesAccount, 1000))

print(charlesAccount.value)
print(myAccount.value)
