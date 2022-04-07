from worldoftanks import WotAPI

wot = WotAPI(application_id='b014x6677gg7y',
             account_id='954317632',
             token='54595037',
             realm='eu')

wot.player_personal()
wot.player_vehicles()
wot.player_achievements()


wot.tankopedia_vehicles(load_once=True)

wot.tankopedia_achievements(load_once=True)

wot.tankopedia_information(load_once=True)
wot.tankopedia_maps(load_once=True)

wot.tankopedia_badges(load_once=True)



wot.vehicle_achievements()
wot.vehicle_statistics()

achievements = wot.player_achivements(load_once=True)
print(achievements)

[{
'name': 'MOXHATKA_B_3AKOHE', 
'outdated': True, 
'section': 'action', 
'section_order': 6, 
'image_big': 'http://api.worldoftanks.eu/static/2.66.0/wot/encyclopedia/achievement/big/medalBobAmway921.png', 
'hero_info': None, 
'name_i18n': None, 
'order': 1443, 
'type': 'single', 
'image': 'http://api.worldoftanks.eu/static/2.66.0/wot/encyclopedia/achievement/medalBobAmway921.png', 
'condition': 'None', 
'description': None
}]