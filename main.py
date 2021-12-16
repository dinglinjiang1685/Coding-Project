print()

import random

pollresult = []
pollResult = {"mach": 0, "web": 0, "graph": 0, "block": 0, "compro": 0}
pollOption = [
    "machine learning", "web development", "graphic/ui design", "blockchain",
    "competitive programming"
]

pollOptionSimplified = ["mach", "web", "graph", "block", "compro"]

print(
    "Welcome to the SWC Coding Club Poll! Choose an option to explore in Computer Science! Here are some options:"
)
print(pollOption)
print(
    "Enter your option: 'mach' for machine learning, 'web' for web development, 'graph' for graphic/ui design, 'block' for blockchain and 'compro' for competitive programming."
)
for i in range(0, 6):
    print('Person', (i + 1))
    print("Please Enter your Option Here")
    newChoice = input()
    while newChoice not in pollOptionSimplified:
        print("invalid option, please see our options")
        newChoice = input()
    else:
        pollresult.append(newChoice)

machine_learning = pollresult.count("mach")
web_development = pollresult.count("web")
graphic_or_ui_design = pollresult.count("graph")
blockchain = pollresult.count("block")
competitive_programming = pollresult.count("compro")

pollResult["mach"] = machine_learning
pollResult["web"] = web_development
pollResult["graph"] = graphic_or_ui_design
pollResult["block"] = blockchain
pollResult["compro"] = competitive_programming

Tiebreaker = []
def largest():
    name = ""
    high = 0
    for x in pollOptionSimplified:
        i = pollResult[x]
        if (i > high):
            high = i
            name = x
        if (i == high):
            #tiebreaker
            print("there is a tie")
            Tiebreaker.append(x)
            random.choice(Tiebreaker)
    return "The option which get the most votes is: ", name


print(largest())
