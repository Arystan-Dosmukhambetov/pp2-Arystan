def sum_all(*args):
    return sum(args)

def show_info(**kwargs):
    return kwargs

print(sum_all(1, 2, 3))
print(show_info(name="Arystan", age=20))
