import { room_file } from "./struct";

let F1:room_file = {
    "height":480,
    "width":1500,
    "player_x":0,
    "player_y":0,
    "background":["media/engine_room/final_bg.png"],
    "dialog": ["Welcome to the engine room. Try not to get burnt."],
    "objects":[
        {
            "pos":[790,0],
            "dialog":["Woah wat's here?"],
            "size":[710,220],
            "images":["media/engine_room/Engine-Big.png"],
            "dialog":["Oh look! A flashlight!"],
            "use":{
                "type": "faucet",
                "object": "flashlight"
            }
        },
        {
            "pos":[100,0],
            "inherit":"elevator"
        },
        {
            "pos":[725,70],
            "inherit":"note",
            "dialog":["The captain stationed me down here for an important reason. I must carry out my mission successfully to feed my family."]
        },
        {
            "pos":[50,70],
            "inherit":"note",
            "dialog":["For $10,000, Mr. Avery has agreed to sabotage the engine room. You are to station yourself at the base of the elevator and deny him means to escape the ship."]
        }
    ]
}