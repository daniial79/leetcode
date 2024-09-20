def longest_common_prefix(strs: list[str]) -> str:
    primary_guess = strs[0]

    for string in strs[1:]:

        limit = min(len(primary_guess), len(string))

        temp = ""

        for i in range(limit):
            
            if primary_guess[i] != string[i]:
                break

            temp += string[i]

        if temp == "":
            return temp
        
        if len(temp) < len(primary_guess):
            primary_guess = temp
    
    return primary_guess