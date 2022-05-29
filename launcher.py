import builtins
import gettext
import os
from os.path import exists
import configparser

from bidict import bidict
import PySimpleGUI as sg
from configparser import ConfigParser

if not callable(getattr(builtins, '_', None)):
    def identity(x): return x
    builtins.__dict__['_'] = identity

ip_address_list = ['example.com:5555', '192.168.1.7:5555']
lang = 'ENG'

parser = ConfigParser()
with open("./keeperfx.cfg") as stream:
    parser.read_string("[top]\n" + stream.read())  # trick config parser to treat cfg as an ini
    config = parser['top']
    lang = config["LANGUAGE"]


LOCALE_DIR = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'lang')
language = gettext.translation(
    'fxLauncher',
    languages=[lang],
    localedir=LOCALE_DIR,
    fallback=True)
language.install()




human_ids_dict={
    _('0 (Red)'):0,
    _('1 (Blue)'):1,
    _('2 (Green)'):2,
    _('3 (Yellow)'):3
    }
human_ids=list(human_ids_dict.keys())

dict_languages={
    "English"   :"ENG",
    "Français"  :"FRE",
    "Deutsch"   :"GER",
    "Italiano"  :"ITA",
    "Español"   :"SPA",
    "Svenska"   :"SWE",
    "Polski"    :"POL",
    "Nederlands":"DUT",
   #"Hungarian" :"HUN",
    "한국어"    :"KOR", 
   #"Dansk"     :"DAN",
   #"Norsk"     :"NOR",
    "Česky"     :"CZE",
   #"Arabic"      :"ARA",
    "Русский"     :"RUS",
    "日本語"       :"JPN",
    "简化中国"     :"CHI",
    "傳統的中國"   :"CHT",
   #"Portuguese   :"POR",
   #"Hindi"       :"HIN",
   #"Bengali"     :"BEN",
   #"Javanese"    :"JAV",
    "sermo Latinus":"LAT",
    }
languages=list(dict_languages.keys())
inv_dict_languages = bidict(dict_languages).inverse

resolutions = ['1024x600','1024x768','1280x720','1280x1024','1366x768','1536x684','1600x900','1920x1080','2560x1440']

wibble_options_dict={
    _("On")          :"ON",
    _("Off")         :"OFF",
    _("Liquid Only") :"LIQUIDONLY",
    }
wibble_options=list(wibble_options_dict.keys())
inv_dict_wibble = bidict(wibble_options_dict).inverse
    
dict_movie_resize_options={
    _("On")                 :"ON",
    _("Off")                :"OFF",
    _("Fit")                :"FIT",
    _("Stretch")            :"STRETCH",
    _("Crop")               :"CROP",
    _("Pixel Perfect")      :"PIXELPERFECT",
    _("4by3")               :"4BY3",
    _("4by3 Pixel Perfect") :"4BY3PP",
    }
movie_resize_options=list(dict_movie_resize_options.keys())
inv_dict_movie_resize_options = bidict(dict_movie_resize_options).inverse

atmos_sound_options_dict={
    _("Off")      :"OFF",
    _("Low")      :"LOW",
    _("Medium")   :"MEDIUM",
    _("High")     :"HIGH",
    }
atmos_sound_options=list(atmos_sound_options_dict.keys())
inv_dict_atmos_sound_options = bidict(atmos_sound_options_dict).inverse

atmos_sound_volumes_dict={
    _("Low")     :"LOW",
    _("Medium")  :"MEDIUM",
    _("High")    :"HIGH",
    }
atmos_sound_volumes=list(atmos_sound_volumes_dict.keys())
inv_dict_atmos_sound_volumes = bidict(atmos_sound_volumes_dict).inverse

dict_bool={
    True  : "ON",
    False : "OFF"
    }
inv_dict_bool = bidict(dict_bool).inverse


dict_compuchat_opts= {
    _("Off")        :"",
    _('Scarce')     :"scarce",
    _('Frequent')   :"frequent"
    }
compuchat_opts=list(dict_compuchat_opts.keys())

packet_opts= [_("Off"),_('Save'),_('Load')]



#tooltips run options

