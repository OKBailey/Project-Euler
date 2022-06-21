

def spell_number(n: int):
    num_dict = {1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety'}
    huns_plc = int(str(int(n/100))[-1])
    tens_plc = int(str(int(n/10))[-1])
    ones_plc = int(str(n)[-1])

    if ones_plc == 0 and tens_plc == 0:
        if huns_plc == 0:
            spell = 'one thousand'
        else:
            spell = num_dict[huns_plc] + ' hundred'
    elif ones_plc == 0 and tens_plc != 0:
        if huns_plc == 0:
            spell = num_dict[tens_plc*10]
        else:
            spell = num_dict[huns_plc] + ' hundred and ' + num_dict[tens_plc*10]
    elif ones_plc !=0 and tens_plc == 0:
        if huns_plc == 0:
            spell = num_dict[ones_plc]
        else:
            spell = num_dict[huns_plc] + ' hundred and ' + num_dict[ones_plc]
    else:
        if 10 <= int(str(tens_plc) + str(ones_plc)) <= 19:
            if huns_plc == 0:
                spell = num_dict[int(str(tens_plc) + str(ones_plc))]
            else:
                spell = num_dict[huns_plc] + ' hundred and ' + num_dict[int(str(tens_plc) + str(ones_plc))]
        else:
            if huns_plc == 0:
                spell = num_dict[tens_plc*10] + '-' + num_dict[ones_plc]
            else:
                spell = num_dict[huns_plc] + ' hundred and ' + num_dict[tens_plc*10] + '-' + num_dict[ones_plc]
    return spell

def spelled_number_letter_count(bottom_limit, top_limit)
