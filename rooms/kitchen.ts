import { room_file } from "./struct";

const kitchen:room_file = {
    "height":480,
    "width":960,
    "player_x":122.5,
    "player_y":0,
    "background":["media/kitchen/bg.png"],
    "dialog": ["Time to cook!"],
    "objects":[
        {
            "pos":[90,10],
            "size":[130,220],
            "images":["media/kitchen/kitdoor.png","media/kitchen/kitdoor_active.png","media/kitchen/opened_door.png"],
            "use":{
                "type":"portal",
                "dest":"F2"
            }
            
        },
        {
            "pos":[250,70],
            "inherit":"note",
            "dialog":["Delivered crates of food: 5 pallets mushrooms, tomatoes, rice, meat, vegetables; 1 pallet unspecified ingredients marked with caution and flammable signs."]
        },
        {
            "pos":[770,180],
            "size":[90,50],
            "images":["media/kitchen/microwave.png","media/kitchen/microwave_active.png"],
            "dialog":["Woah, a lighter! I'd better be careful with this!"],
            "use":{
                "type":"faucet",
                "object":"lighter"
            }
            
        }
        
        
        
    ]
}