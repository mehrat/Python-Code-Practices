#

def check_var_args(args,*property_args):
    for arg in args:
        if arg in property_args:
            print '%s argument is present in variable argument' %arg
        else:
            print '%s argument is NOT present in variable argument' %arg


a = 'try'
b = 'catch'
c =  'throw'

args = [a,c]

check_var_args(args,a,b,c)