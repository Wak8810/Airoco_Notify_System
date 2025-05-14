#引数は，ある時限のデータ(period_data[0]など)
#ある時限の各値の平均が入ったリストを返す
#[CO2平均，Temp平均，humi平均]
def get_ave(data: list):
    elements = [0,0,0]
    wari = len(data)
    for ele in data:
        elements[0] += int(ele[3])
        elements[1] += int(ele[4])
        elements[2] += int(ele[5])
    if(wari == 0):
        return
    elements[0] //= wari
    elements[1] //= wari
    elements[2] //= wari
    return elements
        