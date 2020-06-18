'''
edabit challenge Switching Between Pencils link: https://edabit.com/challenge/MFteyMABeuGaga3a7
'''


def color_pattern_times(cols):
    # if the length of cols is 0
    # return 0

    # if the length of cols is 1
    # return 2

    # the time spent coloring is the number of colors * 2
    coloring_time = len(cols) * 2

    # loop through cols
    # count the number of times that
    # the current color does not match
    # the previous color
    switch_count = 0
    for idx, curr_color in enumerate(cols):
        if idx > 0:
            prev_color = cols[idx - 1]

            if prev_color != curr_color:
                switch_count += 1

    # return the coloring time plus the switch count
    return coloring_time + switch_count
