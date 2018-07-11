def culc_average(bats, hits):
    average = hits / bats

    average_str = to_str_ratio(average)

    return average_str


def to_str_ratio(ratio):
    # ratio_str = ""
    if ratio != 1.0:
        ratio_str = '{:.3f}'.format(ratio)
        ratio_str = ratio_str[1:]
    else:
        ratio_str = "1.000"
    return ratio_str


average = culc_average(20, 10)
print(average)




