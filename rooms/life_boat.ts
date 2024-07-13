import { room_file } from "./struct";

let tst = {
  "height": 480,
  "width": 966,
  "player_x": 800,
  "player_y": 0,
  "background": ["media/staff/life.tiff"],
  "objects": [{
    "pos": [785, 0],
    "inherit": "big_door",
    "use": {
      "type": "portal",
      "dest": "staff_room"
    }
  },{
    "pos":[100,110],
    "size":[250,250],
    "images":["media/staff/raft.png"],
    "use":{
      "type":"portal",
      "dest":"win"
    }
  }]

} as room_file
