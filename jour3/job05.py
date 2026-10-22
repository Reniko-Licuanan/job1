for i in range( 2, 1001 ):
    est_premier = True 

    for diviseur in range( 2, i):
        if i % diviseur == 0: 
            est_premier= False
            break

    if est_premier:
        print( i )