# !/usr/bin/env python3
# function, that turns degrees of Celcius into Fahrenheit and Fahrenheit into Celcius
def switch_scale(string : str) -> str:
    return str(int(temperature.strip('c'))*(9/5)+32) + 'F°' if string[-1] == 'c' else str(int(temperature.strip('f'))-32*(5/9)) + 'C°'

temperature = input("Insert temperature value and it's scale in valuescale format to turn it into different scale, e.g. 451F; 23C; 96f:").lower().strip()

print(switch_scale(temperature))
