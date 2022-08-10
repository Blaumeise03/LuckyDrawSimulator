import random

# All items of the Lucky Draw. Must not contain duplicate names!
items = [
    "Cloud AI",
    "300k SP",
    "Wave Graph",
    "Medium Core",
    "Repro. Mats",
    "Experiment D.",
    "2m Lazarus",
    "1m SP",
    "Cloud AI 2",
    "Cap Skin",
    "Repro. Mats 2",
    "Large Core"
]

# The weights of all the items
weights = [8, 8, 10, 2, 8, 8, 8, 3, 8, 8, 8, 1]

# Contains how often each item was drawn during each round
res = None  # type: list[dict] | None

# Unused, saves the cost of each round
costs = [4, 6, 8, 12, 14, 16, 18, 24, 26, 28, 30, 36]


def setup():
    # Set up the result array
    global res
    res = []
    counter = {}
    for item in items:
        counter[item] = 0
    for j in range(12):
        res.insert(j, counter.copy())


def sim_rolls():
    global res
    # Creates a copy to modify the weights after each draw
    wheel = weights.copy()
    # Simulate the lucky wheel drawings
    for j in range(12):
        # Gets the next item
        rand = random.choices(items, wheel)[0]
        # Sets the weight of this item to zero as it can't be drawn again
        wheel[items.index(rand)] = 0
        # Increment the counter for the item rand for round j
        res[j][rand] += 1


if __name__ == '__main__':
    setup()
    i = 1
    while i < 1000001:
        sim_rolls()
        i += 1
    # Formats results, so it can be pasted into a worksheet
    # Header line
    line = "Rolls	"
    for key in items:
        line += f"{key}	"
    print(line)
    # Body lines
    for k in range(12):
        line = f"{k + 1}	"
        for value in res[k].values():
            line += f"{value}	"
        print(line)
