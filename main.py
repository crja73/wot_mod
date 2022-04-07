from itertools  import count
import wargaming

wot = wargaming.WoT('demo', region='ru', language='ru')


def list_all_provinces():
    fronts = wot.globalmap.fronts()


    for front in fronts:
        for page_no in count(start=1):
        
            provinces = wot.globalmap.provinces(front_id=front['front_id'], page_no=page_no)
            
            if len(provinces) == 0:
                break

            
            for province in provinces:
                print(province['province_name'])


try:
    list_all_provinces()
except wargaming.exceptions.RequestError as e:
    if e.code == 407: 
        print("ERROR")
    else:
        print("Unknown error %s" % repr(e))