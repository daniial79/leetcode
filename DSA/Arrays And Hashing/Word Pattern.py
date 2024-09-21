def word_pattern(pattern: str, s: str) -> bool:
            
    words = s.split(" ")

    if len(pattern) != len(words):
        return False


    map_tracker: dict[str, str] = {}
    
    for i in range(len(pattern)):
        # check for identical keys and different values + loading map_tracker
        if (val := map_tracker.get(pattern[i])) and val != words[i]:
            return False
        else:
            map_tracker[pattern[i]] = words[i]


    # check for different keys and identical values
    return len(set(map_tracker.keys())) == len(set(map_tracker.values()))


