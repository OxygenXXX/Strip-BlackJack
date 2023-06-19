
label StripBlackjack_Debug:
    call StripBlackjack_SpritesTest

label StripBlackjack_SpritesTest:
    
    # Передача упраления блоку с визуальной отладкой спрайтов
    # Тестируемый масштаб спрайтов: close

    call StripBlackjack_SpritesTest.SpritesClose

    # Передача упраления блоку с визуальной отладкой спрайтов
    # Тестируемый масштаб спрайтов: normal

    call StripBlackjack_SpritesTest.SpritesNormal

    # Передача упраления блоку с визуальной отладкой спрайтов
    # Тестируемый масштаб спрайтов: far

    call StripBlackjack_SpritesTest.SpritesFar

    return

# Этот блок позволяет провести визуальную отладку
# Спрайтов всех персонажей, использующихся в моде

# Тестируемый масштаб спрайтов: close

label .SpritesClose:

    # Визуальная отладка спрайтов Алисы Двачевской
    # Масштаб спрайтов: close

    show dv body first close
    dv "Спрайт: dv body first close"

    show dv body second close
    dv "Спрайт: dv body second close"

    show dv body third close
    dv "Спрайт: dv body third close"

    show dv body fourth close
    dv "Спрайт: dv body fourth close"

    show dv body fifth close
    dv "Спрайт: dv body fifth close"

    hide dv

    # Визуальная отладка спрайтов Хатсуне Мику
    # Масштаб спрайтов: close

    show mi body first close
    dv "Спрайт: mi body first close"

    show mi body second close
    dv "Спрайт: mi body second close"

    show mi body third close
    dv "Спрайт: mi body third close"

    hide mi

    # Визуальная отладка спрайтов Славяны Ясеневой
    # Масштаб спрайтов: close
    
    show sl body first close
    dv "Спрайт: sl body first close"

    show sl body second close
    dv "Спрайт: sl body second close"

    show sl body third close
    dv "Спрайт: sl body third close"

    show sl body fourth close
    dv "Спрайт: sl body fourth close"

    hide sl 

    # Визуальная отладка спрайтов Лены Тихоновой
    # Масштаб спрайтов: close

    show un body first close
    dv "Спрайт: un body first close"

    show un body second close
    dv "Спрайт: un body second close"

    show un body third close
    dv "Спрайт: un body third close"

    hide un

    # Визуальная отладка спрайтов Ульяны Лениной
    # Масштаб спрайтов: close

    show us body first close
    dv "Спрайт: us body first close"

    show us body second close
    dv "Спрайт: us body second close"

    show us body third close
    dv "Спрайт: us body third close"

    hide us

    return

# Этот блок позволяет провести визуальную отладку
# Спрайтов всех персонажей, использующихся в моде

# Тестируемый масштаб спрайтов: normal

label .SpritesNormal:
    
    # Визуальная отладка спрайтов Алисы Двачевской
    # Масштаб спрайтов: normal

    show dv body first normal
    dv "Спрайт: dv body first normal"

    show dv body second normal
    dv "Спрайт: dv body second normal"

    show dv body third normal
    dv "Спрайт: dv body third normal"

    show dv body fourth normal
    dv "Спрайт: dv body fourth normal"

    show dv body fifth normal
    dv "Спрайт: dv body fifth normal"

    hide dv

    # Визуальная отладка спрайтов Хатсуне Мику
    # Масштаб спрайтов: normal

    show mi body first normal
    dv "Спрайт: mi body first normal"

    show mi body second normal
    dv "Спрайт: mi body second normal"

    show mi body third normal
    dv "Спрайт: mi body third normal"

    hide mi

    # Визуальная отладка спрайтов Славяны Ясеневой
    # Масштаб спрайтов: normal
    
    show sl body first normal
    dv "Спрайт: sl body first normal"

    show sl body second normal
    dv "Спрайт: sl body second normal"

    show sl body third normal
    dv "Спрайт: sl body third normal"

    show sl body fourth normal
    dv "Спрайт: sl body fourth normal"

    hide sl

    # Визуальная отладка спрайтов Лены Тихоновой
    # Масштаб спрайтов: normal

    show un body first normal
    dv "Спрайт: un body first normal"

    show un body second normal
    dv "Спрайт: un body second normal"

    show un body third normal
    dv "Спрайт: un body third normal"

    hide un

    # Визуальная отладка спрайтов Ульяны Лениной
    # Масштаб спрайтов: normal

    show us body first normal
    dv "Спрайт: us body first normal"

    show us body second normal
    dv "Спрайт: us body second normal"

    show us body third normal
    dv "Спрайт: us body third normal"

    hide us

    return

# Этот блок позволяет провести визуальную отладку
# Спрайтов всех персонажей, использующихся в моде

# Тестируемый масштаб спрайтов: far

label .SpritesFar:
    
    # Визуальная отладка спрайтов Алисы Двачевской
    # Масштаб спрайтов: far

    show dv body first far
    dv "Спрайт: dv body first far"

    show dv body second far
    dv "Спрайт: dv body second far"

    show dv body third far
    dv "Спрайт: dv body third far"

    show dv body fourth far
    dv "Спрайт: dv body fourth far"

    show dv body fifth far
    dv "Спрайт: dv body fifth far"

    hide dv

    # Визуальная отладка спрайтов Хатсуне Мику
    # Масштаб спрайтов: far

    show mi body first far
    dv "Спрайт: mi body first far"

    show mi body second far
    dv "Спрайт: mi body second far"

    show mi body third far
    dv "Спрайт: mi body third far"

    hide mi

    # Визуальная отладка спрайтов Славяны Ясеневой
    # Масштаб спрайтов: far
    
    show sl body first far
    dv "Спрайт: sl body first far"

    show sl body second far
    dv "Спрайт: sl body second far"

    show sl body third far
    dv "Спрайт: sl body third far"

    show sl body fourth far
    dv "Спрайт: sl body fourth far"


    show sl bra first far
    dv "Спрайт: sl body first far"

    show sl bra second far
    dv "Спрайт: sl body second far"

    show sl bra third far
    dv "Спрайт: sl body third far"

    show sl bra fourth far
    dv "Спрайт: sl body fourth far"


    show sl panties first far
    dv "Спрайт: sl body first far"

    show sl panties second far
    dv "Спрайт: sl body second far"

    show sl panties third far
    dv "Спрайт: sl body third far"

    show sl panties fourth far
    dv "Спрайт: sl body fourth far"


    show sl swim first far
    dv "Спрайт: sl body first far"

    show sl swim second far
    dv "Спрайт: sl body second far"

    show sl swim third far
    dv "Спрайт: sl body third far"

    show sl swim fourth far
    dv "Спрайт: sl body fourth far"

    hide sl

    # Визуальная отладка спрайтов Лены Тихоновой
    # Масштаб спрайтов: far

    show un body first far
    dv "Спрайт: un body first far"

    show un body second far
    dv "Спрайт: un body second far"

    show un body third far
    dv "Спрайт: un body third far"

    hide un

    # Визуальная отладка спрайтов Ульяны Лениной
    # Масштаб спрайтов: far

    show us body first far
    dv "Спрайт: us body first far"

    show us body second far
    dv "Спрайт: us body second far"

    show us body third far
    dv "Спрайт: us body third far"

    hide us

    return