from datetime import timedelta, date, datetime as dt

def getDates():    
    today= date.today()
    thirtyDaysBack= today - timedelta(30) 
    dates= {
        "today": today.strftime("%d%b"),
        "thirtyDaysBack": thirtyDaysBack.strftime("%d%b"),
    }
    return dates

def getLastUpdated():
    #only hours needed :)
    return dt.now().strftime("%H")