
def make_message(period_data: list):
    messages = ""
    for i in range(len(period_data)):
        message = ""
        message += "{}限目\n".format(i+1)
        message += "*CO2のスコア: {}*\n".format(period_data[i][0])
        message += "*温度のスコア: {}*\n".format(min(period_data[i][1], period_data[i][2]))
        message += "*湿度のスコア: {}*\n".format(min(period_data[i][3], period_data[i][4]))
        alert_messages = ""
        alert_messages += alert_co2(period_data[i][0])
        alert_messages += alert_temperature(period_data[i][1], period_data[i][2])
        alert_messages += alert_humidity(period_data[i][3], period_data[i][4])
        if(alert_messages == ""):
            alert_messages = "良い環境でした！"
        message += "評価: {}\n".format(alert_messages)
        messages += message
    return messages

def alert_co2(co2_score: int):
    if co2_score == 1:
        return "二酸化炭素濃度が悪い状態でした。換気を忘れずに！"
    return ""

def alert_temperature(high_temp_score: int, low_temp_score: int):
    if high_temp_score == 1:
        return "温度が高い状態でした。暖房を忘れずに！"
    elif low_temp_score == 1:
        return "温度が低い状態でした。冷房を忘れずに！"
    return ""

def alert_humidity(high_humidity_score: int, low_humidity_score: int):
    if high_humidity_score == 1:
        return "湿度が高い状態でした。除湿を忘れずに！"
    elif low_humidity_score == 1:
        return "湿度が低い状態でした。加湿を忘れずに！"
    return ""
    
    