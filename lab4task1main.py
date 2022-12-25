import quicksort 
import hairbrushsort
import timeit

t = timeit.timeit()

def function():
    print('type the list:')
    a = list(eval(input()))
    print('Choose a sort method: quicksort or comb')
    b = input()
    
    if b in 'quicksort':
        quicksort.quick_sort(a)
        print(a)
        print(t)
    
    elif b in 'comb':
        hairbrushsort.comb(a)
        print(a)
        print(t)

    else:
        print('error')
        
function()