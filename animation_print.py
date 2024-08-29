from time import sleep
def print_wa(*values : object, sep : object = ' ', have_newline_at_end : bool = True):
    """
    @param values: values you will print it
    @param sep: (Optional) The object that will paste the values you gave together.
    It will print the values you give in a cool way.
    """
    values_list = []
    for value in values:
        values_list.append(value)
    whole_value = sep.join(values_list)
    ELOWV_IL = list(whole_value)
    for letter in ELOWV_IL:
        print(letter, end='', flush=True)
        sleep(0.09)
    sleep(0.1)
    if have_newline_at_end:
        print('\n')
print_wa("hello", 'world', sep='-')