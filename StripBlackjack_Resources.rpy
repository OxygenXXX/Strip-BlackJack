
init -25 python:

    sprite_width_close = 1125
    sprite_height_close = 1080

    sprite_width_normal = 900
    sprite_height_normal = 1080

    sprite_width_far = 675
    sprite_height_far = 1080

init -20:

    image dv body first close = Composite(
        (sprite_width_close, sprite_height_close),
        (0, 0), "sprites/close/dv/dv_1_body.png"
    )

    image dv body second close = Composite(
        (sprite_width_close, sprite_height_close),
        (0, 0), "sprites/close/dv/dv_2_body.png"
    )

    image dv body third close = Composite(
        (sprite_width_close, sprite_height_close),
        (0, 0), "sprites/close/dv/dv_3_body.png"
    )

    image dv body fourth close = Composite(
        (sprite_width_close, sprite_height_close),
        (0, 0), "sprites/close/dv/dv_4_body.png"
    )

    image dv body fifth close = Composite(
        (sprite_width_close, sprite_height_close),
        (0, 0), "sprites/close/dv/dv_5_body.png"
    )