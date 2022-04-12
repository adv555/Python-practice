def first(size,*args ):
    # return sum size plus all args
    return size + len(args)

def second(size,**args ):
    # return sum size plus all args
    return size + len(args)
    
print(first(5, "first", "second", "third"))
print(second(3, comment_one="first", comment_two="second", comment_third="third"))