#               _("Command line to run. Here you can type by hand the parameters you wish to use.")
tt_heavylog =  _("You usually want standard version, as it is fast and stable.\n Heavylog version logs huge amount of messages to a file \"keeperfx.log\" while you're playing.\n This requires a lot more of computation power, so on slower machines it might severely affect gameplay speed.\n But if the game will crash, the LOG file may help the developers to fix the problem.")
#        _("Switches which you can enable or disable. Their function is explained in readme file. If you don't want to see the intro over and over again, select \"Skip intro\". If you're having problems with keyboard or mouse inside the game, select \"Alt. input\".")
#        _("Gameplay speed. Increasing amount of turns per second will make the action faster. Note that you can temporarely unlock the speed limiter with Ctrl+'+'.")
tt_human_id = _("Change human player ID. This allows you to play as blue, green or yellow keeper.\nUse this option for skirmish - single player levels won't work properly with it, unless they were especially designed for human to play as another keeper.")
#        _("Set the video driver to be used by SDL library. Valid options on Windows host are 'directx' and 'windib'. Use this if your system is broken and most games do not work on it.")
#        _("Host/peer addresses required to join a TCP/IP game. See 'tcp_readme.txt' to get detailed instructions on making multiplayer work.")
#        _("Loads a previously created packet file. Starts the level for which packet file was created, and continues the gameplay. You may exit this mode by pressing Alt+X, or take over the control by pressing Alt+T.")
#        _("Writes a packet file (replay file) when playing. After using this option, you must start a new level and play it continuously to create the replay correctly. Exiting the level or loading will stop the writing process and truncate your replay file.")
#        _("Packet files (replays) handling. If you wish to save a reply of your game, or load a previously saved one, then use this. Otherwise, set it to 'None' to disable the option. Saved replay will be loadable as long as you won't change any of the game files.")
#        _("Accept changes."),
#        _("Abandon changes and close the window.")
tt_skipintro = _("Do not show intro movie on startup")
tt_nocd =      _("Loads music from the keeperfx/music folder. Place the music there.")


#tooltips settings
tt_language      = _("Here you can select your language translation. This will affect the in-game messages, but also speeches during the game.\nNote that some campaigns may not support your language; in this case default one will be used.")
tt_wible         = _("Wibble twists and turns the straight blocks making up the dungeon keeper world.\nTurn it off to get straight lines. Choose \"liquid only\" to still get waves in lava and water.")
tt_censor        =_("Enabling censorship will make only evil creatures to have blood, and will restrict death effect with exploding flesh.\nOriginally, this was enabled in german language version.")
tt_mouse_sen     =_("Increasing sensitivity will speed up the mouse in the game. Default value is 100, setting it to 0 will use your windows default instead.\nHigh values may make the mouse less accurate, so be careful!")
tt_fullscreen    =_("Select whether the game should run in full screen, or as a window. If you've chosen 'windowed', you may want to unlock your mouse cursor at the run options.")
tt_save_settings =_("Write changes to \"keeperfx.cfg\" file.")
tt_atmos         =_("Enabling Atmospheric sounds will have the game play random background sound effects, like drips of water and screams of horror, to set the mood.")
tt_atmos_vol     =_("Change the volume of the Atmospheric sounds effects.")
tt_lock_cursorpos   = _("Overwrite 'unlock cursor' mode in possession to lock the mouse cursor to the game window when possessing a creature.")
tt_freezelostfocus  = _("The game freezes when the window loses focus. Disable to keep playing in background.")
tt_pausemusic       = _("When the game is paused, pause the music too.")
tt_mutelostfocus    = _("When the window loses focus without freezing, still mute the game audio.")
tt_unlockcuronpause = _("When pausing, the game will release the mouse cursor to use on other windows.")
tt_resizemov        = _("Configures how the movies are displayed.")


