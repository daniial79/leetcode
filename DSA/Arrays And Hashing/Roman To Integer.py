def romanToInt(s: str) -> int:

    convertion_table: dict[str, int] = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    
    res = 0

    indicator = 0
    while indicator < len(s):

        if convertion_table.get(s[indicator: indicator+2]):
            res += convertion_table.get(s[indicator: indicator+2])
            indicator += 2
            continue
        
        res += convertion_table[s[indicator]]
        indicator += 1

    return res
