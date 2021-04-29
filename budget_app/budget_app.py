class Category:

    def __init__(x, name):
        x.name = name
        x.ledger = list()
        x.balance = 0

    def deposit(x, amount, description=''):
        x.ledger.append({
            'amount': amount,
            'description': description,
        })
        x.balance += amount

    def withdraw(x, amount, description=''):
        if x.check_funds(amount):
            x.ledger.append({
                'amount': 0-amount,
                'description': description,
            })
            x.balance -= amount
            return True
        else:
            return False

    def get_balance(x):
        return x.balance

    def transfer(x, amount, budget_category):
        if x.check_funds(amount):
            x.ledger.append({
                'amount': 0-amount,
                'description': 'Transfer to ' + budget_category.name,
            })
            x.balance -= amount
            budget_category.balance += amount
            budget_category.ledger.append({
                'amount': amount,
                'description': 'Transfer from ' + x.name,
            })
            return True
        else:
            return False

    def check_funds(x, amount):
        if x.balance >= amount:
            return True
        else:
            return False

    def __str__(x):
        result = x.name.center(30, '*') + '\n'
        for y in x.ledger:
            result += (y['description'].ljust(23))[:23] + format(y['amount'], '.2f').rjust(7) + '\n'
        result += 'Total: ' + format(x.balance, '.2f')
        return result


# Create Spend Chart:
def create_spend_chart(categories):

    # get total withdrawals nad withdrawals by cat
    total_withdrawals = 0
    withdrawals_by_cat = list()

    for x in categories:
        withdrawalByCat = 0
        for y in x.ledger:
            if y['amount'] < 0 and y['description'].split(' ')[0] != 'Transfer':
                total_withdrawals += y['amount'] * -1
                withdrawalByCat += y['amount'] * -1
        withdrawals_by_cat.append(withdrawalByCat)

    # get percent spent by cat
    percentList = list()
    for x in withdrawals_by_cat:
        percentList.append(
            round(((x / total_withdrawals) * 100), 2)
        )

    # add graph
    graphList = list()
    x = 100
    addList = list()
    for x1 in percentList:
        addList.append(' ')
        addList.append(' ')
        addList.append(' ')
    while x >= 0:
        y = '\n' + str(x).rjust(3) + '| '
        index = 0
        for z in percentList:
            if z == 100:
                addList[index] = 'o'
            elif z >= x and z < x + 10:
                addList[index] = 'o'
            index += 3
        addString = ''
        for a in addList:
            addString += a
        y += addString
        graphList.append(y)
        x -= 10

    result = 'Percentage spent by category'
    for x2 in graphList:
        result += x2

    # add bar
    addBar = '\n' + ' ' * 4 + '-' * (len(addList)+1)
    result += addBar

    #add names
    namesList = list()
    for x3 in categories:
        namesList.append(x3.name)

    maxNameLen = len(max(namesList, key=len))

    x4 = maxNameLen
    addNames = ''
    lettersList = list()
    i = 0
    while x4 > 0:
        y = '\n' + ' ' * 5
        for z in namesList:
            if i < len(z):
                y += z[i] + '  '
            else:
                y += ' ' * 3
        i += 1
        lettersList.append(y)
        x4 -= 1

    for x5 in lettersList:
        addNames += x5
    
    result += addNames

    return result
