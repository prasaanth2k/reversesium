from monisys.Managers.Systeminfo import SystemInfo
load = SystemInfo('load_average')

def loadaverage():
    values = load.get_all_data()
    return values