def main():

    sg.theme('Dark Brown 5')
    sg.SetOptions(text_element_background_color='#723d01',
                  element_background_color='#723d01'
                  )

    button_font = ("Arial 15 bold")


    RunOpt_layout =  [sg.Column([[sg.CBox(_('Skip Intro'),   key='ro_SkipIntro',tooltip=tt_skipintro,enable_events=True)],
                                 [sg.CBox(_('Music From Cd'),key='ro_NoCd',     tooltip=tt_nocd,     enable_events=True)],
                                 [sg.CBox(_('Unlock mouse'), key='ro_altinp',                        enable_events=True)],
                                 [sg.CBox(_('Heavylog'),     key='ro_HvLog',    tooltip=tt_heavylog, enable_events=True)],
                                 [sg.CBox(_('No sound'),     key='ro_NoSnd',                         enable_events=True)],
                                 [sg.CBox(_('Cheats'),       key='ro_Alex',                          enable_events=True)]
                                ], background_color='#723d01'),
                      sg.Column([[sg.Push(),sg.Text(_('Computer Chat')),sg.Combo((compuchat_opts),default_value=_('Off'), size=10,key='ro_CompChat',enable_events=True)],
                                 [sg.Push(),sg.Text(_('Human Id')),     sg.Combo(human_ids,default_value=_('0 (Red)'), size=10,key='ro_HumanId',tooltip=tt_human_id,enable_events=True)],
                                 [sg.Push(),sg.Text(_('Game Speed')),sg.InputText('20', size=12,key='ro_GameSpeed',enable_events=True)],
                                 [sg.Frame(_('Packets'),[[sg.Combo((packet_opts),default_value=_('Off'), size=10,key='ro_CompChat',enable_events=True)],
                                                         [sg.Text(_('File')),sg.InputText('replay.pck', size=15,enable_events=True)]])]
                                ], background_color='#723d01'),
                      sg.Column([[sg.InputText('127.0.0.1', size=10,key='ro_mp_ip'),sg.InputText('5555', size=4,key='ro_mp_port'),sg.Button(_('Add'),key='ro_mp_Add')],
                                 [sg.Listbox(values=ip_address_list, size=(20, 5),key='ro_mp_List')],[sg.Push(),sg.Button(_('Remove'),key='ro_mp_Remove')]], background_color='#723d01')]


    tabBasicSettings_layout = [[sg.Column([
                                [sg.Push(),sg.Text(_('Language'),         tooltip=tt_language),   sg.Combo(languages,            tooltip=tt_language, size=12,key='setting_lang')],
                                [sg.Push(),sg.Text(_('Resolution')),                              sg.Combo(resolutions,                               size=12,key='setting_res')],
                                [sg.Push(),sg.CBox(_('Windowed'),         tooltip=tt_fullscreen                                                              ,key='setting_wind' )],
                                [sg.Push(),sg.Text(_('Wibble'),           tooltip=tt_wible),      sg.Combo(wibble_options,       tooltip=tt_wible,    size=12,key='setting_wibl' )],
                                [sg.Push(),sg.Text(_('Resize movies'),    tooltip=tt_resizemov),  sg.Combo(movie_resize_options, tooltip=tt_resizemov,size=12,key='setting_movr')],
                                [sg.Push(),sg.Text(_('Mouse sensitivity'),tooltip=tt_mouse_sen),  sg.InputText('100',            tooltip=tt_mouse_sen,size=12,key='setting_mousen')],
                                [sg.Push(),sg.CBox(_('Censorship'),       tooltip=tt_censor                                                                  ,key='setting_cens')],
                                
                              ], background_color='#723d01'),
                              sg.Column([[sg.Frame(_('Atmospheric Sound'),[[sg.Text(_('Frequency'),  tooltip=tt_atmos    ),sg.Combo(atmos_sound_options,tooltip=tt_atmos,key='setting_atmos')],
                                                      [sg.Text(_('Volume'   ),  tooltip=tt_atmos_vol),sg.Combo(atmos_sound_volumes,tooltip=tt_atmos_vol,key='setting_atmos_vol')]])],
                                                      
                                         [sg.CBox(_('Freeze game on lost focus'),     tooltip=tt_freezelostfocus ,key='setting_frzlstfoc')],
                                         [sg.CBox(_('Mute audio on lost focus'),       tooltip=tt_mutelostfocus   ,key='setting_mutelstfc')],
                                         [sg.CBox(_('Pause music on game pause'),     tooltip=tt_pausemusic      ,key='setting_pausmusic')],
                                         [sg.CBox(_('Unlock cursor on game pause'),   tooltip=tt_unlockcuronpause,key='setting_unlcrpaus')],
                                         [sg.CBox(_('Lock cursor in possession'),tooltip=tt_lock_cursorpos  ,key='setting_lckcurpos')],
                                        ], background_color='#723d01')],
                                [sg.Push(),sg.Button(_('Save'),tooltip=tt_save_settings)]
                                                      
                                                      ]





    runoption_content = sg.Column([[sg.Column([RunOpt_layout],size=(522, 265),pad=0, background_color='#723d01')],
                                                  [sg.InputText('keeperfx.exe -nointro -nocd -alex -sessions 127.0.0.1:5555',do_not_clear = True,key='runoption_text', size=72,pad=0)]],pad=0, key='runoption_content',visible=False)

    settings_content = sg.Column([[sg.TabGroup([[sg.Tab(_('Basic'), tabBasicSettings_layout)]], 
                                                  size=(522, 260),pad=0)],
                                                  ],pad=0, key='settings_content',visible=True)



    
    left = sg.Column([[sg.Column([],size=(27,109),pad=0,background_color='black'),
                      sg.Column([[sg.Button(_('Run Options'),image_data=runoptions_disabled_image,image_size=(149,47),pad=0,border_width=0,font=button_font,button_color=('#f6e1b5','black'))],
                                 [sg.Image(data=betweenTabs_image,        pad=0)],
                                 [sg.Button(_('Settings'),   image_data=settings_disabled_image,  image_size=(149,47),pad=0,border_width=0,font=button_font,button_color=('#f6e1b5','black'))]],pad=0)],
                     [sg.Image(data=left_middle_image,pad=0)],
                     [sg.Image(data=left_left_image,pad=0),
                     sg.Column([[sg.Button(_('Readme'),  image_data=buttonbg_image,pad=0,border_width=0,font=button_font,image_size=(107,47),button_color=('#f6e1b5','black'),key='ReadMeBtn' )],
                                [sg.Image(data=betweenshortbutton_image,pad=0)],
                                [sg.Button(_('Open Log'),image_data=buttonbg_image,pad=0,border_width=0,font=button_font,image_size=(107,47),button_color=('#f6e1b5','black'),key='openLogBtn')]],pad=0),
                     sg.Image(data=leftright_image,pad=0) ]
                     ],pad=0)


    top = [sg.Image(data=top_image,pad=0)]
    middle = [left,settings_content,runoption_content]

    bottom = [sg.Image(data=bottom_image,pad=0),sg.Text("defaultTextHere",key='errortext'),sg.Push(),sg.Button(_('Start'),image_data=buttonbg_image,pad=0,border_width=0,font=button_font,image_size=(80,40),button_color=('#f6e1b5','black'),key='StartBtn' )]
    layout = [top,middle,bottom]


    win = sg.Window(_('KeeperFx Launcher'), layout, finalize=True, keep_on_top=False, grab_anywhere=True, no_titlebar=False,margins=(0, 0),background_color='black', right_click_menu=[[''], ['Exit',]])


    if check_files(win):
        load_config(win)
        load_launch_options(win)

    while True:
        window, event, values = sg.read_all_windows()
        if event is None or event == 'Cancel' or event == 'Exit':
            break
        if event in (_('Run Options'), None):
            win.find_element('settings_content').update(visible=False)
            win.find_element('runoption_content').update(visible=True)
            win.find_element(_('Settings')).update(image_data=settings_disabled_image)
            win.find_element(_('Run Options')).update(image_data=buttonbg_image)
        if event in (_('Settings'), None):
            win.find_element('runoption_content').update(visible=False)
            win.find_element('settings_content').update(visible=True)
            win.find_element(_('Settings')).update(image_data=buttonbg_image)
            win.find_element(_('Run Options')).update(image_data=runoptions_disabled_image)
        if event in ('ro_mp_Add', None):
            ip_address_list.append(values['ro_mp_ip'] + ':' + values['ro_mp_port'])
            win.find_element('ro_mp_List').update(ip_address_list)
        if event in ('ro_mp_Remove', None):
            ip_address_list.remove(values['ro_mp_List'][0])
            win.find_element('ro_mp_List').update(ip_address_list)
        if event in ('ReadMeBtn', None):
            os.startfile("keeperfx_readme.txt")
        if event in ('openLogBtn', None):
            os.startfile("keeperfx.log")
        if event in ('openLogBtn', None):
            os.startfile("keeperfx.log")
        if event in ('StartBtn', None):
            os.startfile(calculateRunOptionText(values))

        win.find_element('runoption_text').update(calculateRunOptionText(values))

    win.close()


