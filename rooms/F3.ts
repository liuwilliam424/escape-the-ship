import { room_file } from "./struct";

let tst = {
  "height": 480,
  "width": 2880,
  "player_x": 0,
  "player_y": 0,
  "background": ["media/hallway/bg_0.png", "media/hallway/bg_1.png", "media/hallway/bg_2.png"],
  "dialog": ["What a long hallway... It's so clean and fancy! Look at those chandeliers! Well, except for that creepy graffiti..."],
  "objects": [
    {
      "pos": [1360, 0],
      "size": [110, 210],
      "images": [
        "media/hallway/door_112.png",
        "media/hallway/door_112_active.png",
        "media/hallway/opened_door.png"
      ],
      "use": {
        "type": "portal",
        "dest": "room112"
      },
      "needs":{
        "object":"key_112",
        "dialog":"Room 112 is locked. You cannot enter this room without its respective key card."
      }
    },
    {
      "pos": [1560, 0],
      "size": [110, 210],
      "images": [
        "media/hallway/door_113.png",
        "media/hallway/door_113_active.png",
        "media/hallway/opened_door.png"
      ],
      "use": {
        "type": "portal",
        "dest": "room113"
      },
      "needs":{
        "object":"key_113",
        "dialog":"Room 113 is locked. You cannot enter this room without its respective key card."
      }

    },
    {
      "pos": [1760, 0],
      "size": [110, 210],
      "images": [
        "media/hallway/door_114.png",
        "media/hallway/door_114_active.png",
        "media/hallway/opened_door.png"
      ],
      "use": {
        "type": "portal",
        "dest": "room114"
      }
    },
    {
      "pos": [1960, 0],
      "size": [110, 210],
      "images": [
        "media/hallway/door_115.png",
        "media/hallway/door_115_active.png",
        "media/hallway/opened_door.png"
      ],
      "use": {
        "type": "portal",
        "dest": "room115"
      }
    },
    {
      "pos": [2160, 0],
      "size": [110, 210],
      "images": [
        "media/hallway/door_116.png",
        "media/hallway/door_116_active.png",
        "media/hallway/opened_door.png"
      ],
      "use": {
        "type": "portal",
        "dest": "room116"
      }
    },
    {
      "pos": [2360, 0],
      "size": [110, 210],
      "images": [
        "media/hallway/door_117.png",
        "media/hallway/door_117_active.png",
        "media/hallway/opened_door.png"
      ],
      "use": {
        "type": "portal",
        "dest": "room117"
      }
    },
    {
      "pos": [2620, 0],
      "size": [100, 200],
      "images": [
        "media/hallway/bathroom_door.png",
        "media/hallway/bathroom_door_active.png"
      ],
      "use": {
        "type": "portal",
        "dest": "bathroom1"
      }
    },
    {
      "pos": [2750, 0],
      "size": [100, 200],
      "images": [
        "media/hallway/bathroom_door.png",
        "media/hallway/bathroom_door_active.png"
      ],
      "use": {
        "type": "portal",
        "dest": "bathroom2"
      }
    },
    {
      "pos":[100,0],
      "inherit":"elevator"
    }
  ]
} as room_file
