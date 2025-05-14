def get_co2_score(data: list):
    ele = int(data[3])
    
    if ele < 900:
        return 3
    elif ele >= 900 and ele < 1000:
        return 2
    else: # 二酸化炭素が多く息苦しい状態
        return 1
    
def get_low_temp_score(data: list):
    ele = float(data[4])

    if ele > 18:
        return 3
    elif ele == 18:
        return 2
    else: # 室温が低い
        return 1
    
def get_high_temp_score(data: list):
    ele = float(data[4])

    if ele < 27:
        return 3
    elif ele == 28:
        return 2
    else: # 室温が高い
        return 1

def get_low_humi_score(data: list):
    ele = float(data[5])

    if ele > 45:
        return 3
    elif ele >= 40 and ele <= 45:
        return 2
    else: # 湿度が低く乾燥しており，風邪を引きやすい
        return 1
    
def get_high_humi_score(data: list):
    ele = float(data[5])

    if ele < 55:
        return 3
    elif ele >= 55 and ele <= 60:
        return 2
    else: # 湿度が高く，カビやダニが発生しやすい
        return 1