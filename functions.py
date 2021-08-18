from numpy import mean, std


def found_critical_value(sel):
    sel.sort()
    sel1 = sel.copy()
    del sel1[0]
    m1, sko1 = mean(sel1), std(sel1, ddof=1)
    if abs(sel[0] - m1) > (3 * sko1):
        critic_val = sel[0]
    else:
        sel3 = sel.copy()
        del sel3[-1]
        m3, sko3 = mean(sel3), std(sel3, ddof=1)
        if abs(sel[-1] - m3) > (3 * sko3):
            critic_val = sel[-1]
        else:
            critic_val = 'limbo'
    return critic_val


def replace_letter_of_name(name):
    list_old = ['е', 'у', 'о', 'р', 'х', 'а', 'с']
    list_new = ['e', 'y', 'o', 'p', 'x', 'a', 'c']
    name_new = name
    for n, i in enumerate(list_old):
        name_new = name_new.replace(i, list_new[n])
    return name_new
