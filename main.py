import pandas

df = pandas.read_csv('example.csv')

information = ''
spendings = df.to_numpy()

for spending in spendings:
    date = spending[0]
    category = spending[1]
    detail = spending[2]
    amount = spending[3]
    spending_information = str(date) + ' * ' + str(detail) + "\n" + "    " + 'Expenses:' +  str(category) + '    ' + str(amount) + ' TL' + "\n"

    information = information + spending_information

with open("ledgerified_csv.data", "w") as file:
    file.write(information)
