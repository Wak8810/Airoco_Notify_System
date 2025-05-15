
def make_message(period_scores: list, cl_num: int):
    messages = ""
    classroom = ['本日のＲ３ー３０１教室における環境をお知らせいたします\n\n', 
                 '本日のＲ３ー４０１教室における環境をお知らせいたします\n\n', 
                 '本日のＲ３ー４０３教室における環境をお知らせいたします\n\n']
    cl_mes = classroom[cl_num]
    for i in range(len(period_scores)):
        if period_scores[i] != None:
            message = ""
            message += "{}限目\n".format(i+1)
            message += "*CO2のスコア: {}*\n".format(period_scores[i][0])
            message += "*温度のスコア: {}*\n".format(min(period_scores[i][1], period_scores[i][2]))
            message += "*湿度のスコア: {}*\n".format(min(period_scores[i][3], period_scores[i][4]))
            alert_messages = ""
            alert_messages += alert_co2(period_scores[i][0])
            alert_messages += alert_temperature(period_scores[i][1], period_scores[i][2])
            alert_messages += alert_humidity(period_scores[i][3], period_scores[i][4])
            if(alert_messages == ""):
                alert_messages = "良い環境でした！"
            message += "評価: {}\n".format(alert_messages)
            messages += message
    
    send_message = cl_mes + messages
    return send_message

def alert_co2(co2_score: int):
    if co2_score == 1:
        return "二酸化炭素濃度が悪い状態でした。換気を忘れずに！"
    elif co2_score == 2:
        return "二酸化炭素濃度の上昇に注意しましょう。"
    return ""

def alert_temperature(high_temp_score: int, low_temp_score: int):
    if high_temp_score == 1:
        return "室温が高い状態でした。冷房を忘れずに！"
    elif high_temp_score == 2:
        return "高温に注意しましょう。"
    elif low_temp_score == 1:
        return "室温が低い状態でした。暖房を忘れずに！"
    elif low_temp_score == 2:
        return "低温に注意しましょう。"
    return ""

def alert_humidity(high_humidity_score: int, low_humidity_score: int):
    if high_humidity_score == 1:
        return "湿度が高い状態でした。除湿を忘れずに！"
    elif high_humidity_score == 2:
        return "湿度の上昇に注意しましょう。"
    elif low_humidity_score == 1:
        return "湿度が低い状態でした。加湿を忘れずに！"
    elif low_humidity_score == 2:
        return "湿度の低下に注意しましょう。"
    return ""
    
    