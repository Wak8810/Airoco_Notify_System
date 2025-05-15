def get_co2_score(data: list):
    ele = int(data[0])
    
    if ele < 900:
        return 3
    elif ele >= 900 and ele <= 1000:
        return 2
    else: # 二酸化炭素が多く息苦しい状態
        return 1
    
def get_high_temp_score(data: list):
    ele = float(data[1])

    if ele < 26:
        return 3
    elif ele >= 26 and ele <= 28:
        return 2
    else: # 室温が高い
        return 1

def get_low_temp_score(data: list):
    ele = float(data[1])

    if ele > 19:
        return 3
    elif ele >= 17 and ele <= 19:
        return 2
    else: # 室温が低い
        return 1

def get_high_humi_score(data: list):
    ele = float(data[2])

    if ele < 60:
        return 3
    elif ele >= 60 and ele <= 70:
        return 2
    else: # 湿度が高く，カビやダニが発生しやすい
        return 1

def get_low_humi_score(data: list):
    ele = float(data[2])

    if ele > 50:
        return 3
    elif ele >= 40 and ele <= 50:
        return 2
    else: # 湿度が低く乾燥しており，風邪を引きやすい
        return 1
    
    
def get_period_scores(data: list):
    for ele in data:
        if ele == None:
            return data
        co2 = get_co2_score(ele)
        high_temp = get_high_temp_score(ele)
        low_temp = get_low_temp_score(ele)
        high_humi = get_high_humi_score(ele)
        low_humi = get_low_humi_score(ele)
        ele.insert(0, co2)
        ele.insert(1, high_temp)
        ele.insert(2, low_temp)
        ele.insert(3, high_humi)
        ele.insert(4, low_humi)
    
    return data
