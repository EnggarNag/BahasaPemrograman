class OVO:
    def __init__(self, saldo):
        self.__saldo = saldo

    def TopUp(self, amount):
        self.__saldo += amount
        return self.__saldo

    def Transfer(self, amount):
        if self.__saldo >= amount:
            self.__saldo -= amount
            return self.__saldo
        else:
            return "Saldo Tidak Cukup"

    def get_saldo(self):
        return self.__saldo

member = OVO(200000)
print(member.TopUp(50000)) # tambah 50000
print(member.Transfer(250000)) # ambil 250000
print(member.get_saldo()) # sisa 0
