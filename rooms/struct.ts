//defines how the data for the game should be structured
//we used typescript because python doesn't have as great of a type-checking system

export interface room_file {
    "height": number,
    "width": number,
    "player_x": number,
    "player_y": number,
    "background": string[],
    "objects": (inherited_object_data | object_data)[],
    /** Dialog shown when you enter a room. Only displays once */
    "dialog"?: string[],
    /** Extra vertical borders for room; specify x value here */
    "borders"?:number[]

}
export interface object_data {
    /** starting bottom-left corner position relative to bottom-left corner of room*/
    "pos": [number, number],
    /** size of obj in pixels (w,h) */
    "size": [number, number],
    /**images for (max) three states: DEFAULT, HOVER, and ACTIVE. For animations, just add an array of images instead */
    "images": (string | string[])[],
    /**(optional) specifies which image states only play forwards once and then backwards once when deactivated (ex. elevator opening) */
    "one_way_animation"?: (0 | 1 | 2)[],
    /**how you can use the obj */
    "use"?: portal | tool | faucet | trap
    /** single dialog when object is interacted with; runs through all strings in array */
    "dialog"?: string[]
    /** Only show the dialog once  */
    "dialog_once"?: boolean

    /** What item it needs to perform intended use; specify empty string to show that this object can never be used */
    "needs"?: {
        "object":string,
        /** If you can't leave the room with the object */
        "reverse"?:boolean 
        /** what is said if the needed object is missing */
        "dialog"?:string|string[] 
    }
}
interface inherited_object_data {
    /**(optional) data to inherit from other objects; if key already exists in level json file, it will not be overriden */
    "inherit": string,
    [x: string]: any
}
interface portal {
    "type": "portal",
    /** room name without the .ts after it */
    "dest": string | dialog_prompt | item_conditional
}
interface tool {
    "type": "tool"
}

// produces an object
interface faucet {
    "type": "faucet",
    /** What is said when the inventory is full */
    "inventory_full_statement"?: string,
    /** obj that will get deposited */
    "object": string
}
interface item_conditional{
    "object":string 
    /** First is if the object isn't in inventory, second is if it is */
    "dest":[string,string]
}
interface dialog_prompt {
    prompt: string[],
    options: { [x: string]: string } //mapping where resulting string relevant to whatever place it is put in
}

//kills player 
interface trap {
    "type": "trap"
    /** When the trap will be activated */
    "when": "immediate"|"activate"
}

export interface tool_data {
    [tool_name: string]: {

        /** size of the obj when placed */
        "size"?: [number, number]
        /** image data */
        "images": string[],
        "dialog"?: string|string[]
    }

}

export type recipes = {
    [x:string]:string[]
}
