import { room_file } from "./struct";

let room113:room_file = {
    "height":480,
    "width":960,
    "player_x":122.5,
    "player_y":0,
    "background":["media/bedroom/113.png"],
    "dialog": ["I wish I lived here..."],
    "objects":[
        {
            "pos":[100,0],
            "size":[110,210],
            "images":["media/hallway/door_113.png","media/hallway/door_113_active.png","media/hallway/opened_door.png"],
            "use":{
                "type":"portal",
                "dest":"F3"
            }
            
        },
        {
            "pos": [620, 20],
            "size":[230,130],
            "images":["media/bedroom/bed.png","media/bedroom/bed_light.png"],
            "use": {
              "type": "faucet",
              "object": "candle"
            }
            
        }
    ]
}
