CORNELL_LIBRARY_TIMES_URL = "https://api3.libcal.com/api_hours_grid.php?iid=973&lid=0&format=json"

UPDATE_TIME = 86400.0

IMAGE_GITHUB_URL = "https://raw.githubusercontent.com/mjs698/library-hours-hack-challenge/master/Images/"

IMAGE_NAMES = ["africana.jpg", "engineering.jpg", "fine-arts.jpg", "hotel.jpeg", "catherwood.jpg",
"kroch.jpeg", "law.jpg", "management.jpg", "mann.jpeg", "mathematics.jpg", "music.jpg",
"olin.jpeg", "adelson.jpg", "uris.jpeg", "veterinary.jpeg"]

LIBRARY_NAMES = ["Africana Library", "Engineering Library", "Fine Arts Library",
"Hotel School Library", "ILR Library", "Kroch Library",
"Law Library", "Management Library", "Mann Library", "Mathematics Library", "Music Library",
"Olin Library",  "Uris Library"]

LIBRARY_NAMES_JSON = ["Africana Library", "Engineering Library",
"Fine Arts Library", "Hotel School Library",
"Industrial and Labor Relations Library", "Kroch Library, Division of Asia Collections",
"Law Circulation", "Management Library w/Johnson ID",
"Mann Library", "Mathematics Library",
"Music Library", "Olin Library", "Uris Library"]

NORTH = "North"; ENG = "Engineering Quad"; CENTRAL = "Central"; AG = "Ag Quad"

LIBRARY_LOCATION = [[42.457417, -76.482298, NORTH], [42.444788, -76.484156, ENG],
[42.451223, -76.482868, CENTRAL], [42.445543, -76.482155, CENTRAL],
[42.447255, -76.481116, CENTRAL], [42.447904, -76.484290, CENTRAL],
[42.443854, -76.485774, CENTRAL], [42.445893, -76.483254, CENTRAL],
[42.448764, -76.476311, AG], [42.448224, -76.480210, CENTRAL],
[42.450200, -76.483684, CENTRAL], [42.447904, -76.484290, CENTRAL],
[42.447752, -76.485314, CENTRAL]]

DELL_DESK = "Dell Desktops"; DELL_LAPT = "Dell Laptops"; P = "Printers"
BandW = "Black and White Printers"; AC = "Adobe Creative"; CP = "Color Printers"
PC = "Phone Chargers"; MAC_LAPT = "Mac Laptops"; LAPT = "Laptops"
CLAB = "Computer Labs"; CA = "Computer Adapters"
LIB = "Library"; SR = "Study Rooms"
RN = "roomName"; LL = "loudnessLevel"
Q = "Quiet"; L = "Loud"; S = "Silent"

LIBRARY_INFORMATION = [ [[], [DELL_DESK, DELL_LAPT, BandW, AC, PC, "HDMI Adapters"], [], "", "", False],

[[{RN: SR, LL: Q},{RN: LIB, LL: Q}, {RN: "Lobby", LL: L}, {RN: CLAB, LL: Q}], [DELL_DESK], [], "", "", False],

[[{RN: "Tables", LL: Q}], [DELL_LAPT, MAC_LAPT, AC, P], ["Fine Arts Books"], "", "", False],

[[{RN: LIB, LL: L},{RN: "Conference room", LL: Q}, {RN: "Marriott Student Learning Center", LL: Q}],
[DELL_DESK, "Lots of Outlets"], ["Macs", "Coffee Bar", "Terrace"], "", "", False],

[[{RN: "Meeting Rooms", LL: Q},{RN: LIB, LL: Q}, {RN: "Computer Lab", LL: Q}],
[DELL_DESK, LAPT, BandW, CP, AC, CA, PC, "Computer Chargers"], ["Lots of Seating", "Lounge 159",
"Human Resources Books", "Management Books", "Economics Books"], "", "", False],

[[{RN: SR, LL: Q},{RN: LIB, LL: Q}, {RN: "Stacks", LL: Q}], [], ["Division of Asia Collections",
"Rare and Manuscripts Collection", "Stacks"], "", "", False],

[[{RN: "Atrium", LL: L}, {RN: "Basement Common Area", LL: Q}], [DELL_DESK, DELL_LAPT, MAC_LAPT, BandW,
AC, PC, "Computer Chargers", CA], ["Comfy Couches", "Fork and Gavel Cafe (Doesn't take brbs)"], "", "", False],

[[{RN: "Atrium", LL: Q}], [DELL_DESK, "Limited Laptop Access", BandW, CP, "Limited Outlets"], ["Lots of Tables"], "", "", False],

[[{RN: "Mandibles Cafe", LL: L}, {RN: "Maker Space", LL: Q}, {RN: "Lobby", LL: L}, {RN: "Stacks", LL: S},
{RN: "Individual Study Rooms", LL: S}, {RN: "Group Study Rooms", LL: L}, {RN: "3rd Floor", LL: S}], [MAC_LAPT,
DELL_LAPT, CA, DELL_DESK, PC, "Computer Chargers", "Headphones", "Projector", "DSLR Cameras", CP, BandW], ["Mann Lab"], "Manndible", "", False],

[[{RN: "Reading Rooms", LL: Q},{RN: "Talk Zone", LL: L}, {RN: "Stacks", LL: Q}, {RN: "Mezzanine", LL: Q},
{RN: "Seminar Rooms", LL: Q}], [DELL_DESK, DELL_LAPT, BandW, CP, AC], [], "", "", False],

[[{RN: "Atrium",  LL: L}], [DELL_DESK, DELL_LAPT, BandW, AC, "Microphones and Recorders"], ["Comfy Couches", "Desks with Outlets"], "", "", False],
[[], [LAPT, "Chargers", "Calculators", P, "Desktops", "Disk Drives"], ["Map Room", "Copy Center",
"Reference Desk", "Basement", "Stacks", "Umbrellas"], "Amit Bhatia Libe Cafe", "", True],

[[{RN: "Cocktail Lounge 24/7", LL: "Varied"}, {RN: "AD White Library", LL: S}, {RN: CLAB, LL: Q},
{RN: "Tower lounge", LL: L}, {RN: "Library Classroom", LL: Q}, {RN: "The Fishbowl 24 hours", LL: Q}],
[DELL_DESK, DELL_LAPT, MAC_LAPT, "Chargers", "Calculators", BandW, CP, AC], ["Umbrellas"], "", "", False]]