def calculateRunOptionText(values):
    if values["ro_HvLog"] == True:
        text = 'keeperfx_hvlog.exe'
    else:
        text = 'keeperfx.exe'

    if values['ro_SkipIntro']:
        text += ' -nointro'
    if values['ro_NoCd']:
        text += ' -nocd'
    if values['ro_altinp']:
        text += ' -altinput'
    if values['ro_NoSnd']:
        text += ' -nosound'
    if values['ro_Alex']:
        text += ' -alex'

    if values['ro_CompChat'] != 'Off':
        text += ' -compuchat ' + values['ro_CompChat']

 #   if ip_address_list.count > 0:
  #      text += ' -sessions  ' + ip_address_list

    return text

def check_files(win):
    if not exists("keeperfx.exe"):
        win.find_element('errortext').update(_('please place file in same folder\nas your keeperfx installation'))
    elif not exists("./data/bluepal.dat"):
        win.find_element('errortext').update(_('files from orininal missing,\npress install to copy them'))
        win.find_element('StartBtn').update('install')
    else:
        win.find_element('errortext').update('')
        win.find_element('StartBtn').update('run')
        return True
    
def load_config(win):
    parser = ConfigParser()
    with open("./keeperfx.cfg") as stream:
        parser.read_string("[top]\n" + stream.read())  # trick config parser to treat cfg as an ini
        config = parser['top']
        win.find_element('setting_lang').update(inv_dict_languages[config["LANGUAGE"]])
        win.find_element('setting_res').update(config["INGAME_RES"]) #TODO cut part off string
        win.find_element('setting_wind').update(config["INGAME_RES"].count("w") > 0)
        win.find_element('setting_wibl').update(inv_dict_wibble[config["WIBBLE"]])
        win.find_element('setting_movr').update(inv_dict_movie_resize_options[config["RESIZE_MOVIES"]])
        win.find_element('setting_mousen').update(config["POINTER_SENSITIVITY"])
        win.find_element('setting_cens').update(inv_dict_bool[config["CENSORSHIP"]])
        win.find_element('setting_lckcurpos').update(inv_dict_bool[config["LOCK_CURSOR_IN_POSSESSION"]])
        win.find_element('setting_frzlstfoc').update(inv_dict_bool[config["FREEZE_GAME_ON_FOCUS_LOST"]])
        win.find_element('setting_pausmusic').update(inv_dict_bool[config["PAUSE_MUSIC_WHEN_GAME_PAUSED"]])
        win.find_element('setting_mutelstfc').update(inv_dict_bool[config["MUTE_AUDIO_ON_FOCUS_LOST"]])
        win.find_element('setting_unlcrpaus').update(inv_dict_bool[config["UNLOCK_CURSOR_WHEN_GAME_PAUSED"]])

        if config["ATMOSPHERIC_SOUNDS"] == "OFF":
            win.find_element('setting_atmos').update(_('Off'))
        else:
            win.find_element('setting_atmos').update(inv_dict_atmos_sound_options[config["ATMOS_FREQUENCY"]])

        win.find_element('setting_atmos_vol').update(inv_dict_atmos_sound_volumes[config["ATMOS_VOLUME"]])
            
