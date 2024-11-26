from math import floor

def tagToId(tag):
    try:
        tag, total, i, arr = [x for x in tag.upper().replace("#", "").replace("O", "0")], 0, 0, ["0", "2", "8", "9", "P", "Y", "L", "Q", "G", "R", "J", "C", "U", "V"]
        while len(tag) > 0:
            ch = tag.pop()
            total += arr.index(ch) * pow(14, i)
            i += 1
        total = int(total)
        highID, lowID = total % 256, floor(total / 256)
        return highID, lowID
    except:
        pass