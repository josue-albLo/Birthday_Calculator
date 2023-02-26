from datetime import date, time, datetime

def time_calculator_brtday(date_birthday:str):
    """ This function is a calculator of days for your birthday and
    it shows the missing days

    Args:
        date_birthday (str): In this variable, 
        you should write your birthday in format YYYY-MM-DD
        and it show you the result on the screen
    """
    if len(date_birthday) > 0 and len(date_birthday) <12:
        try:
            data = date_birthday.split('-')
            bday = datetime(int(data[0]),int(data[1]),int(data[2]))
            today = datetime.now()
            diff = bday - today
            print(f'Your birthday will be in {diff}')
        except ValueError as err:
            print(f'Error converting to integer: {err}')
    else:
        print('This string isn\'t no compatible')

def run():
    birthday = input('Enter your birthday in format YYYY-MM-DD: ')
    time_calculator_brtday(date_birthday=birthday)


if __name__=='__main__':
    run()