def solution(sizes):
    max_width = 0
    max_height = 0

    for card in sizes:
        width = max(card)
        height = min(card)

        if width > max_width:
            max_width = width
        if height > max_height:
            max_height = height

    return max_width * max_height