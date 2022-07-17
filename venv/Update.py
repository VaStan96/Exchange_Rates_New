from datetime import datetime, timedelta
import main_Window

def Update_Window (upd_time, list_rates):
    dic_rates = dict(zip([1,2,3,4,5],['EUR','USD','GBR','JPY','CNY']))
    req_time = datetime.now()+ timedelta(minutes = upd_time)
    req_time = req_time.strftime("%H:%M:%S")
    lbl_time['text'] = "Следующее обновление в "+req_time
    a = dic_rates[1]
