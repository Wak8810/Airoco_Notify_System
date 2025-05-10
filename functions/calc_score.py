def get_co2_score(data: list):
    ele = int(data[3])
    
    if ele < 900:
        return 0
    elif ele >= 900 and ele < 1000:
        return 1
    else: # 二酸化炭素が多く息苦しい状態
        return 2
    
def get_low_temp_score(data: list):
    ele = float(data[4])

    if ele > 18:
        return 0
    elif ele == 18:
        return 1
    else: # 室温が低い
        return 2
    
def get_high_temp_score(data: list):
    ele = float(data[4])

    if ele < 27:
        return 0
    elif ele == 28:
        return 1
    else: # 室温が高い
        return 2

def get_low_humi_score(data: list):
    ele = float(data[5])

    if ele > 45:
        return 0
    elif ele >= 40 and ele <= 45:
        return 1
    else: # 湿度が低く乾燥しており，風邪を引きやすい
        return 2
    
def get_high_humi_score(data: list):
    ele = float(data[5])

    if ele < 55:
        return 0
    elif ele >= 55 and ele <= 60:
        return 1
    else: # 湿度が高く，カビやダニが発生しやすい
        return 2
    
def get_total_score(data: list):
    co2_score = get_co2_score(data)
    low_temp_score = get_low_temp_score(data)
    high_temp_score = get_high_temp_score(data)
    low_humi_score = get_low_humi_score(data)
    high_humi_score = get_high_humi_score(data)
    total_score = co2_score + low_temp_score + high_temp_score + low_humi_score + high_humi_score

    return total_score