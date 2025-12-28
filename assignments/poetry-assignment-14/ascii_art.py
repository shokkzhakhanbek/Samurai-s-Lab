import re

NAMED = {
    "red": (255, 0, 0),
    "green": (0, 200, 0),
    "blue": (0, 120, 255),
}

def parse_color(s):
    if not s:
        return None

    s = s.lower().strip()

    if s in NAMED:
        return NAMED[s]

    if s.startswith("#") and len(s) == 7:
        try:
            r = int(s[1:3], 16)
            g = int(s[3:5], 16)
            b = int(s[5:7], 16)
            return (r, g, b)
        except:
            return None

    m = re.match(r"rgb\((\d+),(\d+),(\d+)\)", s)
    if m:
        return tuple(map(int, m.groups()))

    return None


def build_mask(text, needle):
    if not needle:
        return [True] * len(text)

    mask = [False] * len(text)
    start = 0

    while True:
        idx = text.find(needle, start)
        if idx == -1:
            break

        for i in range(idx, idx + len(needle)):
            if i < len(mask):
                mask[i] = True

        start = idx + 1

    return mask
