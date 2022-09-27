
class Deduction:

    def __init__(self, desc, date, chargeamt, idnum):
        self.__desc = desc
        self.__date = date
        self.__chargeamt = chargeamt
        self.__idnum = idnum


    def set_desc(self, desc):
        self.__desc = desc

    def set_chargeamt(self, chargeamt):
        self.__chargeamt = abs(chargeamt)


    def set_idnum(self, idnum):
        self.__idnum = idnum


    def get_desc(self):
        return self.__desc
    
    def get_date(self):
        return self.__date

    def get_chargeamt(self):
        return self.__chargeamt

    def get_idnum(self): 
        return self.__idnum 


