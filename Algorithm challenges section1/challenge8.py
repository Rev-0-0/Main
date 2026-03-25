cost = 0.75
amntbars = int(input("Enter the number of bars u want\n "))
total = cost*amntbars
print(f"Total is £{total}")
payed = int(input("How much wil you pay(£)\n£"))
print(f"Change is £{payed-total}")