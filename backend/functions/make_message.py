def make_message(period_scores: list, cl_num: int, current_date: str):
    messages = ""
    classroom = ['R3-301', 
                 'R3-401', 
                 'R3-403']
    mes_last = "教室における環境をお知らせいたします\n\n"
    cl_mes = "本日({})の".format(current_date) + classroom[cl_num] + mes_last
    
    def get_stars(score: int) -> str:
        if score == 1:
            return "★☆☆"
        elif score == 2:
            return "★★☆"
        elif score == 3:
            return "★★★"
        return "☆☆☆"
    
    # 最初の区切り線
    messages = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"

    messages += cl_mes
    
    for i in range(len(period_scores)):
        if period_scores[i] != None:
            message = ""
            message += "━━━━━━━━━━━━━━━━━━━━\n"
            message += "📚 {}限目\n".format(i+1)
            
            # CO2スコア
            co2_score = period_scores[i][0]
            message += "🌬️ *CO2のスコア*: {}\n".format(get_stars(co2_score))
            
            # 温度スコア
            temp_score = min(period_scores[i][1], period_scores[i][2])
            message += "🌡️ *温度のスコア*: {}\n".format(get_stars(temp_score))
            
            # 湿度スコア
            humidity_score = min(period_scores[i][3], period_scores[i][4])
            message += "💧 *湿度のスコア*: {}\n".format(get_stars(humidity_score))
            
            # 評価メッセージ
            alert_messages = ""
            alert_messages += alert_co2(co2_score)
            alert_messages += alert_temperature(period_scores[i][1], period_scores[i][2])
            alert_messages += alert_humidity(period_scores[i][3], period_scores[i][4])
            
            if(alert_messages == ""):
                message += "✅ *評価*: 良い環境でした！\n"
            else:
                message += "📝 *評価*: {}\n".format(alert_messages)
            
            messages += message
    messages += "詳しい情報はこちらから\nhttps://wak8810.github.io/Airoco_Notify_System/\n"
    
    # 最後の区切り線
    messages += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    
    send_message = messages
    return send_message

def alert_co2(co2_score: int):
    if co2_score == 1:
        return "⚠️ 二酸化炭素濃度が悪い状態でした。換気を忘れずに！"
    elif co2_score == 2:
        return "⚡ 二酸化炭素濃度の上昇に注意しましょう。"
    return ""

def alert_temperature(high_temp_score: int, low_temp_score: int):
    if high_temp_score == 1:
        return "⚠️ 室温が高い状態でした。冷房を忘れずに！"
    elif high_temp_score == 2:
        return "⚡ 高温に注意しましょう。"
    elif low_temp_score == 1:
        return "⚠️ 室温が低い状態でした。暖房を忘れずに！"
    elif low_temp_score == 2:
        return "⚡ 低温に注意しましょう。"
    return ""

def alert_humidity(high_humidity_score: int, low_humidity_score: int):
    if high_humidity_score == 1:
        return "⚠️ 湿度が高い状態でした。除湿を忘れずに！"
    elif high_humidity_score == 2:
        return "⚡ 湿度の上昇に注意しましょう。"
    elif low_humidity_score == 1:
        return "⚠️ 湿度が低い状態でした。加湿を忘れずに！"
    elif low_humidity_score == 2:
        return "⚡ 湿度の低下に注意しましょう。"
    return ""
    
    