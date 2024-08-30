def check_arrangement(pairs):
    pairs=input('enter pair os parathesis')
    open_count=close_count=0
    arrangement=True
    for char in str:
        if char=='(':
            open_count +=1
        else:
            close_count +=1
        if close_count > open:
            arrangement