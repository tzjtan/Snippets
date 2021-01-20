from itertools import groupby

def compress_into_dashed_list(integer_list, separator=', '):
    # Examples:
    #     print(turn_into_dashed_string([1,3,7]))                     # Gives "1, 3, 7"
    #     print(turn_into_dashed_string([1,2,3,5,7,8]))               # Gives "1-3, 5, 7-8"
    #     print(turn_into_dashed_string([1,2,3,5,7,8]),separator=',') # Gives "1-3,5,7-8"
    make_string = lambda x:str(x[0]) if len(x)==1 else '{}-{}'.format(x[0],x[-1])
    return separator.join([make_string([gc[1] for gc in g]) for f,g in groupby(enumerate(integer_list), lambda i: i[0]-i[1])])
    

