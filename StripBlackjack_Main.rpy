
init python:
    DEBUG_MODE = True

    if DEBUG_MODE == True:
        mods["DEBUG_MAIN"] = u"Карты на раздевание (Отладочный режим)"
    
    if DEBUG_MODE == False:
        mods["StripBlackjack_Intro"] = u"Карты на раздевание (18+)"


label StripBlackjack_Intro:
    pause