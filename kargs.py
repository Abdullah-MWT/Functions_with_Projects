# +++++ 

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_kwargs(name = 'Abdullah', work = 'Developer')
print_kwargs(work = 'Developer', name = 'Abdullah')
print_kwargs(name = 'Abdullah')