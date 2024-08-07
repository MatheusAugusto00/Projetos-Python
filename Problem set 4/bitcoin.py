#import json
import requests
import sys

try:
    bitcoin_number=float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #print(json.dumps(response.json(), indent=2))
    full_data=response.json()
    usd_data=full_data["bpi"]["USD"]
    bitcoin_value=usd_data["rate"]
    bitcoin_value=float(bitcoin_value.replace(",",""))
    bitcoin_value_multiplied=bitcoin_value*bitcoin_number
    print(f"${bitcoin_value_multiplied:,.4f}")

except IndexError:
    sys.exit("Missing command-line argument")

except ValueError:
    sys.exit("Command-line argument is not a number")




