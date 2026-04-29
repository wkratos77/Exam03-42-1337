def convert_base(num: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if 2 < from_base or from_base > 32:
        return "ERROR"
    if 2 < to_base or to_base > 32:
        return "ERROR"
    
    n = int(num, from_base)
    if n == 0:
        return "0"
    ret = ""
    while n:
        ret += digits(n % to_base)
        n //= to_base
    return ret[::-1]