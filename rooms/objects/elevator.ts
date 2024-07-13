import { object_data } from "../struct"

let elevtor: object_data = {
  "size": [330, 330],
  "pos": [1275, 0], 
  "images": [
    "media/elevator/1.png",
    [
      "media/elevator/1.png",
      "media/elevator/2.png",
      "media/elevator/3.png",
      "media/elevator/4.png",
      "media/elevator/5.png",
      "media/elevator/6.png",
      "media/elevator/7.png",
      "media/elevator/8.png",
      "media/elevator/9.png",
      "media/elevator/10.png",
      "media/elevator/11.png",
      "media/elevator/12.png",
      "media/elevator/13.png",
      "media/elevator/14.png"
    ],
    "media/elevator/1.png"
  ],
  "one_way_animation": [1],
  "use": {
    "type": "portal",
    "dest": {
      "prompt":["Which floor do you wish to go to? (1 is lowest)"],
      "options":{"1":"F1","2":"F2","3":"F3","4":"F4"}
    }
  }
}
