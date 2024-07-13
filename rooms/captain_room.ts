import { room_file } from "./struct";

let tst = {
  "height": 480,
  "width": 1500,
  "player_x": 20,
  "player_y": 0,
  "background": ["media/captain_room/captain.png"],
  "borders":[1150],
  "objects": [
    {
    "pos": [10, 0],
    "inherit": "door",
    "use": {
      "type": "portal",
      "dest": "F4"
    },
    "needs":{
        "object":"key",
        "reverse":true,
        "dialog":"You can't leave with key! That would be stealing!"
    }
  },
  {
    "pos":[800,70],
    "inherit":"note",
    "dialog":["210 million for ship insurance, paying 200k guard 50k explosives, massive profits. T minus 20 minutes until \"blastoff\""]
  },
  {
    "pos": [320, 40],
    "size": [460,390],
    "images":["media/captain_room/painting_active.png","media/captain_room/painting.png"],
    "dialog":["What? It's a key!"],
    "use": {
      "type": "faucet",
      "object": "key"
    }
  }

]
} as room_file
