import { room_file } from "./struct";

const room112:room_file = {
    "height":480,
    "width":960,
    "player_x":122.5,
    "player_y":0,
    "background":["media/bedroom/112.png"],
    "dialog": ["Wow it feels weird invading someone's room."],
    "objects":[
        {
            "pos":[100,0],
            "size":[110,210],
            "images":["media/hallway/door_112.png","media/hallway/door_112_active.png","media/hallway/opened_door.png"],
            "use":{
                "type":"portal",
                "dest":"F3"
            },
            "needs":{
                "object":"key_112",
                "dialog":"Better not forget your card in here!"
            }
        },
        {
            "pos": [450, 20],
            "size":[90,120],
            "images":["media/bedroom/drawer.png","media/bedroom/drawer_light.png"],
            "use": {
              "type": "faucet",
              "object": "talcum"
            }
            
        }

    ]
}
