import { room_file } from "./struct";

let room115:room_file = {
    "height":480,
    "width":960,
    "player_x":122.5,
    "player_y":0,
    "background":["media/bedroom/115.png"],
    "objects":[
        {
            "pos":[100,0],
            "size":[110,210],
            "images":["media/hallway/door_115.png","media/hallway/door_115_active.png","media/hallway/opened_door.png"],
            "use":{
                "type":"portal",
                "dest":"F3"
            }
        }
    ]
}