def is_subsequence(t: str, s: str) -> bool:
    if len(s) == 0:
        return True

    main_indicator, sub_indicator = 0, 0

    while main_indicator < len(t) and sub_indicator < len(s):

        if t[main_indicator] == s[sub_indicator]:
            sub_indicator += 1

        main_indicator += 1
    
    return sub_indicator == len(s)
    