def load_launch_options(win):
    with open("./launch.sh") as stream:
        run_string =stream.read()
        win.find_element('ro_HvLog'    ).update(run_string.find("keeperfx_hvlog.exe") > 0)
        win.find_element('ro_SkipIntro').update(run_string.find("-nointro")           > 0)
        win.find_element('ro_NoCd'     ).update(run_string.find("-nocd")              > 0)
        win.find_element('ro_altinp'   ).update(run_string.find("-altinput")          > 0)
        win.find_element('ro_NoSnd'    ).update(run_string.find("-nosound")           > 0)
        win.find_element('ro_Alex'     ).update(run_string.find("-alex")              > 0)
        if "-packetsave" in run_string:
            win.find_element('ro_Alex')



if __name__ == '__main__':

#base64 encoded background images
    top_image = 'iVBORw0KGgoAAAANSUhEUgAAAtAAAACxCAMAAADavnp4AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA3FpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo3ZWIwMzZlMC01MTBiLTA0NDYtOGExZS1hODY0YzQzNzRkZjkiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6QjhGNjEyRDRDMkVEMTFFQzg2M0M4MDFGQUQwNzU5N0MiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6QjhGNjEyRDNDMkVEMTFFQzg2M0M4MDFGQUQwNzU5N0MiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjdlYjAzNmUwLTUxMGItMDQ0Ni04YTFlLWE4NjRjNDM3NGRmOSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDo3ZWIwMzZlMC01MTBiLTA0NDYtOGExZS1hODY0YzQzNzRkZjkiLz4gPC9y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'
    bottom_image = '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'
    runoptions_disabled_image = 'iVBORw0KGgoAAAANSUhEUgAAAJUAAAAvCAMAAADdLXhuAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABhQTFRFUzQLSysERCUBYUIZWzsSb08raUojZkYfIS+lDwAABPtJREFUeNqsWQmS4yAMVEcy/P/Hiw4w2GCTyVKTqqyDRSO1zqXPxoJ+iIRzzikdKWUWIiCe61cSEdY/5rJFV2aOR6JbxN8oG8uOQ5fu0B9xP5A+2wsmO/uJFMJgqChO9OUwyIDawSL1EiajoFIhzOIv/oTKQIhJdVVVsNIthVE0ytIgOVZ0V/MfG9LPr6gcAdup7ZqmpKJEVvuFiVPOBi8AUOhVd9pj1s1LUN+hqtzSj5/YFIZqMwmT+SIh1RihXUlRl5VDV07aH3X1QRiMzYzlX5VO+twQiNHFIMXP9qeaqoquLy/P+ZJXoRXzM5dsmFRBRu6snqXHJuZKeqCBN6o5cqEHWPSGARNQxObZBZiaMBTYHavkYqkeyeL4ONsP2e5jT/6qq6J0mmmraKWIz6EQ4w8F61twqi5n4Yzc6OEHnVOGyG9QQTSu0IT04YlGkdysqcxxk4YiaggLP6iGv3hfUfWI8hEVPAgfjGt8YEOluCKoh9jQSs6C5naGOltasBWoTpkkJZjINio56qIL2exsPdD9qcsboR2cO53eGsZymHzQFNjzj+yi4obqkBnpy4npcK/rEtCFJJ78IiRc1VQA8OQIeiLV0a3RijUeeOSRRl7TYs8Rdw3LepESRjndxdMWKjqGlehCLpgVzeGGyw8O5kWCw+fB1EaR1J+ALQvyI6yI9CQ3VJgUJ2bF6y8YQHXmeLLgBdWRaRFoq/tpSD1j1WXXPSLLRf6xg+oK6s75MbUCtcYKTncw4Dng8dJH2kEld1QHzQtV53+t64Qrqs8XluilP7E93d9LWBY5FooswpqnmdY+392Z31Fh9l4xIhbloNdx5LWXlVbCTKuyjmey253pKxVPudUCWAv6nL2y0fp+vjtNRfOOBeew0hIWzoqUTW+aq6eS8/G/Uc2NSNQ1E5qMFVf53BlfCou0ENwi4l9QpSmqqPC8svMKwYqWbbElIGInD6aXK43ZTjxSsRtQi6ksMzeUJSrZQUV5QUrManlvbmrWc5f8DlWiX3RF8+61VpxuOwfG9+yDJaq9PEic0o79VFfcSngvhNnjFU/GCKvblndqUqLnTpm1qEvDqzSvB7xnJUTZpYHB24pZXJ9GBq2qI0s9opLs3lTAtGCFZbCyTqX4PefWCspUWXMj5lY5vlTIxYQj4bMsipkWME1t0fDYnMRhYagvYJX1YD1tLTvXeem8zME9LuZ5VnObteTi8f1sBhedu5NWsaV24W6Y8tylqrbONg4r+kVFPjSm/oXnRaAXGTF889ES9V3KMyiJJs46mcVgADVUdSaIW0t/H+dy2ySN84qs65HUUd7GDOFeRA+YJs1LJYAVEPXVa8Osv6ZgFfV1685MBk9DHdOHosK9bD7Hk48THh/84SyzJxbEvVmYFrtRirvOqXdOdLM2LyPCKTFxlJgljdPEd135wAB3zHXEZqFzYV60CVxQCp8OXZvi4KKFr6dqt+zhYwZ6HooTVrb41KHb6QzYnvX5DRFfTutZbf7Qz6COGQQ4jx5AdDSpm2lJqCmoJtEeySqyDnSOIC90HmxzVMd3GdBEM/6L+cx7sDl9xny2d+oZHdleh8Zjf3zDRbuotFlc2KSlGqzyIG4XqXtxThTQBpF7mHw6aO4Kas1QI/epACcW7VuwchNVkiUa7Jubzj6/TrovwRBtWPESRF+4gq9IeP2fCHQu0TilqP4JMAB+6EMcDakIMQAAAABJRU5ErkJggg=='
    betweenTabs_image = 'iVBORw0KGgoAAAANSUhEUgAAAJcAAAALCAMAAABF5e9zAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpFQjI1OUQyQ0MzRDUxMUVDQjA4RURGMURDNUNENDQ3QSIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpFQjI1OUQyREMzRDUxMUVDQjA4RURGMURDNUNENDQ3QSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkVCMjU5RDJBQzNENTExRUNCMDhFREYxREM1Q0Q0NDdBIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkVCMjU5RDJCQzNENTExRUNCMDhFREYxREM1Q0Q0NDdBIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+49UK1AAAAGBQTFRFIiIUU1NKHR0RMjIkQUEzAAAASUk+EREJOjotKSkaGRkNJSUYW1tSLS0eFhYMDQ0FFRUKNjYoKSkdRkY5BAQCCQkFGhoQPT0wTU1ALi4hDQ0IHx8UCAgDEhILLCwbEBAH2hzY8QAAAldJREFUeNqUVGGT6iAMjGilhSuhNKCFIP//X17qeb2bp96bZvzAgGw3uxug+y5G5K5DVQzWikjrFusUEVvTDSMT6fY4IKIuwnLsgbsXRfRiDy7XeRqUhcEqH7E6j7p6JCaWC9G52lHHugzjsgwFnjFpw5U1oTct6kjESOhU802AvGAO8+F8Gl7yelk89Jf+stgwBVDem/FowQ6Dc8nk+/n20Vy5g/dA9MeRnJG9HH23o9gGgEKbmD+qEtV6d6zmdt+IGp7U56pKAbj3QKtrfK/mc5SeEHO8/4/VdL4A7SEG/Xk+2QLBKudrE2yOrbpaHVhllD2O0LyDISyyetaCc9bOx5V2MyYpUK4hGvAxmmLHW/GSODVdPz5m4D28zEmuTP08X6+X8TZKiG63QX6D9UKx1aqlzeyNUkn/4aNGUZA5Rv6OuvTHa/4lq3jr++B2ySV9ptGq5KRTH0lwY84CL3ziFq5N2+fb2JCzizJ930mS67Rd+oJo42L4/0H8xwovoXcdO5XyL0BGZYdQUquiVCrWQmkveLFzHL1455NRyXqHRiZHNcllzE4myKQwzYfrZHbKRXA6n+dpDNNpuo3H0Y7W6VU9l3NKRlJdlLgaIDmEd88PiYM669g4imASuLbaKAuRvtrpdDgfdbeTF4oYIYQk0uhaii/rALSqH8LLQPFjqt6+E7+l4Jed/wwj79DNBFs2/73Q+hKdsktWjKQOtas+v+cVG2r6QmjZy8Bsz05XRxmsw3zDB6kdvMx0PV8WCTAXEMeWsPQjiJFOkgVOVybtlVK5+xRgABi0RGHZCoycAAAAAElFTkSuQmCC'
    settings_disabled_image = 'iVBORw0KGgoAAAANSUhEUgAAAJUAAAAvCAMAAADdLXhuAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABhQTFRFVDQLSysEYkIaWzwSaEkiRCUBb08qRicBm05kqQAABO5JREFUeNqsWYGWpCAMaylj//+Pl7QFQRFHZ733bt0dhdCmaWDo8+JSEuJ6r0/eJJL9VSZmxuv4wVR/w2NfoehnVpaUktCb5TClnBOxqgKHGEZSzFBQlVt88i2qQ6DKyLHgZ4GqK8LciJMhKZee1k5v8reP9CL3JTw6R/z5BZWtkN+hKllD9mt0CpM6mrC+RlVykEsSXscKxGqEV+bpQM9RlWGzvAwVFiWS5S7U9I4Z65lZl6xMchdpegNKVgksWVl9DHG4JQA95sW23WRAVdfE2nK+gfU0ViQ/0cqqpavC/0FV4o8xl8Th5cdlXemOmA9RtcLmtcjyel1lCP5XVCaC/KBtzsoFTef/UKGhlujfDKnr7vjNGPSMqQjVOoE2K9/R/Yab9CaBfNcm+aZg3M5cp7yi0q9sCdY5D0RrtH3HLf1WLzqp9EvrnjIcSvv7pxDoRcc/x94mCsu1J1Aptz+PD2+o5BhGj5WC5rDi9oxW6cRUk+ui+DELLGbMJBuuAuxQMni+NYgZv+gZrVA+4zAqefOLTrziCouPsNLRDKFwz74dTnrZ6yP2x0hxCky5Lh1lv68jIPcY2IiAh/TTMx5mCxiGDB4c2Fl11ErQeBUfWq8+zMrS++f9iUy9jJZeKrap6eaxG7WtD11Ksk5FtFcGlYqJh4Yz9N6ygYh4NV9MMDO+qVALmEVon1NbBm0mVb6Rduq8VWXUaEsgHgdHULMsPRF6gSmoCFHDT9BW6dNLg+2H9qrQUY+sg7nUIPfpxBib0ZzOIeypcc+GMRW1e44NIIJim1aUChONVFJDd4GKIUvim1+NACRdbWKOrC9hjQpE2VCgiuy5YILeOlGGpb0VCmWQgSs99WjW4nRfRLRn6n1+1XD2HkOnxqHcymJvIy4cZth86xuTTCzdhXuqsAoei3gpVDte8JxZjvAL/tFB2120/BjAWcgd6xB638xF9Z1nR47PvBo4X0Yw4xG7eifSPpuRm55sniBYxhmniUyeEPO/cxJQlAe0o98HWdaJuAr5iVc3vsE9Q3A3Xdj6lK68k0W4NEBvEUF0rYcg7bjo1J11YSQ1zC2FJvAsltnb8RwWh255QCl4xUfWENGlU9AJKrgUjp5LM9QwA4U4IhfnB5FDy5lptro0440WqAmqmzMiKK/MSRXyCC0Ctaa4qKlWfy4kkQNyYMSPnIz1A+9reb7Ty7YzNonE6s+EyNEPaPSivG8iIU5PUCHu5fU51TVaCWgVqLzWRo6lkBRqp4Uabw+LfxIrG8Jo1Tca5yyyZmKVTY282C0ngyEz1YKr6YPI5jN0d/4P94N13LF9emlD1rMTy/ll4ORwMii91xrEuwsbPUkgsuGyILtRhLUdQOH/zUNm97jdPVmq5uFqe6bnPrg+LANFqDOWXPPktS2mZ+0yUIYL8sSjOPBwJHo058/P+nInCy42IQaY2wIWEYosOt7dNVsK+Rie31B5t0m+a7Nze64yKLahQvqqVcd20FOKNtRZoCz/fKq2RbdRP0wWKzMLRuQttVAZySrEutfSPO8MP6Hi5hbUvg0wd5Oty3jVidmdyJ7/paQ2Sf3+xjtD/uak6OrcWzXKlisfvYakfdvh26gcUCChLYM5wPmVYyvpqBKHk1vGSq9Rfer83GVQzMN7a/EjRUe3eeY2Z1fjWA6UVINdYIVPnn758ifAADSfd0yO3FlwAAAAAElFTkSuQmCC'
    left_middle_image = 'iVBORw0KGgoAAAANSUhEUgAAALIAAABICAMAAABlXV8lAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo1QkFDMjIxMUM0QjkxMUVDQTREM0UzREUzMTY1QzQ0MSIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo1QkFDMjIxMkM0QjkxMUVDQTREM0UzREUzMTY1QzQ0MSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjVCQUMyMjBGQzRCOTExRUNBNEQzRTNERTMxNjVDNDQxIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjVCQUMyMjEwQzRCOTExRUNBNEQzRTNERTMxNjVDNDQxIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+ZuPikgAAADBQTFRFREQ5JSUYAQEA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'
    left_left_image = 'iVBORw0KGgoAAAANSUhEUgAAABsAAABsCAMAAACsLTkeAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABhQTFRFMzMmJycaAAAAExMKREQ4VVVMCQkEHBwQ3SLBVQAAAfpJREFUeNqcVtF26zAIA5OK///jge2kSY1829uzs4dpFgjJptLKDxC/pJEPjGEwdRDMDI1hWY7Wg7sJadPiI1wC18CwTkn6hKso54xzhNN4LxoDo31i7wPBRjWqr/3nXKiGGAvXYOa+85Zx8j7Tob0GME6uD1kQjeeaeJuhLs/F34Zy6i3BTnUrhrwIRs4BY2TYeYvPXPf7MykLzGkvu7wkaXRa5SWioiqiRrXXvfSjBLMgFNUqE/CAJHopOaNYp0yhskI2bXqcg/ko56sPYYClPsX4z7WezVNPH8JWPY6j1BAKjtfrkEPEVk7LaqEuncdTQ7zEEqRaZb5zBms1syHBfYTpXi8viEVFn7Xv9ZAKXvEjWuTTep+908p3O4f54VHOxfUNyiMoGaM3WOT60iP1c9w+ZxahjXKibpW31jfD9G/NfLrb7+B7H+XARt67uzlSyGOYIy5pPMr73vo9uu+4fqz3GTlM0lt2R/4CzYTKcEJadTltyXW+GzPbPd7y+d528EghzvZ7wLLOZXScQ5D7qLs/gY1kqBRv/3mhNt8LbvXm+9emS0/fL8aJ2eaNrPVhamxseex2OHbfpfyH9/qtZvPOR1Tt5/3+Dwz4+txlX8WJ33vBrh6+3P0Xdl7TglXsBFfabZ+MMLFc2W74bvd/WW8+Q1XFPwEGAKQxHDUWc6m8AAAAAElFTkSuQmCC'
    betweenshortbutton_image = 'iVBORw0KGgoAAAANSUhEUgAAAG0AAAAKCAMAAACJ1yCGAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAABhQTFRFUFBGNDQnQ0M3JSUXAgIBamppEhIJXV1WwWoJJAAAAWdJREFUeNqEU1uSwzAI4xHD/W+8SICb7n4sbZoZQxGSsES4q6l6PM9TT+Ag6vV8RR1WHaLegU+f2znpLFA1M5H6IlKZ9nOO3g4q6A849z7DYSAqzVcfa/fIrH6IHi88z7EuAVpV4OfkSdthahpWVl4EZHSofZhwlnijGbGyEcECIwe6SQw3RhM084smRGNKRiGfrsSJF87igzO+UJLR5/JRstpUtpUs8qtkxrUiBD7RDCbZE7Z4o8W1rT2j5B2xw48FSLbYCfmM+VJ6hmEHadimEsPr6c/z2ZW4/q9xwna63SA8ZRxEGW45ShNLZKj9WsE/0atbAmFB9HIL2S0JOoIf4zgzgxwbJdFB6kHOlxq3P97rskJgq7SNC98aPdMOYxi1lOJb5OILLXiFZA2ka+9YVbt0rpHMDtSjcwN2dufSZUfl266cabxFbpTnPyGd+wh2NlfcxxdZNOIp9x8lc/vzKll/+RFgAJpJDye/4eyXAAAAAElFTkSuQmCC'
    leftright_image = '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'
    buttonbg_image = 'iVBORw0KGgoAAAANSUhEUgAAAG0AAAAxCAMAAADnatfoAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRFcj0BAAAAAoAOVwAAAB5JREFUeNrswQEBAAAAgiD/r25IQAEAAAAAPJgAAwAVDgAB/uNZYgAAAABJRU5ErkJggg=='   
    main()

