from art import logo

print(logo)
print("Welcome to the secret auction program")

auction_dict={}

while(True):
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  auction_dict[name]=bid

  choice=input("Are there any other bidders? Type 'yes or 'no' \n").lower()

  if(choice=='yes'):
    continue
  else:
    break

max=0
for key in auction_dict:
  value= auction_dict[key]
  if(value>max):
    max=value
    winner=key

print(f"The winner is {winner} with a bid of {max}.")

# Project by Shivani verma