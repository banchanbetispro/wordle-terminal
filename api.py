from requests import get
#from pprint import PrettyPrinter

#Initialize printer
#printer = PrettyPrinter()
data = get("https://www.randomlists.com/data/words.json").json()["data"]