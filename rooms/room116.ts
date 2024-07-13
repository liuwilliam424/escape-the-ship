import { room_file } from "./struct";

let room116:room_file = {
    "height":480,
    "width":960,
    "player_x":122.5,
    "player_y":0,
    "background":["media/bedroom/116.png"],
    "objects":[
        {
            "pos":[100,0],
            "size":[110,210],
            "images":["media/hallway/door_116.png","media/hallway/door_116_active.png","media/hallway/opened_door.png"],
            "use":{
                "type":"portal",
                "dest":"F3"
            }
        }
    ]
}