import time
import base64


#start Personlised Configs edit the values to customise your bot!
#intro and questions to ask in one dic to make it more customisible and les code searching for changes 
intro = "Hello I am the Smart Conversational Acquisition Machine or S.C.A.M for short."
questions = {
	"name":"May I have you full name?", 
	"purchase":"Would you like to make a purchase?", 
	"email":"What email would you like us to sell to other companies?",#Ask for their email address. Store the values input to a variable.
	"phone":"What phone number would you like to ring off the hook from spam calls?",#Ask for their phone number.  Store the values input to a variable.
	"quanity":"How many S.C.A.M licenses can we charge you for today?",
	"VIP":"Wonderful! Can I intrest you in paying a Premium for Our Gold Support Plan?\nWith the Gold Support Plan it lowers the avrage reponce time from 1-2 weeks to 1-2 days.",#Ask if they would also like to purchase an optional Gold Support plan that gets them priority #support. 
	"restart": "Would you like to Restart your S.C.A.M A.I?",
	"ccn": "What is the Number of the credit card we can charge our outragous prices to?",
	"cvc": "CVC number? \n Thats the 3 numbers on the back of the card",
	"zip": "Please enter the Zipcode of the billing address for the card."
}

#user info in one dic to be sent out to a back end system or api 
#Ask for a credit card number.  Store the values input to a variable.
#Ask for a credit card expiration date. Store the values input to a variable.
#Ask for a CVC number on the back of the credit card.  Store the values input to a variable.
#Ask for a zip code. Store the values input to a variable.
userinfo_template = {
	"name":"Valued Customer",
	"email":"",
	"ccn":"",
	"last4":"",
	"ccd":"",
	"exp":"",
	"cvc":"",
	"zip":"",
	"gold":"",
	"lic":"",
	"key":""

}
#used to reset user for another run of the bot
userinfo = userinfo_template.copy() 
#Provide a few sentence overview of your Chatbot program. Be creative - make some stuff up. #Output it to the screen with a nice format of your choice. Make this as serious or as silly a #scenario as you want it to be. 
def overview(name):
	overview = f"""
{name},
 
 Introducing the S.C.A.M. AI™
 Smart Conversational Acquisition Machine
 At S.C.A.M. AI™, we believe that appearances are everything
 and substance is completely optional.
 Our cutting-edge chatbot solution uses advanced buzzword technology
 to simulate intelligent conversations,
 convincing customers to buy into our vision
 (and into long-term licensing agreements they will definitely regret later).
 With features like Predictive Persuasion™, Synthetic Sincerity™,
 and our patented Algorithmic Empathy™,
 S.C.A.M. AI™ is guaranteed (but legally not binding)
 to revolutionize customer engagement for your business.
 Join us today and license S.C.A.M. AI™
 where we Sell Confidence and Marketing, not just software.
 Disclaimer: S.C.A.M. AI™ is for demonstration purposes only.
 Actual customer satisfaction may vary wildly.
"""
	return overview
#easily change prices in one spot
#The Gold Support plan costs $500/year for license purchases 1 - 50.
#The Gold Support plan costs $350/year for license purchases 51 - 99.
#The Gold Support plan costs $250/year for license purchases 100+.
upsell={
	"quanity1":"1 -50",
	"quanity2":"51 - 99",
	"quanity3":"100+",
	"price1":"500",
	"price2":"350",
	"price3":"250",
	"cycle":"/year"
}

prices_template = {
	"license":75,
	"tax":0.1,
	"sign":"$",
	"gold":"",
	"sub":"",
	"cart":0.0
}
#used to reset user for another run of the bot
prices = prices_template.copy() 
#End Configs

#reuseable easily digestable upsell table
goldSupportTable = f"""
+------------+------------+
|       Gold Support      |
+------------+------------+
| {"License":<10} | {"Cost":<10} |
+------------+------------+
| {upsell["quanity1"]:<10} | {upsell["price1"]:<10} |
| {upsell["quanity2"]:<10} | {upsell["price2"]:<10} |
| {upsell["quanity3"]:<10} | {upsell["price3"]:<10} | 
+------------+------------+
"""

def receipt():
	receipt = f"""
    		  S.C.A.M. AI™
    		1313 Mockingbird Lane
    
    
    Licenses: 					{userinfo['lic']} @ {prices['sign']}{prices['license']}
    Gold Support:				{f"{prices['sign']}{prices['gold']}{upsell['cycle']}" if userinfo['gold'] else "N/A"}
    
    SubTotal:					{prices['sub']:.2f}
    Tax:					{prices['tax'] * 100:.2f}% 
    
    Total:					{prices['cart']:.2f}
    
    Billing Info:
    Name: {userinfo['name']}
    Phoene: {userinfo['phone']}
    E-mail:{userinfo['email']}
    Last 4 of Card number: ************{userinfo['last4']}
    exp: {userinfo['exp']}
    """

	return receipt

def userbubble():
	return f"{userinfo['name']} > "

def chatbubble(output):
	lines = output.split('\n')
	max_len = max(len(line) for line in lines)

	#top
	top =' ' * 9 + ' ' + '_' * (max_len +2)
	top +='\n' +' ' * 9 + '/' + ' ' * (max_len +2)+ '\\\n'

	#lines
	body = ''
	for line in lines:
		padding = ' ' * (max_len - len(line))
		body +=' ' * 9 +'| ' + line + padding + ' |\n'

	#bottom
	bottom = 'S.C.A.M < '+ ' ' * (max_len +2) + '|'
	bottom += '\n' + ' ' * 9 + '\\' + '_' * (max_len +2) + '/\n'	 
	return top + body + bottom 

