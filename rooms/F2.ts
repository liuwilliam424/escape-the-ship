import { room_file } from "./struct";

let tst = {
  "height": 480,
  "width": 720,
  "player_x": 0,
  "player_y": 0,
  "background": ["media/hallway/hall.png"],
  "dialog": ["Man, what is that smell! It smells delicious. I'm hungry. If only I could eat an apple..."],
  "objects": [
    {
      "pos": [195, 0],
      "inherit": "elevator"
    },
    {
      "pos": [50, 0],
      "size": [110, 210],
      "images":[
        "media/hallway/gendoor.png",
        "media/hallway/gendoor_active.png",
        "media/hallway/opened_door.png"
      ],
      "use": {
        "type": "portal",
        "dest": "restaurant"
      }
    },
    {
      "pos": [570, 0],
      "size": [110, 210],
      "images": [
        "media/hallway/gendoor.png",
        "media/hallway/gendoor_active.png",
        "media/hallway/opened_door.png"
      ],
      "use": {
        "type": "portal",
        "dest": "kitchen"
      }
    }
  ]
} as room_file
