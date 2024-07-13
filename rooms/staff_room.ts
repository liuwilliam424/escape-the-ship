import { room_file } from "./struct";

let tst = {
  "height": 480,
  "width": 1400,
  "player_x": 1200,
  "player_y": 0,
  "background": ["media/staff/bg.png"],
  "dialog":["Oh! There's a light switch here. I guess I don't need the flashlight anymore."],
  "objects": [{
    "pos": [1185, 0],
    "inherit": "door",
    "use": {
      "type": "portal",
      "dest": "F4"
    }
  },{
    "pos": [95, 0],
    "inherit": "big_door",
    "use": {
      "type": "portal",
      "dest": "life_boat"
    }
  }]

} as room_file