def ccvarify():
	print(chatbubble(questions['ccn']))
	while True:
		valid = input(userbubble())
		if 16 >= len(valid) <=19:
			try:
				userinfo['last4'] = valid[-4:]
				valid = int(valid)
				userinfo['key'] = int.from_bytes(userinfo['name'].encode('utf-8'), 'big')
				userinfo['ccn'] = valid ^ userinfo['key']
				return
			except ValueError:
				print(chatbubble("Please enter a valid credit card number."))
		else:
			print(chatbubble("Please enter a valid credit card number"))
	return

def buy():
	print(chatbubble(f"{userinfo['name']},\nWelcome to our Totally secure checkout portal."))
	print(chatbubble(questions['email']))
	userinfo['email']=input(userbubble())
	print(chatbubble(questions['phone']))
	userinfo['phone']=input(userbubble())
	#ask for cc info varify obfuscat and store credit card number
	ccvarify()
	print(chatbubble("Exp date? Format : MM/YY"))
	userinfo["exp"]=input(userbubble())
	print(chatbubble(questions['cvc']))
	userinfo['cvc'] = input(userbubble())
	print(chatbubble(questions['zip']))
	userinfo['zip'] = input(userbubble())
	print(chatbubble("Great Thanks for that here is a copy of your Receipt \nThank you for your purchase!"))
	time.sleep(2)

	#calcuate costs to be printed on the recipt
	#In the receipt output, include the customer's name, phone number, email address, 
	#the credit #card number, and expiration date.
	#Output a receipt using all of the variables you have input. 
    #Be sure to show the total license #number, 
    #the amount for each license, the subtotal, tax, and total amount due
     	#Apply 10% tax for the total bill. 
	#Calculate the total amount due. Store the values input to a variable.
	if userinfo['gold']:
		userinfo['lic'] = int(userinfo['lic'])
		if userinfo['lic'] <= 50:
			prices['gold'] = 500
		elif userinfo['lic'] <= 99:
			prices['gold'] = 350
		else:
			prices['gold'] = 250
 	#MATH
 	if userinfo['gold']:
 		prices['sub'] = float(prices['license'] * userinfo['lic'] + prices['gold'])
 	else:
 		prices['sub'] = float(prices['license'] * userinfo['lic'])

	prices['cart'] =prices['sub'] + prices['sub'] * prices['tax']

	print(receipt())
	time.sleep(2)
	print(chatbubble("Thanks for your purchase, and have the day you deserve!"))
	return

#If yes -- continue to the following items:
def purchase():
	#Each chatbot license costs $75. Calculate and display their current total.  Store the values #input to a variable.
	#Ask for how many chatbot licenses they would like to purchase. Store the values input to a #variable.
	print(chatbubble(f"Exelent, {userinfo['name']},\n {questions['quanity']}\n They are {prices['sign']}{prices['license']} each"))
	userinfo["lic"] = input(userbubble())
	time.sleep(1)
	print(chatbubble(questions['VIP']))
	time.sleep(1)
	print(chatbubble("Here is the Cost breakdown of Gold Support:")) 
	time.sleep(1)
	print(chatbubble(goldSupportTable))
	
	gold =input(userbubble()).strip().lower()
	if gold == 'yes':
		userinfo['gold'] = True
	else:
		userinfo['gold'] = False
	confirm = f"Great {userinfo['name']},\n" + f"We currently have you down for {userinfo['lic']} licenses of S.C.A.M"+("\nand Gold Support!" if userinfo['gold']== True else "")

	print(chatbubble(confirm))
	print(chatbubble(f"Would you like to checkout, {userinfo['name']}?"))
	checkout = input(userbubble()).strip().lower()
	if checkout == 'yes':
		buy()
	else:
		confirm()
	return

def confirm():
	#Ask if your customer would like to make a purchase.
	print(chatbubble(questions["purchase"]))
	buy = input(userbubble()).strip().lower()
	if buy == 'yes':
		purchase()
	else:
		return
	return

def main():
	#userbubble = f"{userinfo['name']} > "
	print(chatbubble(intro))
	time.sleep(1)
	#Ask for the customer's first and last name. Store the values input to a variable.
	print(chatbubble(questions['name']))
	userinfo['name'] = input(userbubble())
	#userinfo['name']=input(f"{userinfo['name']} > ")
	#userbubble = f"{userinfo['name']} > "
	print(chatbubble(f"Welcome {userinfo['name']}!")) #Greet your customer using their full name.
	time.sleep(1)
	print(chatbubble(overview(userinfo['name'])))
	time.sleep(1)
	confirm()
	return

if __name__ == "__main__":
	while True:
		main()
		#Ask the customer if they would like to restart the ChatBot.
		print(chatbubble(questions["restart"]))
		check = input(userbubble()).strip().lower()
		if check == "yes":
			userinfo = userinfo_template.copy()
			prices = prices_template.copy()
		else:
			#If no - thank the customer by name and say goodbye.
			print(chatbubble(f" Bye {userinfo['name']}!"))
			break
