def solution(w, h):
    if w == h:
        return w * h - w
    larger = max(w, h)
    smaller = min(w, h)
    while larger and smaller:
        smaller,larger = larger % smaller, smaller
    gcd = larger

    return w*h - (w+h-gcd)


print(solution(8, 12))
