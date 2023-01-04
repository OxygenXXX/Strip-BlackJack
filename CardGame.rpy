screen CardGameChoose:
    if btnn < 7 and ipoint < 22:
        textbutton "{font=21/font/21font.ttf}{size=40}Ещё карту" xalign .07 yalign .12 xysize (150, 70) action [SetVariable("karta"+str(btnn),renpy.random.randint(2,11)),SetVariable("kartam"+str(btnn),renpy.random.choice([100,200,300,400])),SetVariable("btnn",btnn+1),Jump("CardGameCheck")]
    textbutton "{font=21/font/21font.ttf}{size=40}Хватит" xalign .20 yalign .12 xysize (150, 70) action Jump("cstand")
    if ScoreOn == False:
        textbutton "{font=21/font/21font.ttf}{size=40}Вкл счётчик" xalign .32 yalign .12 xysize (160, 70) action [SetVariable("ScoreOn", True)]
    if ScoreOn == True:
        textbutton "{font=21/font/21font.ttf}{size=40}Выкл счётчик" xalign .31 yalign .12 xysize (170, 70) action [SetVariable("ScoreOn", False)]
    #vbox:
    #    spacing 10
    #    xalign .502 yalign .4905
    #    xysize (1000, 200)
    #    text "[RandCheck]"
    if ScoreOn == True:
        vbox:
            spacing 10
            xalign .06 yalign .9
            xysize (667,33)
            text "{font=21/font/21font.ttf}{size=65}[karta1] + [karta2] + [karta3] + [karta4] + [karta5] + [karta6]"
        
screen CardGameChoose2:
    textbutton "{font=21/font/21font.ttf}{size=40}В меню" xalign .46 yalign .12 xysize (150, 70) action Jump("CardGame_menu")
screen CardGameFinal:
    if step <= 0:
        vbox:
            spacing 10
            xalign .3502 yalign .4905
            xysize (1000, 200)
            text "{font=21/font/21font.ttf}{size=91}{color=000000}Нельзя отчаиваться!"
        vbox:
            spacing 10
            xalign .35 yalign .49
            xysize (1000, 200)
            text "{font=21/font/21font.ttf}{size=90}Нельзя отчаиваться!"
        textbutton "{font=21/font/21font.ttf}{size=45}Ещё раз" xalign .23 yalign .525 xysize (150, 70) action [SetVariable("step",1), Jump("CardGame2")]
        textbutton "{font=21/font/21font.ttf}{size=45}В меню" xalign .33 yalign .525 xysize (150, 70) action Jump("CardGame_menu")
    elif step >= 8 and girl == "sl_CG":
        vbox:
            spacing 10
            xalign .502 yalign .4905
            xysize (1000, 200)
            text "{font=21/font/21font.ttf}{size=91}{color=000000}Победа!"
        vbox:
            spacing 10
            xalign .5 yalign .49
            xysize (1000, 200)
            text "{font=21/font/21font.ttf}{size=90}Победа!"
        textbutton "{font=21/font/21font.ttf}{size=45}В меню" xalign .26 yalign .525 xysize (150, 70) action Jump("CardGame_menu")
    elif step >= 6 and girl != "sl_CG":
        vbox:
            spacing 10
            xalign .502 yalign .4905
            xysize (1000, 200)
            text "{font=21/font/21font.ttf}{size=91}{color=000000}Победа!"
        vbox:
            spacing 10
            xalign .5 yalign .49
            xysize (1000, 200)
            text "{font=21/font/21font.ttf}{size=90}Победа!"
        textbutton "{font=21/font/21font.ttf}{size=45}В меню" xalign .26 yalign .525 xysize (150, 70) action Jump("CardGame_menu")
screen CardGameCards:
    hbox xalign .03 yalign .5:
        add "21/cards/"+str(karta1+kartam1)+".png"
        add "21/cards/"+str(karta2+kartam2)+".png"
        add "21/cards/"+str(karta3+kartam3)+".png"
        add "21/cards/"+str(karta4+kartam4)+".png"
        add "21/cards/"+str(karta5+kartam5)+".png"
        add "21/cards/"+str(karta6+kartam6)+".png"
    
label CardGame3:
    stop music fadeout 2
    $ renpy.pause (1, hard=True)
    scene greenbg with dissolve
    show tablebg with dissolve
    if girl == "dv_CG":
        play music music_list['heather'] fadein 2
    elif girl == "un_CG":
        play music music_list['lightness'] fadein 2
    elif girl == "mi_CG":
        play music music_list['memories'] fadein 2
    elif girl == "mt_CG":
        play music music_list['eternal_longing'] fadein 2
    elif girl == "sl_CG":
        play music music_list['dance_of_fireflies'] fadein 2
    elif girl == "us_CG":
        play music music_list['went_fishing_caught_a_girl'] fadein 2
    jump CardGame2
