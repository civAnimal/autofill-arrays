import sublime_plugin

DATA = [('fruitsA\tautoFill', '"Apple", "Mango", "Avocado", "Cherry", "Pomegranate"'), ('fruitsB\tautoFill', '"Orange", "Apricot", "Strawberry", "Grapes", "Pear"'), ('fruitsC\tautoFill', '"Peach", "Plum", "Papaya", "Raspberry", "Banana"'), ('fruitsD\tautoFill', '"Guava", "Kumquat", "Tangerine", "Satsuma", "Huckleberry", "Jujube", "Watermellon", "Lychee", "Date", "Fig"'), ('fruitsE\tautoFill', '"Coconut", "Nectarine", "Cranberry", "Quince", "Yuzu", "Clementine", "Lemon", "Lime", "Mulberry", "Grapefruit", "Blueberry", "Passionfruit", "Mandarine", "Falsa", "Loquat"'), ('animalsA\tautoFill', '"Lion", "Fox", "Zebra", "Dinosaur", "Wolf"'), ('animalsB\tautoFill', '"Cheetah", "Bison", "Crocodile", "Gorilla", "Jackal"'), ('animalsC\tautoFill', '"Leapord", "Panda", "Elephant", "Coyote", "Kangaroo"'), ('animalsD\tautoFill', '"Tiger", "Chimpanzee", "Iguana", "Porcupine", "Llama", "Hound", "Bear", "Chipmunk", "Ferret", "Hippopotamus"'), ('animalsE\tautoFill', '"Frog", "Walrus", "Octopus", "Crab", "Lobster", "Shrimp", "Turtle", "Toad", "Otter", "Alligator"'), ('animalsF\tautoFill', '"Deer", "Racoon", "Skunk", "Badger", "Impala", "Beaver", "Gopher", "Armadillo", "Antelope", "Alpaca"'), ('animalsG\tautoFill', '"Cat", "Dog", "Pig", "Horse", "Donkey", "Mule", "Camel", "Mouse", "Hamster", "Monkey", "Cow", "Buffalo", "Sheep", "Goat", "Rabbit", "Hare", "Lizard", "Tortoise", "Ox"'), ('insectsA\tautoFill', '"Ant", "Spider", "Mosquito", "Dragonfly", "Butterfly"'), ('insectsB\tautoFill', '"Moth", "Bee", "Cricket", "Scorpio", "Beetle"'), ('insectsC\tautoFill', '"Fly", "Snail", "Ladybug", "Flea", "Caterpillar"'), ('fishA\tautoFill', '"Shark", "Whale", "Dolphin", "Salmon", "Trout"'), ('fishB\tautoFill', '"Fugu", "Snapper", "Sardine", "Carp", "Koi"'), ('fishC\tautoFill', '"Piranha", "Chimaera", "Barracuda", "Mackerel", "Cod"'), ('fishD\tautoFill', '"Pomfret", "Bowfin", "Angler", "Anchovy", "Duckbill", "Sabertooth", "Zander", "Zingel", "Dory", "Herring", "Mahi_Mahi", "Manta_Ray", "Stingray", "Sturgeon", "Goldfish", "Rohu", "Eel"'), ('birdsA\tautoFill', '"Dove", "Eagle", "Raven", "Penguin", "Owl"'), ('birdsB\tautoFill', '"Swan", "Robin", "Flamingo", "Peacock", "Macaw"'), ('birdsC\tautoFill', '"Kiwi", "Ostrich", "Emu", "Turkey", "Chicken"'), ('birdsD\tautoFill', '"Falcon", "Blue_Jay", "Seagull", "Mockingbird", "Qual", "Goose", "Pigeon", "Stork", "Cuckoo", "Parrot"'), ('birdsE\tautoFill', '"Duck", "Hawk", "Pelican", "Woodpecker", "Kingfisher", "Hummingbird", "Crow", "Albatross", "Swallow", "Sparrow", "Wren"'), ('flowersA\tautoFill', '"Rose", "Dahlia", "Magnolia", "Tulip", "Daisy"'), ('flowersB\tautoFill', '"Sakura", "Zinnia", "Carnation", "Jasmine", "Lily"'), ('flowersC\tautoFill', '"Iris", "Sage", "Azaleas", "Daffodil", "Lilac"'), ('flowersD\tautoFill', '"Lotus", "Periwinkle", "Mimosa", "Lobelia", "Fuchsia", "Peony", "Snapdragon", "Hollyhock", "Primrose", "Cosmos"'), ('flowersE\tautoFill', '"Pansie", "Orchid", "Acacia", "Snowdrop", "Sunflower", "Dandelion", "Morning_Glory", "Buttercup", "Marigold", "Lavender", "Petunia", "Crocus", "Poppy"'), ('vegetablesA\tautoFill', '"Potato", "Pumpkin", "Cabbage", "Broccoli", "Paprika"'), ('vegetablesB\tautoFill', '"Spinach", "Scallion", "Cucumber", "Carrot", "Tomato"'), ('vegetablesC\tautoFill', '"Basil", "Oregano", "Rosemary", "Parsley", "Thyme"'), ('vegetablesD\tautoFill', '"Wasabi", "Ginger", "Coriander", "Fennel", "Jalapeno", "Peanuts", "Anise", "Lavender", "Garlic", "Zucchini"'), ('vegetablesE\tautoFill', '"Mushroom", "Onion", "Chickpeas", "Chamomile", "Lemongrass", "Chives", "Leek", "Rhubarb", "Celery", "Okra"'), ('vegetablesF\tautoFill', '"Turnip", "Shallot", "Lettuce", "Artichoke", "Aubergine", "Asparagus", "Cauliflower", "Beetroot", "Pepper", "Parsnip", "Alfalfa", "Daikon", "Peas", "Yam"'), ('zodiacs\tautoFill', '"Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"'), ('planets\tautoFill', '"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"'), ('days\tautoFill', '"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"'), ('months\tautoFill', '"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"'), ('greeks\tautoFill', '"Aphrodite", "Athena", "Artemis", "Ares", "Apollo", "Demeter", "Dionysus", "Hades", "Hera", "Hermes", "Poseidon", "Zeus"'), ('romans\tautoFill', '"Venus", "Minerva", "Diana", "Mars", "Apollo", "Ceres", "Bacchus", "Pluto", "Juno", "Mercury", "Neptune", "Jupiter"'), ('colorsPrimary\tautoFill', '"Red", "Yellow", "Blue"'), ('colorsSecondary\tautoFill', '"Orange", "Green", "Violet"'), ('colorsTertiary\tautoFill', '"Red_Orange", "Yellow_Orange", "Blue_Green", "Yellow_Green", "Red_Violet", "Blue_Violet"'), ('colorsRainbow\tautoFill', '"Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"'), ('drinks\tautoFill', '"Water", "Milk", "Tea", "Coffee", "Lemonade", "Juice", "Milkshake", "Smoothie", "Soda", "Beer", "Wine"'), ('foodsA\tautoFill', '"Bread", "Cake", "Pizza", "Pasta", "Honey"'), ('foodsB\tautoFill', '"Rice", "Burger", "Cookies", "Spaghetti", "Donut"'), ('foodsC\tautoFill', '"Milk", "Cream", "Butter", "Yogurt", "Cheese"'), ('foodsD\tautoFill', '"Sushi", "Pudding", "Sandwich", "Salsa", "Bagel", "Bacon", "Sausage", "Lasagna", "Muffin", "Pie"'), ('foodsE\tautoFill', '"Chips", "Popcorn", "Ravioli", "Doritos", "Tacos", "Burritos", "Croissant", "Biscuit", "Enchilada", "Nachos"'), ('elementsA\tautoFill', '"Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"'), ('elementsB\tautoFill', '"Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"'), ('elementsC\tautoFill', '"Sodium", "Magnesium", "Aluminium", "Silicon", "Phosphorus"'), ('elementsD\tautoFill', '"Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese"'), ('elementsE\tautoFill', '"Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine"'), ('elementsF\tautoFill', '"Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium"'), ('elementsG\tautoFill', '"Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Caesium"'), ('elementsH\tautoFill', '"Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium"'), ('elementsI\tautoFill', '"Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium"'), ('elementsJ\tautoFill', '"Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine"'), ('elementsK\tautoFill', '"Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium"'), ('elementsL\tautoFill', '"Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium"'), ('elementsM\tautoFill', '"Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"'), ('metalsPrecious\tautoFill', '"Platinum", "Palladium", "Gold", "Silver"'), ('metalsIndustrial\tautoFill', '"Iron", "Steel", "Aluminium", "Copper", "Lead", "Tin", "Zinc", "Nickel", "Magnesium"'), ('seasons\tautoFill', '"Summer", "Autumn", "Winter", "Spring"'), ('gemsA\tautoFill', '"Diamond", "Emerald", "Sapphire", "Ruby", "Pearl"'), ('gemsB\tautoFill', '"Opal", "Topaz", "Amber", "Obsidian", "Tourmaline", "Zircon"'), ('oceans\tautoFill', '"Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Arctic Ocean"'), ('seasA\tautoFill', '"Mediterranean Sea", "Caribbean Sea", "South China Sea", "Bering Sea", "Gulf Of Mexico"'), ('seasB\tautoFill', '"Okhotsk Sea", "Eash China Sea", "Hudson Bay", "Japan Sea", "Andaman Sea", "North Sea", "Red Sea", "Baltic Sea"'), ('riversA\tautoFill', '"Amazon", "Nile", "Yangtze", "Danube", "Ganges"'), ('riversB\tautoFill', '"Mekong", "Indus", "Volga", "Mississippi", "Sepik"'), ('riversC\tautoFill', '"Zambezi", "Euphrates", "Murray", "Tigris", "Zaire"'), ('treesA\tautoFill', '"Oak", "Maple", "Pine", "Sycamore", "Willow"'), ('treesB\tautoFill', '"Cedar", "Mahogany", "Palm", "Birch", "Fern"'), ('treesC\tautoFill', '"Acacia", "Hickory", "Mulberry", "Hibiscus", "Lilac"'), ('treesD\tautoFill', '"Myrtle", "Rosewood", "Poplar", "Sumac", "Zaragoza", "Spruce", "Koyamaki", "Fig", "Olive", "Camellia"'), ('treesE\tautoFill', '"Papaya", "Sandalwood", "Candleberry", "Mimosa", "Locust", "Amborella", "Hemlock", "Aspen", "Ash", "Beech", "Elm"'), ('languagesA\tautoFill', '"English", "Mandarin", "Hindi", "Spanish", "French"'), ('languagesB\tautoFill', '"Arabic", "Bengali", "Russian", "Portuguese", "Indonesian"'), ('languagesC\tautoFill', '"Urdu", "German", "Japanese", "Swahili", "Marathi"'), ('languagesD\tautoFill', '"Telugu", "Punjabi", "Wu", "Tamil", "Turkish"'), ('directionsFour\tautoFill', '"North", "East", "South", "West"'), ('directionsEight\tautoFill', '"North", "North_East", "East", "South_East", "South", "South_West", "West", "North_West"'), ('numbersA\tautoFill', '301, 302, 303, 304, 305'), ('numbersB\tautoFill', '306, 307, 308, 309, 310'), ('numbersC\tautoFill', '311, 312, 313, 314, 315'), ('numbersD\tautoFill', '316, 317, 318, 319, 320, 321, 322, 323, 324, 325'), ('numbersE\tautoFill', '326, 327, 328, 329, 330, 331, 332, 333, 334, 335'), ('numbersF\tautoFill', '336, 337, 338, 339, 340, 341, 342, 343, 344, 345'), ('numbersOddA\tautoFill', '301, 303, 305, 307, 309'), ('numbersOddB\tautoFill', '311, 313, 315, 317, 319'), ('numbersOddC\tautoFill', '321, 323, 325, 327, 329'), ('numbersOddD\tautoFill', '331, 333, 335, 337, 339, 341, 343, 345, 347, 349'), ('numbersOddE\tautoFill', '351, 353, 355, 357, 359, 361, 363, 365, 367, 369'), ('numbersOddF\tautoFill', '371, 373, 375, 377, 379, 381, 383, 385, 387, 389'), ('numbersEvenA\tautoFill', '302, 304, 306, 308, 310'), ('numbersEvenB\tautoFill', '312, 314, 316, 318, 320'), ('numbersEvenC\tautoFill', '322, 324, 326, 328, 330'), ('numbersEvenD\tautoFill', '332, 334, 336, 338, 340, 342, 344, 346, 348, 350'), ('numbersEvenE\tautoFill', '352, 354, 356, 358, 360, 362, 364, 366, 368, 370'), ('numbersEvenF\tautoFill', '372, 374, 376, 378, 380, 382, 384, 386, 388, 390'), ('numbersPrimeA\tautoFill', '2, 3, 5, 7, 11'), ('numbersPrimeB\tautoFill', '13, 17, 19, 23, 29'), ('numbersPrimeC\tautoFill', '31, 37, 41, 43, 47'), ('numbersPrimeD\tautoFill', '53, 59, 61, 67, 71, 73, 79, 83, 89, 97'), ('numbersPrimeE\tautoFill', '101, 103, 107, 109, 113, 127, 131, 137, 139, 149'), ('numbersPrimeF\tautoFill', '151, 157, 163, 167, 173, 179, 181, 191, 193, 197'), ('nummbersG\tautoFill', '346, 347, 348, 349, 350, 351, 352, 353, 354, 355'), ('nummbersH\tautoFill', '356, 357, 358, 359, 360, 361, 362, 363, 364, 365'), ('nummbersI\tautoFill', '366, 367, 368, 369, 370, 371, 372, 373, 374, 375'), ('nummbersJ\tautoFill', '376, 377, 378, 379, 380, 381, 382, 383, 384, 385'), ('nummbersK\tautoFill', '386, 387, 388, 389, 390, 391, 392, 393, 394, 395'), ('nummbersL\tautoFill', '396, 397, 398, 399, 400, 401, 402, 403, 404, 405'), ('nummbersOddG\tautoFill', '391, 393, 395, 397, 399, 401, 403, 405, 407, 409'), ('nummbersOddH\tautoFill', '411, 413, 415, 417, 419, 421, 423, 425, 427, 429'), ('nummbersOddI\tautoFill', '431, 433, 435, 437, 439, 441, 443, 445, 447, 449'), ('nummbersOddJ\tautoFill', '451, 453, 455, 457, 459, 461, 463, 465, 467, 469'), ('nummbersOddK\tautoFill', '471, 473, 475, 477, 479, 481, 483, 485, 487, 489'), ('nummbersOddL\tautoFill', '491, 493, 495, 497, 499, 501, 503, 505, 507, 509'), ('nummbersEvenG\tautoFill', '392, 394, 396, 398, 400, 402, 404, 406, 408, 410'), ('nummbersEvenH\tautoFill', '412, 414, 416, 418, 420, 422, 424, 426, 428, 430'), ('nummbersEvenI\tautoFill', '432, 434, 436, 438, 440, 442, 444, 446, 448, 450'), ('nummbersEvenJ\tautoFill', '452, 454, 456, 458, 460, 462, 464, 466, 468, 470'), ('nummbersEvenK\tautoFill', '472, 474, 476, 478, 480, 482, 484, 486, 488, 490'), ('nummbersEvenL\tautoFill', '492, 494, 496, 498, 500, 502, 504, 506, 508, 510')]

class AutoFillArrays(sublime_plugin.EventListener):

  def on_query_completions(self, view, prefix, locations):
    return DATA

# Copyright (c) 2021 civAnimal ... Email: civanimal@gmail.com ... Twitter: civAnimal
# Released under ... Creative Commons License (CC BY-SA)
