import { room_file } from "./struct";

let tst = {
  "height": 480,
  "width": 720,
  "player_x": 315,
  "player_y": 0,
  "background": ["media/hallway/hall.png"],
  "objects": [{
    "pos": [195, 0],
    "inherit": "elevator"
  }, {
    "pos": [40, 0],
    "inherit": "door",
    "use": {
      "type": "portal",
      "dest": {
        "object":"flashlight",
        "dest":["staff_room_dark","staff_room"]
      }
    },
    "needs":{
      "object":"copy_key",
      "dialog":"Hmm... I need a key to enter"
    }


  },
  {
    "pos":[450,70],
    "inherit":"note",
    "dialog":["Hehe, nobody is going to sneak past me! The captain has promised me fabulous rewards for guarding his room. I hear there's something interesting brewing..."]
  },
  {
    "pos": [570, 0],
    "inherit": "door",
    "use": {
      "type": "portal",
      "dest": "captain_room"
    }
  }]

} as room_file
