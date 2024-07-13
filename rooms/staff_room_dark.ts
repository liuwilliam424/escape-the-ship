import { room_file } from "./struct";

let tst = {
  "height": 480,
  "width": 100,
  "player_x": 0,
  "player_y": 0,
  "background": ["media/dark.png"],
  "dialog":["It's too dark in there...","I'm...","scared of the dark...","perhaps I'll enter if I find a light source","use [space] to leave"],
  "objects": [{
    "pos":[0,0],
    "images":["media/dark.png"],
    "size":[100,480],
    "use":{
      "type":"portal",
      "dest":"F4"
    }
  }]

} as room_file
