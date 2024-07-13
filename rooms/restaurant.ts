import { room_file } from "./struct";

const restaurant:room_file = {
    "height":480,
    "width":720,
    "player_x":122.5,
    "player_y":0,
    "background":["media/restaurant/bg.png"],
    "dialog": ["Time to eat!"],
    "objects":[
        {
            "pos":[600,0],
            "size":[110,210],
            "images":["media/hallway/gendoor.png","media/hallway/gendoor_active.png","media/hallway/opened_door.png"],
            "use":{
                "type":"portal",
                "dest":"F2"
            }
            
        },
        {
            "pos":[130,232],
            "size":[50,25],
            "images":["media/restaurant/cloche.png"],
            "dialog":["It's the key to 112! I wonder who put it here."],
            "use":{
                "type":"faucet",
                "object":"key_112"
            }
            
        },
        {
            "pos":[60,70],
            "inherit":"note",
            "dialog":["Woah! My drink was just knocked over! The ship is quaking! What's happening?"]
        },
        {
            "pos":[240,232],
            "size":[50,25],
            "images":["media/restaurant/cloche.png"],
            "dialog":["Room 113's key card! Why is it in the restaurant..."],
            "use":{
                "type":"faucet",
                "object":"key_113"
            }
            
        },
        {
            "pos":[350,232],
            "size":[50,25],
            "images":["media/restaurant/cloche.png"],
            "dialog":["Nothing to be found here..."]
            
        },
        {
            "pos":[420,115],
            "size":[50,50],
            "images":["media/restaurant/apple.png"],
            "dialog":["You just got poisoned by an apple. Looks like it's the end. Boohoo, you lost. Game over."],
            "use":{
                "type":"trap",
                "when":"activate"
            }
            
        }
    ]
}