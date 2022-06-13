import tkinter as tk

window = tk.Tk()

lbl_calc_result = tk.Label(
    master=window,
    text='0',
    width=30,
    height=3,
)
lbl_calc_result.grid(row=0, column=0, columnspan=4)


def is_last_number_float(current):
    for char in current[::-1]:
        if char == '.':
            return True
        if char in ['+','*','-']:
            return False
        
    return False   


def insert_number_in_calc_result(btn_text):
    current = lbl_calc_result['text']
    
    if btn_text == 'C':
        lbl_calc_result['text'] = '0'
    elif current == '0':
        lbl_calc_result['text'] = btn_text
    elif btn_text == '=':
        result = f'{eval(current)}'
        lbl_calc_result['text'] = result
    elif btn_text == '.':
        if not is_last_number_float(current):
            lbl_calc_result['text'] += btn_text
    elif btn_text in ['+', '-', '*'] and current[-1] in ['+', '-', '*']:
        lbl_calc_result['text'] = current[:-1] + btn_text
    else:
        lbl_calc_result['text'] += btn_text
             
     
calc_keys = [
    {
        'text' : '7',
        'command' : lambda: insert_number_in_calc_result('7'),
    },
    {
        'text' : '8',
        'command': lambda: insert_number_in_calc_result('8'),
    },
    {
        'text' : '9',
        'command': lambda: insert_number_in_calc_result('9'),
    },
    {
        'text' : '*',
        'command': lambda: insert_number_in_calc_result('*'),
    },
    {
        'text' : '4',
        'command' : lambda: insert_number_in_calc_result('4'),
    },
    {
        'text' : '5',
        'command': lambda: insert_number_in_calc_result('5'),
    },
    {
        'text' : '6',
        'command': lambda: insert_number_in_calc_result('6'),
    },
    {
        'text' : '-',
        'command': lambda: insert_number_in_calc_result('-'),
    },
    {
        'text' : '1',
        'command' : lambda: insert_number_in_calc_result('1'),
    },
    {
        'text' : '2',
        'command': lambda: insert_number_in_calc_result('2'),
    },
    {
        'text' : '3',
        'command': lambda: insert_number_in_calc_result('3'),
    },
    {
        'text' : '+',
        'command': lambda: insert_number_in_calc_result('+'),
    },
    {
        'text' : '0',
        'command': lambda: insert_number_in_calc_result('0'),
    },
    {
        'text' : '.',
        'command': lambda: insert_number_in_calc_result('.'),
    },
    {
        'text' : 'C',
        'command': lambda: insert_number_in_calc_result('C'),
    },
    {
        'text' : '=',
        'command' : lambda: insert_number_in_calc_result('='),
    },
]

calc_keys_objs = []

for calc_key_data in calc_keys:
    btn = tk.Button(
    master=window,
    text=calc_key_data['text'],
    command=calc_key_data['command'],
    height=3
    )
    calc_keys_objs.append(btn) 
    
for i, calc_key_obj in enumerate(calc_keys_objs):
    calc_key_obj.grid(row= (i//4)+1, column= i%4, sticky='nsew')
        

window.mainloop()