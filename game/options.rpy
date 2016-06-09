## Этот файл содержит некоторые опции которые можно изменить для настройки
## вашей игры на Ren'Py. Он содержит только самые часто используемые настройки...
## Их на самом деле гораздо больше.
##
## Строки, начинающиеся с двух знаков '#' являются комментариями, и вы
## не должны их раскомментировать. Строки, начинающиеся с одного
## знака '#' являются закоментированным кодом, и вы можете их
## раскомментировать в подходящих вам ситуациях.

init -1 python hide:

    ## Включать ли нам инструменты разработчика? Здесь нужно
    ## поставить False перед выпуском игры, чтобы
    ## пользователь не смог мошенничать, используя эти инструменты.

    config.developer = True

    ## Эти управляют шириной и высотой экрана.

    config.screen_width = 1024
    config.screen_height = 768

    ## Это управляет заголовком окна, когда Ren'Py
    ## запущен в оконном режиме.

    config.window_title = u"The story about Miku and Eugene(maybe)"

    # Эти управляют именем и версией игры, которые указываются
    # в журналах отладки.
    config.name = "The story about Miku and Eugene"
    config.version = "0.1"
    config.log = "config.log"


    config.window_icon = "images/misc/icon_large.png"
    config.windows_icon = "images/misc/icon.png"

    #########################################
    # Темы

    ## Затем, мы захотим вызвать функцию темы. theme.roundrect
    ## это тема, поддерживающая круглые прямоугольники.
    ##
    ## Функция темы берет несколько параметров, которые
    ## настраивают цветовую схему.

    theme.marker(
        ## Theme: Marker
        ## Color scheme: First Valentines

        ## The color of an idle widget face.
        widget = "#eccb7e",

        ## The color of a focused widget face.
        widget_hover = "#5c3a00",

        ## The color of the text in a widget.
        widget_text = "#3d0000",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#ce5a02",

        ## The color of a disabled widget face.
        disabled = "#5c3a00",

        ## The color of disabled widget text.
        disabled_text = "#BFA1A1",

        ## The color of informational labels.
        label = "#5D1010",

        ## The color of a frame containing widgets.
        frame = "#F8F2D0",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "images/bg/mmbg.png",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "#D98989",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )


    #########################################
    ## Эти настройки позволяют вам настроить окно,
    ## содержащее диалоги и текст "от автора", замещая его
    ## изображением.

    ## Фон окна. В Frame, числа символизируют размер
    ## левого/правого и верхнего/нижнего бордюров
    ## соответственно.

    # style.window.background = Frame("frame.png", 12, 12)

    ## Внешние поля - пространство, окружающее окно, на котором
    ## не рисуется фон.

    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## Внутренние поля - пространство внутри окна, где
    ## рисуется фон.

    # style.window.left_padding = 6
    # style.window.right_padding = 6
    # style.window.top_padding = 6
    # style.window.bottom_padding = 6

    ## Это минимальная высота окна, включая поля.

    # style.window.yminimum = 250


    #########################################
    ## Это позволит вам изменить расположение главного меню.

    ## Это работает так: мы находим точку-якорь внутри
    ## объекта и точку позиции (pos) на экране.
    ## Затем, мы размещаем объект так, чтобы эти точки совпадали.

    ## Якорь/pos можно задавать как целое или действительное число.
    ## Если целое, оно принимается как кол-во пикселей от
    ## левого верхнего угла. Если действительное, число
    ## принимается как доля размера объекта или экрана.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## Это позволяет настроить шрифт текста в Ren'Py.

    ## Файл, содержащий шрифт.

    # style.default.font = "DejaVuSans.ttf"

    ## Размер текста по умолчанию.

    # style.default.size = 22

    ## Заметьте, что это изменит стиль лишь некоторого
    ## текста. У других кнопок свои стили.


    #########################################
    ## Эти настройки позволят изменить некоторые звуки
    ## Ren'Py.

    ## Установите False если в игре нет звуковых эффектов.

    config.has_sound = True

    ## Установите False если в игре нет музыки.

    config.has_music = True

    ## Установите True если в игре есть озвучка.

    config.has_voice = False

    config.gl_resize = True

    config.mouse = { }
    config.mouse["default"] = [
        ("images/misc/mouse1.png",  0, 0)

        ]

    ## Звуки при нажатии на кнопки и imagemap-ы.

    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Звуки при входе и выходе из игрового меню.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## Звук для проверки громкости.

    # config.sample_sound = "click.wav"

    ## Музыка, играющая в главном меню.

    # config.main_menu_music = "main_menu_theme.ogg"


    #########################################
    ## Справка.

    ## Это позволит настроить опцию справки в меню Ren'Py.
    ## Это могут быть:
    ## - Метка в сценарии. В этом случае эта метка вызывается
    ##   для показа помощи.
    ## - Имя файла отнсоительно основной директории.
    ##   Он будет открыт в веб-браузере.
    ## None. Помощь будет выключена.
    config.help = None


    #########################################
    ## Переходы.

    ## Используется при входе в игровое меню.
    config.enter_transition = None

    ## Используется при выходе из игрвого меню.
    config.exit_transition = None

    ## Используется между экранами игрового меню.
    config.intra_transition = None

    ## Используется при входе в игровое меню из главного.
    config.main_game_transition = None

    ## Используется при возвращении в главное меню из игры.
    config.game_main_transition = None

    ## Используется при переходе в главное меню из окна загрузки.
    config.end_splash_transition = None

    ## Используется при переходе в главное меню после окончания игры.
    config.end_game_transition = None

    ## Используется при загрузке игры.
    config.after_load_transition = None

    ## Используется при отображении окна.
    config.window_show_transition = None

    ## Используется при скрытии окна.
    config.window_hide_transition = None

    ## Используется при переходе в режим NVL сразу после режима ADV.
    config.adv_nvl_transition = dissolve

    ## Используется при переходе в режим ADV сразу после режима NVL.
    config.nvl_adv_transition = dissolve

    ## Используется при отображении yesno.
    config.enter_yesno_transition = None

    ## Используется при скрытии yesno.
    config.exit_yesno_transition = None

    ## Используется при входе в реплей.
    config.enter_replay_transition = None

    ## Используется при выходе из реплея.
    config.exit_replay_transition = None

    ## Используется при изменении изображения с помощью "say" с изобразительными атрибутами.
    config.say_attribute_transition = None

    #########################################
    ## Имя директории, где хранятся данные игры.
    ## (это необходимо задать рано, чтобы постоянная информация могла быть
    ## найдена на стадии инициализации.)
python early:
    config.save_directory = "ThestoryaboutMikuandEugene-1464906320"

init -1 python hide:
    #########################################
    ## Стандартные значения настроек.

    ## Эти опции используются лишь при первом запуске игры.
    ## Чтобы применить их снова, удалите game/saves/persistent.

    ## Запустить в полноэкранном режиме?

    config.default_fullscreen = False

    ## Скорость текста по умолчанию, в знаках в секунду. 0 - бесконечность.

    config.default_text_cps = 50

    config.has_autosave = True

    ## Время авто-режима по умолчанию.

    config.default_afm_time = 10

    config.main_menu_music = "sounds/music/TheChemicalBrosDoitagain.ogg"

    config.rollback_length = 128
    config.hard_rollback_limit = 100

    #########################################
    ## Остальные настройки могут быть ниже.


init python:
    build.directory_name = "thestoryaboutmikuandeugene-0.1"
    build.executable_name = "The story about Miku and Eugene"
    build.include_update = False
    build.classify('**debug.rpy**', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.rpy', None)
    build.classify('**.bat', None)
    build.classify('**.txt', None)
    build.classify('**.bak', None)
    build.classify('**.rpy#', None)
    build.classify('**.log', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.mp3', 'archive')