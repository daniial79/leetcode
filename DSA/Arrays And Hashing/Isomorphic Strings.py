def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_tracker: dict[str, list[int]] = {}
    t_tracker: dict[str, list[int]] = {}

    # at this point we know s and t are same in length
    for i in range(len(s)):
        update_tracker(s_tracker, s[i], i)
        update_tracker(t_tracker, t[i], i)

    # change s_tracker dictionary keys to t_tracker keys preserving it's values to compare
    t_keys = t_tracker.keys()    
    s_tracker_maped = dict(zip(t_keys, list(s_tracker.values())))
    
    return s_tracker_maped == t_tracker

def update_tracker(tracker: dict[str, list[int]], char: str, idx: int):
    if tracker.get(char):
        tracker[char].append(idx)
    else:
        tracker.setdefault(char, [idx])

is_isomorphic("egg", "add")