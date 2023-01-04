init:

    image disclaimerSM = "21/bg/disclaimerSM.png"
    image first_preview = "21/bg/first_preview.png"
    image greenbg = "21/bg/greenbg.png"
    image menu_bg_SM = "21/bg/menu_bg_SM.jpg"
    image tablebg = "21/bg/tablebg.png"
    ########
    image dv_CG0 = "21/sp/dv_CG0.png"
    image dv_CG1 = "21/sp/dv_CG1.png"
    image dv_CG2 = "21/sp/dv_CG2.png"
    image dv_CG3 = "21/sp/dv_CG3.png"
    image dv_CG4 = "21/sp/dv_CG4.png"
    image dv_CG5 = "21/sp/dv_CG5.png"
    image dv_CG6 = "21/sp/dv_CG6.png"
    image mi_CG0 = "21/sp/mi_CG0.png"
    image mi_CG1 = "21/sp/mi_CG1.png"
    image mi_CG2 = "21/sp/mi_CG2.png"
    image mi_CG3 = "21/sp/mi_CG3.png"
    image mi_CG4 = "21/sp/mi_CG4.png"
    image mi_CG5 = "21/sp/mi_CG5.png"
    image mi_CG6 = "21/sp/mi_CG6.png"
    image mt_CG0 = "21/sp/mt_CG0.png"
    image mt_CG1 = "21/sp/mt_CG1.png"
    image mt_CG2 = "21/sp/mt_CG2.png"
    image mt_CG3 = "21/sp/mt_CG3.png"
    image mt_CG4 = "21/sp/mt_CG4.png"
    image mt_CG5 = "21/sp/mt_CG5.png"
    image mt_CG6 = "21/sp/mt_CG6.png"
    image sl_CG0 = "21/sp/sl_CG0.png"
    image sl_CG1 = "21/sp/sl_CG1.png"
    image sl_CG2 = "21/sp/sl_CG2.png"
    image sl_CG3 = "21/sp/sl_CG3.png"
    image sl_CG4 = "21/sp/sl_CG4.png"
    image sl_CG5 = "21/sp/sl_CG5.png"
    image sl_CG6 = "21/sp/sl_CG6.png"
    image sl_CG7 = "21/sp/sl_CG7.png"
    image sl_CG8 = "21/sp/sl_CG8.png"
    image un_CG0 = "21/sp/un_CG0.png"
    image un_CG1 = "21/sp/un_CG1.png"
    image un_CG2 = "21/sp/un_CG2.png"
    image un_CG3 = "21/sp/un_CG3.png"
    image un_CG4 = "21/sp/un_CG4.png"
    image un_CG5 = "21/sp/un_CG5.png"
    image un_CG6 = "21/sp/un_CG6.png"
    image us_CG0 = "21/sp/us_CG0.png"
    image us_CG1 = "21/sp/us_CG1.png"
    image us_CG2 = "21/sp/us_CG2.png"
    image us_CG3 = "21/sp/us_CG3.png"
    image us_CG4 = "21/sp/us_CG4.png"
    image us_CG5 = "21/sp/us_CG5.png"
    image us_CG6 = "21/sp/us_CG6.png"

    $ mods["CardGameIntro"] = u"Карты на раздевание"
    
    $ persona5_2_menu = "21/music/persona5_2_menu.ogg"
    image leaf_small_sm = "21/GUI/leaf_small.png"
    image leaf_medium_sm = "21/GUI/leaf_medium.png"
    image leaf_large_sm = "21/GUI/leaf_large.png"
    image leaffall_small_sm:
        truecenter
        xzoom 1.3 yzoom 1.7
        contains:
            SnowBlossom("leaf_large_sm", count=15, border=100, xspeed=(30, 70), yspeed=(50, 400), start=0.5)
        contains:
            SnowBlossom("leaf_medium_sm", count=30, border=100, xspeed=(15, 20), yspeed=(75, 300), start=0.3)
        contains:
            SnowBlossom("leaf_small_sm", count=40, border=100, xspeed=(50, 60), yspeed=(100, 250), start=0)
         
    image leaffall_small_l_sm:
        "leaffall_small_sm"
        rotate 30.0
   
    screen CardGame_menu:
        imagebutton auto "21/GUI/TradMoonButton_%s.png" xalign .01 yalign .99 clicked OpenURL("https://vk.com/tradmoon")
        imagebutton auto "21/GUI/Exit_CG_%s.png" xalign .99 yalign .99 action Return()
        imagebutton auto "21/GUI/dv_gui_%s.png" xalign .15 yalign .18 action [SetVariable("girl","dv_CG"), SetVariable("step",step+1), Jump("CardGame3")]
        imagebutton auto "21/GUI/un_gui_%s.png" xalign .50 yalign .18 action [SetVariable("girl","un_CG"), SetVariable("step",step+1), Jump("CardGame3")]
        imagebutton auto "21/GUI/mi_gui_%s.png" xalign .85 yalign .18 action [SetVariable("girl","mi_CG"), SetVariable("step",step+1), Jump("CardGame3")]
        imagebutton auto "21/GUI/mt_gui_%s.png" xalign .15 yalign .82 action [SetVariable("girl","mt_CG"), SetVariable("step",step+1), Jump("CardGame3")]
        imagebutton auto "21/GUI/sl_gui_%s.png" xalign .50 yalign .82 action [SetVariable("girl","sl_CG"), SetVariable("step",step+1), Jump("CardGame3")]
        imagebutton auto "21/GUI/us_gui_%s.png" xalign .85 yalign .82 action [SetVariable("girl","us_CG"), SetVariable("step",step+1), Jump("CardGame3")]
    
label CardGameIntro:
    $ ScoreOn = False
    scene disclaimerSM with dissolve
    $ renpy.pause(1, hard=True)
    pause
    scene black with dissolve
    $ renpy.pause(1, hard=True)
    show first_preview with dissolve2
    $ renpy.pause(2)
    hide first_preview with dissolve2
    jump CardGame_menu
label CardGame_menu:
    $ RandCheck = 0
    $ step = 0
    $ girl = "girl"
    hide screen CardGameFinal
    hide screen CardGameChoose
    hide screen CardGameChoose2
    hide screen CardGameCards
    stop ambience
    stop music fadeout 2
    stop sound
    stop sound_loop
    $ renpy.pause (2, hard=True)
    $ sunset_time ()
    play music persona5_2_menu fadein 5
    scene menu_bg_SM with Dissolve(2)
    show leaffall_small_l_sm with Dissolve(3)
    call screen CardGame_menu with Dissolve(3)
