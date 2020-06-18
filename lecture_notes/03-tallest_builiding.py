'''
edabit challenge Height of the Tallest Building link: https://edabit.com/challenge/LuBtaT9dwStbd7mnK
'''

# Questions
# How do I count height?
# Why are there empty rows?
# How do we group the strings into one building?
# Max input?
# Can buildings overlap?
'''
Example One:
[
  " ",
  "#"
]
Should return "20m"
'''


def tallest_building_height(floors):
    max_floor_count = 0
    # determine longest string
    longest_string = 0

    for floor in floors:
        if len(floor) > longest_string:
            longest_string = len(floor)

     # create a list that keeps track of the
     # number of # that have occurred repeatedly in one column
    floor_streak = [0] * longest_string
    # loop through each string in the input list
    for floor in floors:
        # loop through each char in the current string
        for idx, char in enumerate(floor):
            # if the char is equal to "#"
            if char == "#":
                floor_streak[idx] += 1
                if floor_streak[idx] > max_floor_count:
                    max_floor_count = floor_streak[idx]
            else:
                floor_streak[idx] = 0
    # return max_floor_count * 20 as a string formatted like "height m"
    return str(max_floor_count*20) + "m"
