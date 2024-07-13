import { room_file } from "./struct";

let room114:room_file = {
    "height":480,
    "width":960,
    "player_x":122.5,
    "player_y":0,
    "background":["media/bedroom/114.png"],
    "dialog": ["Wha... what? *Lifts head* What's going on? Why is the ship rumbling?!?! What? I have to escape!", "Use WAD or arrow keys to move. Space or mouseclick is used to interact with objects.", "Press I for inventory and use number keys to drop items.", "Click on items to select. Items can be crafted after being selected together by pressing C.", "Good luck, and thank you for playing. Enjoy your stay..."],
    "objects":[
        {
            "pos":[100,0],
            "size":[110,210],
            "images":["media/hallway/door_114.png","media/hallway/door_114_active.png","media/hallway/opened_door.png"],
            "use":{
                "type":"portal",
                "dest":"F3"
            }
        }
        
    ]
}