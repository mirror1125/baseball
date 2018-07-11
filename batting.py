def calc_ba(ab, hits):
    """
    calclate batting average
    :param ab: at bats
    :param hits: hits
    :return:
    """
    ba = hits / ab
    ba_str = to_str_ratio(ba)

    return ba_str


def calc_slg(tb, ab):
    """
    calculate slugging average(SLG)
    :param tb: total bases
    :param ab: at bats
    :return: SLG
    """
    slg = tb / ab
    slg_str = to_str_ratio(slg)

    return slg_str


def calc_tb(single, double, triple, hr):
    """
    calculate total bases(TB)
    :param single: number of single hits[int]
    :param double: number of double hits[int]
    :param triple: number of triple hits[int]
    :param hr: number of Home Run(HR)[int]
    :return: TB[int]
    """

    tb = single + (2 * double) + (3 * triple) + (4 * hr)

    return tb


def to_str_ratio(ratio):
    """
    ratio[float] to ratio[str](ex: .289)
    :param ratio: ratio[float](ex: 0.314543...)
    :return: ratio[str] (ex: .314, 1.215, etc)
    """
    if ratio != 1.0:
        ratio_str = '{:.3f}'.format(ratio)
        ratio_str = ratio_str[1:]
    else:
        ratio_str = "1.000"
    return ratio_str






