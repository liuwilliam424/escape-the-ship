import { room_file } from "./struct";

const bathroom2:room_file = {
    "height":480,
    "width":720,
    "player_x":0,
    "player_y":0,
    "background":["media/bathroom/bg.png"],
    "dialog": ["Welcome to the Lady's room. Try not to slip."],
    "objects":[
        {
            "pos":[20,0],
            "size":[110,210],
            "images":["media/hallway/bathroom_door.png","media/hallway/bathroom_door_active.png"],
            "use":{
                "type":"portal",
                "dest":"F3"
            }
            
        },
        {
            "pos":[120,0],
            "size":[150,200],
            "images":["media/bathroom/sink.png"],
            "dialog":["What a clean sink!"]
        },
        {
            "pos":[130,70],
            "inherit":"note",
            "dialog":["The captain has just announced our entrance to international waters! Although I can't wait for this cruise, some things seem... off. The ship smells of gasoline, and the food was gritty..."]
        },
        {
            "pos":[270,0],
            "size":[150,80],
            "images":["media/bathroom/puddle.png"],
            "dialog":["Wow what a slippery and deceptively large puddle! You just slipped! Game over."],
            "use":{
                "type":"trap",
                "when":"immediate"
            }
            
        }
    ]
}