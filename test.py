def args_sum(*args):
    a = list(args)
    try: 
        return sum(a)
    except:
        return "Все аргументы должны являться числами"
print(args_sum(1,2,3,4,5.3, None))