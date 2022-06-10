import tkinter as tk

window = tk.Tk()

lbl_calc_result = tk.Label(
    master=window,
    text='0',
    width=30,
    height=3,
)
lbl_calc_result.grid(row=0, column=0, columnspan=4)

calc_keys = [
    {
        'text' : '7',
        'command' : lambda: print('7'),
    },
    {
        'text' : '8',
        'command': lambda: print('8'),
    },
    {
        'text' : '9',
        'command': lambda: print('9'),
    },
    {
        'text' : '+',
        'command': lambda: print('+'),
    },
      {
        'text' : '4',
        'command' : lambda: print('4'),
    },
    {
        'text' : '5',
        'command': lambda: print('5'),
    },
    {
        'text' : '6',
        'command': lambda: print('6'),
    },
    {
        'text' : '-',
        'command': lambda: print('-'),
    },
      {
        'text' : '1',
        'command' : lambda: print('1'),
    },
    {
        'text' : '2',
        'command': lambda: print('2'),
    },
    {
        'text' : '3',
        'command': lambda: print('3'),
    },
    {
        'text' : '*',
        'command': lambda: print('*'),
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
    if i // 4 == 0:
        calc_key_obj.grid(row= (i//4)+1, column= i%4, sticky='nsew')
        

window.mainloop()