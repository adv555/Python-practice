health=[[1, 1, 5, 10], [10, 2], [1, 1, 1]]
user=1


def game(terra, power):
    

    for i in terra:
        for el in i:
            if el <= power:
                power+=el
            else:
                break


    return power





print(game(health, user))