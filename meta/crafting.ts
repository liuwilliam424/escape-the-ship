import { recipes as recipes } from "../rooms/struct";

//Crafting recipies with products on left side (reactants and products must be valid objects!)
let recipes: recipes = {
    "melted_wax": ["candle", "lighter"],
    "putty": ["talcum", "toothpaste"],
    "wax_indented": ["key", "putty"],
    "copy_key": ["wax_indented", "melted_wax"]
}