class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        diffTrans = {}
        # result = set()

        for trans in transactions:
            name, time, amount, city = trans.split(",")
            diffTrans["name"] = name
            diffTrans["time"] = time
            diffTrans["amount"] = amount
            diffTrans["city"] = city
        
        print(diffTrans)



transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
# transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
# transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]

print(Solution().invalidTransactions(transactions))