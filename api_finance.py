import requests




r = requests.get('http://data.fixer.io/api/latest?access_key= [your key]')
jresponse = r.json()
num = jresponse["rates"]["USD"]

dollarrate = 100/num

print(dollarrate)

print(jresponse)

# if str(dollarrate) > str(saved_rate):
#     notification.send_email("For 100 Dollars, you will receive " + str(dollarrate) + " Euros")
#
#     with open('/root/fx_rate/priorrate.txt','w') as pr:
#         pr.write(str(dollarrate))

