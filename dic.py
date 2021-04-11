import sys
hevin = {
    "carname":"i10",
    "model":2011,
    "insurance":"yes"
    }
Ranjan = {
    "carname":"innova",
    "model":2013,
    "insurance":"yes"
    }
if (sys.argv[1] == "Ranjan"):
    a = Ranjan
elif (sys.argv[1] == "hevin"):
    a = hevin
else:
    a = "none"

print(a)

