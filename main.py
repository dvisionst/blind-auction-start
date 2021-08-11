from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)

# creating variables of all the user inputs for the secret auction 
bidder_name = input("What is your name? ")
bid_amount = int(input("How much will you bid? "))
adding_more_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
clear()

# created an empty dictionary and a function in order to add more participants in
# a while loop
auction_dict_list = {}

def secret_auction(name_of_bidder,amount):
    auction_dict_list[name_of_bidder]=amount
secret_auction(bidder_name,bid_amount)

# while loop that adds all of the participants of the secret auction
# it creates a key and value pair that keeps getting appended to auction_dict_list
while adding_more_bidders == "yes":
    bidder_name = input("What is your name? ")
    bid_amount = int(input("How much will you bid? "))
    adding_more_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
    secret_auction(bidder_name,bid_amount)
    clear()

# simple finding the max value algorithm also gets the name (key) of max bidder
# for the final print statement.
max_bid = 0
max_bidder = ''
for name in auction_dict_list:
    if auction_dict_list[name]>max_bid:
        max_bid = auction_dict_list[name]
        max_bidder = name

print(f"The winner is {max_bidder} with a bid of ${max_bid}")