label CardGame2:
    $ RandCheck = renpy.random.randint(15,18)
    $ nullgirl = girl
    if step <= 0:
        hide screen CardGameChoose
        hide screen CardGameChoose2
        hide screen CardGameCards
        show screen CardGameFinal
    elif step >= 8 and girl == "sl_CG":
        hide screen CardGameChoose
        hide screen CardGameChoose2
        hide screen CardGameCards
        show screen CardGameFinal
    elif step >= 6 and girl != "sl_CG":
        hide screen CardGameChoose
        hide screen CardGameChoose2
        hide screen CardGameCards
        show screen CardGameFinal
    $ nullgirl = girl+str(step)
    show expression nullgirl with dissolve:
        xcenter 0.78 ycenter 0.45
    hide tablebg
    show tablebg
    jump CardGame
label CardGame:
    $ btnn=2
    $ kart1=renpy.random.randint(2,11)
    $ kartm1=renpy.random.choice([100,200,300,400])
    $ karta1=renpy.random.randint(2,11)
    $ kartam1=renpy.random.choice([100,200,300,400])
    $ kart2=0
    $ kart3=0
    $ kart4=0
    $ kart5=0
    $ kart6=0
    $ kartm2=0
    $ kartm3=0
    $ kartm4=0
    $ kartm5=0
    $ kartm6=0
    $ karta2=0
    $ karta3=0
    $ karta4=0
    $ karta5=0
    $ karta6=0
    $ kartam2=0
    $ kartam3=0
    $ kartam4=0
    $ kartam5=0
    $ kartam6=0
    $ cpupoint=kart1
    $ ipoint=karta1
    $ StopLoop = False
label CardGameTable:
    if step < 8 and step > 0 and girl == "sl_CG":
        show screen CardGameCards
        show screen CardGameChoose
        show screen CardGameChoose2
    elif step < 6 and step > 0 and girl != "sl_CG":
        show screen CardGameCards
        show screen CardGameChoose
        show screen CardGameChoose2
    $ renpy.pause(hard=True)
label CardGameCheck:
    $ ipoint=karta1+karta2+karta3+karta4+karta5+karta6
    if ipoint>21:
        if karta1==11:
            $ karta1=1
        elif karta2==11:
            $ karta2=1
        elif karta3==11:
            $ karta3=1
        elif karta4==11:
            $ karta4=1
        elif karta5==11:
            $ karta5=1
        elif karta6==11:
            $ karta6=1
        $ ipoint=karta1+karta2+karta3+karta4+karta5+karta6
    jump CardGameTable
label cstand:
    hide screen CardGameChoose
    hide screen CardGameChoose2
    $ cpupoint=kart1+kart2+kart3+kart4+kart5+kart6
    $ ipoint=karta1+karta2+karta3+karta4+karta5+karta6
    if StopLoop == False and cpupoint >= 18:
        if btnn==4:
            $ kart3=0
            $ kartm3=0
        if btnn==5:
            $ kart4=0
            $ kartm4=0
        if btnn==6:
            $ kart5=0
            $ kartm5=0
        if btnn==7:
            $ kart6=0
            $ kartm6=0
        $ StopLoop = True
        jump cstand
    if StopLoop == False and cpupoint > 21:
        if kart1==11:
            $ kart1=1
        elif kart2==11:
            $ kart2=1
        elif kart3==11:
            $ kart3=1
        elif kart4==11:
            $ kart4=1
        elif kart5==11:
            $ kart5=1
        elif kart6==11:
            $ kart6=1
        $ StopLoop = True
        jump cstand
    if cpupoint < RandCheck:
        if kart2==0:
            $ kart2=renpy.random.randint(2,11)
            $ kartm2=renpy.random.choice([100,200,300,400])
            jump cstand
        elif kart3==0:
            $ kart3=renpy.random.randint(2,11)
            $ kartm3=renpy.random.choice([100,200,300,400])
            jump cstand
        elif kart4==0:
            $ kart4=renpy.random.randint(2,11)
            $ kartm4=renpy.random.choice([100,200,300,400])
            jump cstand
        elif kart5==0:
            $ kart5=renpy.random.randint(2,11)
            $ kartm5=renpy.random.choice([100,200,300,400])
            jump cstand
        elif kart6==0:
            $ kart6=renpy.random.randint(2,11)
            $ kartm6=renpy.random.choice([100,200,300,400])
            jump cstand
    elif ipoint > 21:
        if cpupoint > 21:
            $ renpy.pause(2, hard=True)
            "Мы оба перебрали - ничья."
        else:
            $ renpy.pause(2, hard=True)
            "У неё - [cpupoint]. А у меня перебор."
            $ step = step - 1
            jump CardGame2
    elif cpupoint > 21:
        $ renpy.pause(2, hard=True)
        "У неё перебор, я победил."
        $ step = step + 1
        jump CardGame2
    elif ipoint > cpupoint:
        $ renpy.pause(2, hard=True)
        "Со счётом [ipoint]:[cpupoint] победил я!"
        $ step = step + 1
        jump CardGame2
    elif ipoint == cpupoint:
        $ renpy.pause(2, hard=True)
        "Равный счёт - ничья."
    else:
        $ renpy.pause(2, hard=True)
        "У неё - [cpupoint], а у меня - [ipoint]. Я проиграл."
        $ step = step - 1
        jump CardGame2
    jump CardGame
