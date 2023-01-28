# ========================================= sum_() , max_() and min_() =========================================

def sum_(*son):
    yidingi1 = 0
    for i in son:
        yidingi1 += i
    return yidingi1

def max_(*son):
    katta = son[0]
    for i in son:
        if i > katta:
            katta = i
    return katta

def min_(*son):
    katta = son[0]
    for i in son:
        if i < katta:
            katta = i
    return katta

# ========================================= '<' , '>' and '=' =========================================

# def katta(son1,son2):
#     '''Ushbu dastur sizga ikkta a va b qiymatlarni solish tirib kattasini topib beradi'''
#     if son1 > son2:
#         print(son1)
#
# print(katta(1,2))