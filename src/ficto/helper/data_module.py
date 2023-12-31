# Mapping of countries to their corresponding country codes
country_to_code = {
    "US": "US",
    "UK": "UK",
    "Canada": "CA",
    "Australia": "AUS",
    "Germany": "DE",
    "France": "FR",
    "Japan": "JP",
    "China": "CN",
    "India": "IN",
    "Brazil": "BR",
    "Russia": "RU",
    "South Africa": "ZA",
    "Mexico": "MX",
    "Italy": "IT",
    "Spain": "ES",
    "South Korea": "KR",
    "Saudi Arabia": "SA",
    "Argentina": "AR",
    "Turkey": "TR",
    "Netherlands": "NL",
    "Sweden": "SE",
    "Switzerland": "CH",
    "Singapore": "SG",
    "New Zealand": "NZ",
    "Norway": "NO",
    "Denmark": "DK",
    "Ireland": "IE",
    "Finland": "FI",
    "Austria": "AT",
    "Belgium": "BE",
    "Portugal": "PT",
    "Greece": "GR"
    # Add more mappings as needed
}
# Mapping of countries to their corresponding currency codes
country_to_currency = {
    "US": "USD",
    "UK": "GBP",
    "Canada": "CAD",
    "Australia": "AUD",
    "Germany": "EUR",
    "France": "EUR",
    "Japan": "JPY",
    "China": "CNY",
    "India": "INR",
    "Brazil": "BRL",
    "Russia": "RUB",
    "South Africa": "ZAR",
    "Mexico": "MXN",
    "Italy": "EUR",
    "Spain": "EUR",
    "South Korea": "KRW",
    "Saudi Arabia": "SAR",
    "Argentina": "ARS",
    "Turkey": "TRY",
    "Netherlands": "EUR",
    "Sweden": "SEK",
    "Switzerland": "CHF",
    "Singapore": "SGD",
    "New Zealand": "NZD",
    "Norway": "NOK",
    "Denmark": "DKK",
    "Ireland": "EUR",
    "Finland": "EUR",
    "Austria": "EUR",
    "Belgium": "EUR",
    "Portugal": "EUR",
    "Greece": "EUR"
    # Add more country-to-currency mappings as needed
}
# Passport formats for various countries
passport_formats = {
    "US": "AA######",
    "UK": "######",
    "Canada": "AA######",
    "Australia": "########",
    "Germany": "#########",
    "France": "#########",
    "Japan": "AA########",
    "China": "##########",
    "India": "##########",
    "Brazil": "########",
    "Russia": "#########",
    "South Africa": "AA########",
    "Mexico": "########",
    "Italy": "#########",
    "Spain": "#########",
    "South Korea": "########",
    "Saudi Arabia": "AA########",
    "Argentina": "#########",
    "Turkey": "#########",
    "Netherlands": "#########",
    "Sweden": "#########",
    "Switzerland": "#########",
    "Singapore": "AA########",
    "New Zealand": "#########",
    "Norway": "#########",
    "Denmark": "#########",
    "Ireland": "#########",
    "Finland": "#########",
    "Austria": "#########",
    "Belgium": "#########",
    "Portugal": "#########",
    "Greece": "#########"
    # Add more formats for other countries as needed
}
# Social Security Number (SSN) formats for various countries
ssn_formats = {
    "US": "###-##-####",
    "UK": "##-##-##",
    "Canada": "###-###-###",
    "Australia": "#########",
    "Germany": "#########",
    "France": "##-##-##-###",
    "Japan": "###-##-####",
    "China": "##########",
    "India": "##########",
    "Brazil": "###-##-###",
    "Russia": "###-##-####",
    "South Africa": "##-##-##-###",
    "Mexico": "###-##-####",
    "Italy": "#########",
    "Spain": "#########",
    "South Korea": "#########",
    "Saudi Arabia": "##-######-####",
    "Argentina": "##-###-###",
    "Turkey": "#########",
    "Netherlands": "#########",
    "Sweden": "########-####",
    "Switzerland": "###-###-###-###",
    "Singapore": "S########",
    "New Zealand": "#########",
    "Norway": "#########",
    "Denmark": "#########",
    "Ireland": "#########",
    "Finland": "########-###",
    "Austria": "#########",
    "Belgium": "########-###",
    "Portugal": "#########",
    "Greece": "###-##-####"
    # Add more formats for other countries as needed
}
# Phone number formats for various countries
phone_formats = {
    "US": "+1-XXX-XXX-XXXX",
    "UK": "+44-7XXX-XXX-XXX",
    "AUS": "+61-4XX-XXX-XXX",
    "CA": "+1-XXX-XXX-XXXX",  # Canadian format is similar to the US
    "Germany": "+49-XXXX-XXXXXXX",
    "France": "+33-X-XX-XX-XX-XX",
    "Japan": "+81-XX-XXXX-XXXX",
    "China": "+86-1XXX-XXXX-XXXX",
    "India": "+91-9XX-XXXX-XXXX",
    "Brazil": "+55-9XXXX-XXXX",
    "Russia": "+7-XXX-XXX-XX-XX",
    "South Africa": "+27-XX-XXX-XXXX",
    "Mexico": "+52-1-XXX-XXX-XXXX",
    "Italy": "+39-3XX-XXX-XXXX",
    "Spain": "+34-6XX-XXX-XXX",
    "South Korea": "+82-1XXX-XXXX-XXXX",
    "Saudi Arabia": "+966-5XX-XXXX-XXX",
    "Argentina": "+54-9XX-XXXX-XXXX",
    "Turkey": "+90-5XX-XXX-XX-XX",
    "Netherlands": "+31-6-XXXXXXXX",
    "Sweden": "+46-7X-XXX-XX-XX",
    "Switzerland": "+41-7XX-XXX-XXX",
    "Singapore": "+65-9XXX-XXXX",
    "New Zealand": "+64-2X-XXXX-XXXX",
    "Norway": "+47-9X-XX-XX-XX",
    "Denmark": "+45-2X-XX-XX-XX",
    "Ireland": "+353-8X-XXX-XXXX",
    "Finland": "+358-4X-XXXX-XXX",
    "Austria": "+43-6X-XXXXXXX",
    "Belgium": "+32-4X-XX-XX-XX",
    "Portugal": "+351-9XX-XXXXXX",
    "Greece": "+30-6XX-XXX-XXXX"
    # Add more formats for other countries as needed
}
# Mapping of departments to lists of job designations within each department
designation_mapping = {
    "Marketing": [
        "Jr. Executive",
        "Executive",
        "Sr. Executive",
        "Asst. Manager",
        "Manager",
        "Sr. Manager",
        "Asst. Director",
        "Director",
        "AVP",
        "VP",
        "CMO",
    ],
    "Sales": [
        "Sales Associate",
        "Sales Representative",
        "Account Executive",
        "Account Manager",
        "Sales Manager",
        "Sr. Sales Manager",
        "Director of Sales",
        "VP of Sales",
    ],
    "Finance": [
        "Jr. Accountant",
        "Accountant",
        "Sr. Accountant",
        "Asst. Controller",
        "Controller",
        "Sr. Controller",
        "CFO",
    ],
    "IT": [
        "Jr. Developer",
        "Developer",
        "Sr. Developer",
        "Lead Developer",
        "Technical Lead",
        "Manager of IT",
        "Director of IT",
        "CTO",
    ],
    "Operations": [
        "Operations Associate",
        "Operations Coordinator",
        "Operations Supervisor",
        "Operations Manager",
        "Sr. Operations Manager",
        "Director of Operations",
        "VP of Operations",
    ],
    "Procurement": [
        "Procurement Assistant",
        "Procurement Specialist",
        "Procurement Analyst",
        "Procurement Manager",
        "Sr. Procurement Manager",
        "Director of Procurement",
        "VP of Procurement",
    ],
    "Accounts": [
        "Jr. Accountant",
        "Accountant",
        "Sr. Accountant",
        "Asst. Controller",
        "Controller",
        "Sr. Controller",
        "CFO",
    ],
    "HR": [
        "Jr. HR Executive",
        "HR Executive",
        "Sr. HR Executive",
        "HR Manager",
        "Sr. HR Manager",
        "HR Director",
        "VP of HR",
    ],
    "Customer Service": [
        "Customer Service Representative",
        "Customer Service Specialist",
        "Customer Service Coordinator",
        "Customer Service Manager",
        "Sr. Customer Service Manager",
        "Director of Customer Service",
        "VP of Customer Service",
    ],
    "Research and Development": [
        "Research Assistant",
        "Research Associate",
        "Research Scientist",
        "Sr. Research Scientist",
        "Lead Research Scientist",
        "Director of Research and Development",
        "VP of R&D",
    ],
    "Quality Assurance": [
        "QA Tester",
        "QA Engineer",
        "QA Analyst",
        "Sr. QA Analyst",
        "Lead QA Engineer",
        "Director of Quality Assurance",
        "VP of Quality Assurance",
    ],
    "Legal": [
        "Legal Assistant",
        "Legal Secretary",
        "Paralegal",
        "Legal Counsel",
        "Sr. Legal Counsel",
        "Director of Legal",
        "VP of Legal",
    ],
    "Public Relations": [
        "PR Assistant",
        "PR Coordinator",
        "PR Specialist",
        "PR Manager",
        "Sr. PR Manager",
        "Director of PR",
        "VP of PR",
    ],
    "Supply Chain": [
        "Supply Chain Assistant",
        "Supply Chain Coordinator",
        "Supply Chain Analyst",
        "Supply Chain Manager",
        "Sr. Supply Chain Manager",
        "Director of Supply Chain",
        "VP of Supply Chain",
    ],
    "Engineering": [
        "Jr. Engineer",
        "Engineer",
        "Deputy Engineer",
        "Assistant Engineer",
        "Executive Engineer",
        "Superintending Engineer",
        "Asst. Director",
        "Director",
        "AVP",
        "VP",
        "CTO",
    ],
    "Product Management": [
        "Product Assistant",
        "Product Coordinator",
        "Product Manager",
        "Sr. Product Manager",
        "Director of Product Management",
        "VP of Product Management",
    ],
    "Health and Safety": [
        "Safety Officer",
        "Health and Safety Coordinator",
        "Health and Safety Specialist",
        "Health and Safety Manager",
        "Sr. Health and Safety Manager",
        "Director of Health and Safety",
        "VP of Health and Safety",
    ],
    "Training and Development": [
        "Training Assistant",
        "Training Coordinator",
        "Training Specialist",
        "Training Manager",
        "Sr. Training Manager",
        "Director of Training and Development",
        "VP of Training and Development",
    ],
    "Business Development": [
        "Business Development Associate",
        "Business Development Representative",
        "Business Development Executive",
        "Business Development Manager",
        "Sr. Business Development Manager",
        "Director of Business Development",
        "VP of Business Development",
    ],
    "Facilities Management": [
        "Facilities Assistant",
        "Facilities Coordinator",
        "Facilities Manager",
        "Sr. Facilities Manager",
        "Director of Facilities Management",
        "VP of Facilities Management",
    ],
    "Data Science": [
        "Data Scientist",
        "Sr. Data Scientist",
        "Lead Data Scientist",
        "Data Science Manager",
        "Director of Data Science",
        "VP of Data Science",
    ],
}

# Mapping of countries to states and cities within each state
country_to_states_and_cities = {
    "US": {
        "Alabama": [
            "Montgomery",
            "Auburn",
            "Birmingham",
            "Huntsville",
            "Dothan",
            "Mobile",
            "Tuscaloosa",
            "Decatur",
            "Hoover",
            "Florence",
        ],
        "Arizona": [
            "Phoenix",
            "Tucson",
            "Yuma",
            "Tempe",
            "Gilbert",
            "Sedona",
            "Scottsdale",
            "Chandler",
            "Flagstaff",
            "Mesa",
        ],
        "California": [
            "Los Angeles",
            "San Francisco",
            "San Diego",
            "Sacramento",
            "Fresno",
            "San Jose",
            "Oakland",
            "Long Beach",
            "Santa Ana",
            "Anaheim",
        ],
        "Texas": [
            "Houston",
            "Dallas",
            "Austin",
            "San Antonio",
            "Fort Worth",
            "El Paso",
            "Arlington",
            "Corpus Christi",
            "Plano",
            "Laredo",
        ],
        "New York": [
            "New York City",
            "Buffalo",
            "Rochester",
            "Albany",
            "Syracuse",
            "Yonkers",
            "White Plains",
            "Utica",
            "Schenectady",
            "New Rochelle",
        ],
        "Florida": [
            "Miami",
            "Orlando",
            "Tampa",
            "Jacksonville",
            "Fort Lauderdale",
            "Pensacola",
            "Tallahassee",
            "St. Petersburg",
            "Naples",
            "Fort Myers",
        ],
        "Illinois": [
            "Chicago",
            "Springfield",
            "Peoria",
            "Aurora",
            "Rockford",
            "Joliet",
            "Naperville",
            "Elgin",
            "Waukegan",
            "Champaign",
        ],
        "Georgia": [
            "Atlanta",
            "Augusta",
            "Savannah",
            "Columbus",
            "Macon",
            "Athens",
            "Albany",
            "Sandy Springs",
            "Roswell",
            "Johns Creek",
        ],
        "Michigan": [
            "Detroit",
            "Grand Rapids",
            "Ann Arbor",
            "Lansing",
            "Flint",
            "Kalamazoo",
            "Dearborn",
            "Sterling Heights",
            "Livonia",
            "Troy",
        ],
        "Colorado": [
            "Denver",
            "Colorado Springs",
            "Aurora",
            "Fort Collins",
            "Lakewood",
            "Thornton",
            "Arvada",
            "Westminster",
            "Centennial",
            "Boulder",
        ],
    },
    "UK": {
        "Norfolk": ["Holt", "Cromer", "King's Lynn", "Aylsham", "Hunstanton"],
        "Kent": ["Canterbury", "Maidstone", "Dover", "Margate", "Ashford"],
        "Surrey": ["Guildford", "Woking", "Camberley", "Epsom", "Esher"],
        "Essex": ["Chelmsford", "Basildon", "Colchester", "Southend-on-Sea", "Harlow"],
        "Hampshire": [
            "Winchester",
            "Southampton",
            "Portsmouth",
            "Basingstoke",
            "Gosport",
        ],
        "West Midlands": [
            "Birmingham",
            "Coventry",
            "Wolverhampton",
            "Solihull",
            "Dudley",
        ],
        "Lancashire": ["Manchester", "Liverpool", "Preston", "Blackpool", "Burnley"],
        "Devon": ["Exeter", "Plymouth", "Torquay", "Paignton", "Exmouth"],
        "Oxfordshire": ["Oxford", "Banbury", "Bicester", "Abingdon", "Witney"],
        "North Yorkshire": [
            "York",
            "Harrogate",
            "Scarborough",
            "Middlesbrough",
            "Selby",
        ],
    },
    "Canada": {
        "Ontario": [
            "Toronto",
            "Ottawa",
            "Hamilton",
            "London",
            "Mississauga",
            "Brampton",
            "Markham",
            "Vaughan",
            "Windsor",
            "Kitchener",
        ],
        "Quebec": [
            "Montreal",
            "Quebec City",
            "Laval",
            "Gatineau",
            "Longueuil",
            "Sherbrooke",
            "Saguenay",
            "Levis",
            "Trois-Rivieres",
            "Terrebonne",
        ],
        "British Columbia": [
            "Vancouver",
            "Surrey",
            "Burnaby",
            "Richmond",
            "Kelowna",
            "Kamloops",
            "Nanaimo",
            "Victoria",
            "Abbotsford",
            "Langley",
        ],
        "Alberta": [
            "Calgary",
            "Edmonton",
            "Red Deer",
            "Lethbridge",
            "St. Albert",
            "Medicine Hat",
            "Grande Prairie",
            "Airdrie",
            "Spruce Grove",
            "Leduc",
        ],
        "Manitoba": [
            "Winnipeg",
            "Brandon",
            "Steinbach",
            "Thompson",
            "Portage la Prairie",
            "Selkirk",
            "Winkler",
            "Dauphin",
            "Morden",
            "Flin Flon",
        ],
    },
    "Australia": {
        "New South Wales": [
            "Sydney",
            "Newcastle",
            "Central Coast",
            "Wollongong",
            "Maitland",
            "Blue Mountains",
            "Queanbeyan",
            "Goulburn",
            "Tamworth",
            "Orange",
        ],
        "Victoria": [
            "Melbourne",
            "Geelong",
            "Ballarat",
            "Bendigo",
            "Shepparton",
            "Melton",
            "Mildura",
            "Wodonga",
            "Warrnambool",
            "Sunbury",
        ],
        "Queensland": [
            "Brisbane",
            "Gold Coast",
            "Sunshine Coast",
            "Townsville",
            "Cairns",
            "Toowoomba",
            "Mackay",
            "Rockhampton",
            "Bundaberg",
            "Hervey Bay",
        ],
        "Western Australia": [
            "Perth",
            "Mandurah",
            "Bunbury",
            "Geraldton",
            "Albany",
            "Kalgoorlie",
            "Broome",
            "Karratha",
            "Port Hedland",
            "Rockingham",
        ],
        "South Australia": [
            "Adelaide",
            "Mount Gambier",
            "Whyalla",
            "Murray Bridge",
            "Port Augusta",
            "Port Pirie",
            "Port Lincoln",
            "Victor Harbor",
            "Gawler",
            "Goolwa",
        ],
    },
}
# Mapping of product categories to lists of product names within each category
product_names_dict = {
    "Electronics": [
        "Smartphone",
        "Laptop",
        "Headphones",
        "Tablet",
        "Camera",
        "Smartwatch",
        "Speaker",
        "Gaming Console",
        "Wireless Earbuds",
        "Power Bank",
        "TV",
        "Fitness Tracker",
        "Virtual Reality Headset",
        "Printer",
        "External Hard Drive",
        "Drone",
        "Bluetooth Keyboard",
        "Home Security Camera",
        "Wireless Charger",
        "Portable Projector",
    ],
    "Clothing": [
        "T-shirt",
        "Jeans",
        "Dress",
        "Shoes",
        "Sweater",
        "Jacket",
        "Hat",
        "Socks",
        "Skirt",
        "Pants",
        "Scarf",
        "Gloves",
        "Hoodie",
        "Boots",
        "Watch",
        "Tie",
        "Belt",
        "Sunglasses",
        "Backpack",
        "Umbrella",
    ],
    "Home and Kitchen": [
        "Coffee Maker",
        "Blender",
        "Toaster",
        "Microwave",
        "Pots and Pans",
        "Cutlery Set",
        "Dishwasher",
        "Air Fryer",
        "Refrigerator",
        "Kettle",
        "Vacuum Cleaner",
        "Food Processor",
        "Stand Mixer",
        "Bread Maker",
        "Waffle Maker",
        "Slow Cooker",
        "Knife Set",
        "Coffee Grinder",
        "Juicer",
        "Espresso Machine",
    ],
    "Books": [
        "Fiction",
        "Non-Fiction",
        "Mystery",
        "Science Fiction",
        "Biography",
        "Fantasy",
        "Romance",
        "Thriller",
        "Self-Help",
        "Cookbook",
        "History",
        "Science",
        "Art",
        "Travel",
        "Poetry",
        "Business",
        "Health",
        "Children's",
        "Classic Literature",
        "Humor",
    ],
    "Toys": [
        "Action Figures",
        "Dolls",
        "Building Blocks",
        "Board Games",
        "Puzzles",
        "Remote Control Cars",
        "Stuffed Animals",
        "Educational Toys",
        "Outdoor Toys",
        "Art Supplies",
        "Sports Equipment",
        "Play Kitchen",
        "Toy Cars",
        "Dress-Up Clothes",
        "Musical Toys",
        "Science Kits",
        "Robot Toys",
        "Magic Sets",
        "Water Guns",
        "Toy Trains",
    ],
    "Beauty and Personal Care": [
        "Shampoo",
        "Conditioner",
        "Body Wash",
        "Face Moisturizer",
        "Sunscreen",
        "Makeup Remover",
        "Lip Balm",
        "Perfume",
        "Hair Dryer",
        "Flat Iron",
        "Electric Toothbrush",
        "Razor",
        "Cologne",
        "Nail Polish",
        "Facial Cleanser",
        "Hand Cream",
        "Deodorant",
        "Hair Styling Gel",
        "Curling Iron",
        "Eye Cream",
    ],
    "Sports and Outdoors": [
        "Tent",
        "Hiking Boots",
        "Backpack",
        "Camping Stove",
        "Sleeping Bag",
        "Binoculars",
        "Fishing Rod",
        "Bicycle",
        "Running Shoes",
        "Water Bottle",
        "Golf Clubs",
        "Ski Gear",
        "Yoga Mat",
        "Swimming Goggles",
        "Soccer Ball",
        "Basketball",
        "Tennis Racket",
        "Football",
        "Baseball Glove",
        "Hammock",
    ],
    "Automotive": [
        "Car Battery",
        "Tire Pressure Gauge",
        "Car Wax",
        "Oil Filter",
        "Windshield Wipers",
        "Jump Starter",
        "Car Seat Covers",
        "Car Vacuum",
        "Dash Cam",
        "GPS Navigation System",
        "Car Air Freshener",
        "Roof Rack",
        "Car Charger",
        "Car Jack",
        "Floor Mats",
        "Car Wash Kit",
        "Tool Set",
        "Snow Chains",
        "Car Cover",
        "Bluetooth Car Adapter",
    ],
    "Health and Household": [
        "Vitamins",
        "First Aid Kit",
        "Air Purifier",
        "Humidifier",
        "Water Filter",
        "Thermometer",
        "Weight Scale",
        "Blood Pressure Monitor",
        "Sleeping Mask",
        "Electric Blanket",
        "Essential Oils",
        "Cleaning Supplies",
        "Laundry Detergent",
        "Trash Bags",
        "Paper Towels",
        "Hand Sanitizer",
        "Bath Towels",
        "Mop and Bucket",
        "Dish Soap",
        "Toothpaste",
    ],
    "Tools and Home Improvement": [
        "Drill",
        "Screwdriver Set",
        "Wrench",
        "Toolbox",
        "Power Drill",
        "Circular Saw",
        "Measuring Tape",
        "Paint Brushes",
        "Ladder",
        "Safety Glasses",
        "Socket Set",
        "Hacksaw",
        "Plunger",
        "Extension Cord",
        "Cordless Screwdriver",
        "Flashlight",
        "Nails and Screws Assortment",
        "Level",
        "Stud Finder",
        "Work Gloves",
    ],
    "Grocery": [
        "Cereal",
        "Pasta",
        "Rice",
        "Canned Soup",
        "Frozen Vegetables",
        "Fresh Fruits",
        "Bread",
        "Milk",
        "Eggs",
        "Cheese",
        "Yogurt",
        "Snack Bars",
        "Juice",
        "Coffee",
        "Tea",
        "Cookies",
        "Chocolate",
        "Condiments",
        "Cereal Bars",
        "Nuts",
    ],
    "Pet Supplies": [
        "Dog Food",
        "Cat Food",
        "Pet Bed",
        "Dog Collar",
        "Cat Litter",
        "Fish Tank",
        "Bird Cage",
        "Pet Toys",
        "Dog Leash",
        "Pet Grooming Kit",
        "Reptile Habitat",
        "Small Animal Cage",
        "Aquarium Filter",
        "Hamster Wheel",
        "Pet Carrier",
        "Bird Feeder",
        "Dog Shampoo",
        "Cat Scratcher",
        "Fish Food",
        "Treats",
    ],
    "Baby": [
        "Diapers",
        "Baby Wipes",
        "Baby Formula",
        "Baby Clothes",
        "Pacifiers",
        "Baby Bottles",
        "Stroller",
        "Car Seat",
        "Baby Monitor",
        "High Chair",
        "Crib",
        "Changing Table",
        "Baby Carrier",
        "Playpen",
        "Diaper Bag",
        "Baby Shoes",
        "Teething Toys",
        "Baby Blanket",
        "Nursery Decor",
        "Baby Swaddle",
    ],
    "Office Products": [
        "Desk Organizer",
        "Laptop Stand",
        "Office Chair",
        "Printer Paper",
        "Notebooks",
        "Pens",
        "Stapler",
        "Desk Lamp",
        "Filing Cabinet",
        "Whiteboard",
        "Mouse Pad",
        "Computer Monitor",
        "Desk Calendar",
        "Headset",
        "Desk Fan",
        "Hole Punch",
        "Scissors",
        "Paper Clips",
        "Business Cards Holder",
        "Desk Clock",
    ],
    "Jewelry": [
        "Necklace",
        "Bracelet",
        "Earrings",
        "Ring",
        "Watch",
        "Anklet",
        "Brooch",
        "Cufflinks",
        "Pendant",
        "Charm Bracelet",
        "Jewelry Box",
        "Hairpin",
        "Bangle",
        "Pearl Necklace",
        "Diamond Stud Earrings",
        "Gold Chain",
        "Gemstone Ring",
        "Silver Hoop Earrings",
        "Wedding Band",
        "Lockets",
    ],
    "Movies and TV": [
        "DVDs",
        "Blu-ray Discs",
        "TV Series Box Set",
        "Streaming Device",
        "Movie Posters",
        "Popcorn Maker",
        "Movie Tickets",
        "Soundbar",
        "Projector",
        "Home Theater System",
        "TV Stand",
        "Media Storage Tower",
        "Movie Merchandise",
        "Collectibles",
        "Movie Trivia Games",
        "Movie Soundtracks",
        "Film Cameras",
        "Action Figure Collectibles",
        "Movie Scripts",
        "Movie Magazines",
    ],
    "Video Games": [
        "Gaming Mouse",
        "Gaming Keyboard",
        "Gaming Headset",
        "Gaming Chair",
        "Gaming Console",
        "Video Game Controller",
        "Gaming Laptop",
        "Gaming Desk",
        "Gaming Monitor",
        "Gaming Mouse Pad",
        "Virtual Reality Gaming System",
        "Gaming Microphone",
        "Gaming Glasses",
        "Gaming Accessories Kit",
        "Gaming Storage Tower",
        "Video Games Collection",
        "Gaming Capture Card",
        "Gaming Speakers",
        "Gaming Router",
        "Gaming Merchandise",
    ],
    "Musical Instruments": [
        "Guitar",
        "Keyboard",
        "Drum Set",
        "Violin",
        "Saxophone",
        "Trumpet",
        "Flute",
        "Piano",
        "Acoustic Guitar",
        "Electric Bass",
        "Clarinet",
        "Cello",
        "Mandolin",
        "Banjo",
        "Harp",
        "Accordion",
        "Ukulele",
        "Djembe",
        "Synthesizer",
        "Microphone",
    ],
    "Industrial and Scientific": [
        "Lab Equipment",
        "Microscope",
        "Centrifuge",
        "Chemistry Set",
        "Safety Goggles",
        "Laboratory Glassware",
        "Industrial Scale",
        "Lab Coats",
        "Safety Gloves",
        "Safety Boots",
        "Calipers",
        "Thermocouples",
        "Industrial Fans",
        "Soldering Iron",
        "Digital Multimeter",
        "Bunsen Burner",
        "Electronic Components",
        "Laboratory Refrigerator",
        "Fume Hood",
        "Lab Bench",
    ],
    "Arts, Crafts, and Sewing": [
        "Paint Set",
        "Sketchbooks",
        "Canvas",
        "Watercolor Brushes",
        "Sewing Machine",
        "Knitting Needles",
        "Crochet Hooks",
        "Quilting Fabric",
        "Scissors",
        "Art Easels",
        "Acrylic Paints",
        "Oil Paints",
        "Colored Pencils",
        "Craft Glue",
        "Craft Paper",
        "Embroidery Thread",
        "Beads and Jewelry Making Kits",
        "Fabric Markers",
        "Sewing Patterns",
        "Art Apron",
    ],
}
# List of common male first names
male_names = [
    "John",
    "Robert",
    "Michael",
    "William",
    "David",
    "Richard",
    "Joseph",
    "Charles",
    "Thomas",
    "Christopher",
    "Daniel",
    "Paul",
    "Mark",
    "Donald",
    "George",
    "Kenneth",
    "Steven",
    "Edward",
    "Brian",
    "Ronald",
    "Anthony",
    "Kevin",
    "Jason",
    "Matthew",
    "Gary",
    "Timothy",
    "Jose",
    "Larry",
    "Jeffrey",
    "Frank",
    "Scott",
    "Eric",
    "Stephen",
    "Andrew",
    "Raymond",
    "Gregory",
    "Joshua",
    "Jerry",
    "Dennis",
    "Walter",
    "Patrick",
    "Peter",
    "Harold",
    "Douglas",
    "Henry",
    "Carl",
    "Arthur",
    "Ryan",
    "Roger",
    "Joe",
    "Juan",
    "Jack",
    "Albert",
    "Jonathan",
    "Justin",
    "Terry",
    "Gerald",
    "Keith",
    "Samuel",
    "Willie",
    "Ralph",
    "Lawrence",
    "Nicholas",
    "Roy",
    "Benjamin",
    "Bruce",
    "Brandon",
    "Adam",
    "Harry",
    "Fred",
    "Wayne",
    "Billy",
    "Steve",
    "Louis",
    "Jeremy",
    "Aaron",
    "Randy",
    "Howard",
    "Eugene",
    "Carlos",
    "Russell",
    "Bobby",
    "Victor",
    "Martin",
    "Ernest",
    "Phillip",
    "Todd",
    "Jesse",
    "Craig",
    "Alan",
    "Shawn",
    "Clarence",
    "Sean",
    "Philip",
    "Chris",
    "Johnny",
    "Earl",
    "Jimmy",
    "Antonio",
    "Danny",
]
# List of common female first names
female_names = [
    "Mary",
    "Patricia",
    "Jennifer",
    "Linda",
    "Elizabeth",
    "Barbara",
    "Susan",
    "Jessica",
    "Sarah",
    "Karen",
    "Nancy",
    "Lisa",
    "Margaret",
    "Betty",
    "Dorothy",
    "Sandra",
    "Ashley",
    "Kimberly",
    "Donna",
    "Emily",
    "Michelle",
    "Carol",
    "Amanda",
    "Melissa",
    "Deborah",
    "Stephanie",
    "Rebecca",
    "Laura",
    "Sharon",
    "Cynthia",
    "Kathleen",
    "Helen",
    "Amy",
    "Shirley",
    "Angela",
    "Frances",
    "Anna",
    "Ruth",
    "Virginia",
    "Brenda",
    "Pamela",
    "Catherine",
    "Debra",
    "Janet",
    "Carolyn",
    "Renee",
    "Kathryn",
    "Lori",
    "Tiffany",
    "Connie",
    "Victoria",
    "Evelyn",
    "Grace",
    "Diane",
    "Alice",
    "Julie",
    "Heather",
    "Teresa",
    "Doris",
    "Gloria",
    "Judy",
    "Mildred",
    "Denise",
    "Jane",
    "Martha",
    "Andrea",
    "Sara",
    "Jacqueline",
    "Ann",
    "Wanda",
    "Bonnie",
    "Julia",
    "Ruby",
    "Lois",
    "Tina",
    "Phyllis",
    "Norma",
    "Paula",
    "Diana",
    "Annie",
    "Lillian",
    "Emily",
    "Robin",
    "Peggy",
    "Crystal",
    "Gladys",
    "Rita",
    "Dawn",
    "Connie",
    "Fannie",
    "Holly",
    "Erin",
    "April",
    "Kristen",
    "Pauline",
]
# List of common last names
last_names = [
    "Smith",
    "Johnson",
    "Brown",
    "Davis",
    "Wilson",
    "Moore",
    "Taylor",
    "Anderson",
    "Thomas",
    "Jackson",
    "White",
    "Harris",
    "Martin",
    "Thompson",
    "Garcia",
    "Martinez",
    "Robinson",
    "Clark",
    "Rodriguez",
    "Lewis",
    "Lee",
    "Walker",
    "Hall",
    "Allen",
    "Young",
    "Hernandez",
    "King",
    "Wright",
    "Lopez",
    "Hill",
    "Scott",
    "Green",
    "Adams",
    "Baker",
    "Nelson",
    "Carter",
    "Mitchell",
    "Perez",
    "Roberts",
    "Turner",
    "Phillips",
    "Campbell",
    "Parker",
    "Evans",
    "Edwards",
    "Collins",
    "Stewart",
    "Sanchez",
    "Morris",
    "Rogers",
    "Reed",
    "Cook",
    "Morgan",
    "Bell",
    "Murphy",
    "Bailey",
    "Rivera",
    "Cooper",
    "Richardson",
    "Cox",
    "Howard",
    "Ward",
    "Torres",
    "Peterson",
    "Gray",
    "Ramirez",
    "James",
    "Watson",
    "Brooks",
    "Kelly",
    "Sanders",
    "Price",
    "Bennett",
    "Wood",
    "Barnes",
    "Ross",
    "Henderson",
    "Coleman",
    "Jenkins",
    "Perry",
    "Powell",
    "Long",
    "Patterson",
    "Hughes",
    "Flores",
    "Washington",
    "Butler",
    "Simmons",
    "Foster",
    "Gonzales",
    "Bryant",
    "Alexander",
    "Russell",
    "Griffin",
    "Diaz",
    "Hayes",
    "Myers",
    "Ford",
    "Hamilton",
    "Graham",
    "Sullivan",
    "Wallace",
]
# Dictionary mapping country codes to latitude ranges
country_latitudes = {
    "US": (24.396308, 49.384358),  # Contiguous United States
    "UK": (49.91224, 58.635),  # United Kingdom
    "Canada": (41.681982, 83.110626),  # Canada
    "Australia": (-43.634597, -10.668185),  # Australia
    "Germany": (47.270111, 55.056482),
    "France": (41.303, 51.124),
    "Japan": (24.396308, 45.551483),
    "China": (18.159073, 53.560815),
    "India": (8.076, 37.084),
    "Brazil": (-33.751667, 5.272222),
    "Russia": (41.198476, 81.858),
    "South Africa": (-34.834019, -17.589844),
    "Mexico": (14.534472, 32.718711),
    "Italy": (35.813081, 47.092),  # Approximate mainland Italy
    "Spain": (27.498, 43.791),
    "South Korea": (33.19, 38.625),
    "Saudi Arabia": (16.347, 32.159),
    "Argentina": (-55.051667, -21.781111),
    "Turkey": (35.8131, 42.107),
    "Netherlands": (50.77083, 53.359167),
    "Sweden": (55.34, 69.07),
    "Switzerland": (45.818, 47.81),
    "Singapore": (1.258, 1.478),
    "New Zealand": (-47.3, -33.6),
    "Norway": (57.885, 71.19),
    "Denmark": (54.57, 57.74),
    "Ireland": (51.427, 55.385),
    "Finland": (59.808, 70.095),
    "Austria": (46.372, 49.012),
    "Belgium": (49.497, 51.505),
    "Portugal": (36.959, 42.141),
    "Greece": (35.81, 41.748)
    # Add more countries and latitude ranges as needed
}
# Dictionary mapping country codes to longitude ranges
country_longitudes = {
    "US": (-125.000000, -66.934570),  # Contiguous United States
    "UK": (-8.646362, 1.763306),  # United Kingdom
    "Canada": (-141.000000, -52.617390),  # Canada
    "Australia": (112.921112, 153.6349),  # Australia
    "Germany": (5.988659, 15.016995),
    "France": (-5.453, 9.561),
    "Japan": (122.934570, 153.986672),
    "China": (73.502519, 135.000000),
    "India": (68.186, 97.416),
    "Brazil": (-73.982226, -34.729444),
    "Russia": (-168.534159, 169.039551),
    "South Africa": (16.344452, 32.891960),
    "Mexico": (-117.12771, -86.590573),
    "Italy": (6.6193, 18.540),  # Approximate mainland Italy
    "Spain": (-18.167, 4.327),
    "South Korea": (125.887, 129.583),
    "Saudi Arabia": (34.495, 55.668),
    "Argentina": (-73.582778, -53.637222),
    "Turkey": (25.813, 44.79),
    "Netherlands": (3.358333, 7.210833),
    "Sweden": (11.11, 24.17),
    "Switzerland": (5.957, 10.491),
    "Singapore": (103.638, 104.072),
    "New Zealand": (166.464, 178.841),
    "Norway": (4.992, 31.03),
    "Denmark": (7.43, 15.12),
    "Ireland": (-10.477, -5.414),
    "Finland": (20.645, 31.586),
    "Austria": (9.535, 17.166),
    "Belgium": (2.54, 6.408),
    "Portugal": (-9.492, -6.19),
    "Greece": (20.869, 29.65)
    # Add more countries and longitude ranges as needed
}
# List of company name prefixes
company_prefix = [
    "secure",
    "premium",
    "delux",
    "innovative",
    "creative",
    "techno",
    "global",
    "dynamic",
    "synergistic",
    "stellar",
    "exquisite",
    "elite",
    "ultimate",
    "visionary",
    "pinnacle",
    "vibrant",
    "profound",
    "paragon",
    "zenith",
    "prime",
    "stellar",
    "supreme",
    "elegant",
    "quantum",
    "infinity",
    "excellent",
    "majestic",
    "efficiency",
    "harmony",
    "splendid",
    "superior",
    "inspire",
    "insight",
    "integral",
    "luminous",
    "fusion",
    "radiant",
    "evolve",
    "accelerate",
    "innate",
    "innovation",
    "excellence",
    "embrace",
    "prosperity",
    "forge",
    "synergy",
    "catalyst",
    "spectrum",
    "horizon",
    "unison",
    "integrity",
    "precision",
    "transcend",
    "illuminate",
    "noble",
    "zen",
    "velocity",
    "synergy",
    "grandeur",
    "genesis",
    "effulgent",
    "harmonic",
    "quantum",
    "resonance",
    "stellar",
    "invincible",
    "intrepid",
    "innate",
    "stellar",
    "supreme",
    "eclipse",
    "rhapsody",
    "vanguard",
    "purity",
    "virtue",
    "equilibrium",
    "evolve",
    "integrity",
    "luminous",
    "triumph",
    "prosper",
    "zenith",
    "synergy",
    "vivid",
    "integral",
]
# List of company name suffixes
company_suffix = [
    "tech",
    "metal",
    "chemical",
    "services",
    "solutions",
    "pharmaceuticals",
    "machineries",
    "automotive",
    "glass",
    "woodworks",
    "systems",
    "networks",
    "solutions",
    "enterprises",
    "industries",
    "ventures",
    "technologies",
    "dynamics",
    "concepts",
    "innovations",
    "consulting",
    "labs",
    "group",
    "mechanics",
]
# List of words for generating email addresses (email_1)
email_1 = [
    "beautiful",
    "opera",
    "sunshine",
    "desert",
    "rock",
    "rhythm",
    "ocean",
    "tulip",
    "norwester",
    "mew",
    "love",
]
# List of words for generating email addresses (email_2)
email_2 = [
    "xoxo",
    "story",
    "poetry",
    "water",
    "fire",
    "abc",
    "findme",
    "lighthouse",
    "glasswall",
    "silk",
    "heaven",
]
# List of words for generating email addresses (email_3)
email_3 = ["a2z", "1010", "1996", "mozzarella", "x", "80s", "work", "uni"]
# List of default department names
default_departments = [
    "Marketing",
    "Sales",
    "Finance",
    "IT",
    "Operations",
    "Procurement",
    "Accounts",
    "HR",
    "Customer Service",
    "Research and Development",
    "Quality Assurance",
    "Legal",
    "Public Relations",
    "Supply Chain",
    "Engineering",
    "Product Management",
    "Health and Safety",
    "Training and Development",
    "Business Development",
    "Facilities Management",
    "Data Science",
]

# List of common words for generating passwords (password_words_1)
password_words_1 = [
    "apple",
    "david",
    "wowza",
    "happy",
    "banana",
    "chocolate",
    "abcdef",
    "asdfgh",
    "admin",
    "diamond",
    "eagle",
]
# List of common words and characters for generating passwords (password_words_2)
password_words_2 = [
    "123",
    "456",
    "password",
    "123456",
    "secret",
    "pass",
    "!",
    "@",
    "hello",
    "000",
    "000000",
    "sunshine",
]
# List of default industry categories
default_industry = [
    "Fashion and Retail",
    "Telecom",
    "Technology",
    "Automotive",
    "Media and Entertainment",
    "Healthcare",
    "Finance and Banking",
    "Energy and Utilities",
    "Hospitality and Tourism",
    "Food and Beverage",
    "Real Estate",
    "Education",
    "Aerospace",
    "Environmental",
    "Biotechnology",
    "Pharmaceuticals",
    "Logistics and Transportation",
    "Sports and Recreation",
    "Insurance",
    "Government and Public Services",
    "Consumer Goods",
    "Manufacturing",
    "Agriculture",
    "Information Technology",
    "E-commerce",
    "Consulting",
    "Marketing and Advertising",
    "Construction",
    "Nonprofit and Social Services",
    "Telecommunications",
    "Gaming",
    "Research and Development",
    "Space Exploration",
    "Fitness and Wellness",
    "Legal Services",
    "Art and Design",
    "Renewable Energy",
    "Robotics",
    "Artificial Intelligence",
    "Virtual Reality",
    "Augmented Reality",
    "Cybersecurity",
    "Blockchain",
    "Quantum Computing",
]
# List of default product categories
default_product_categories = [
    "Electronics",
    "Clothing",
    "Home and Kitchen",
    "Books",
    "Toys",
    "Beauty and Personal Care",
    "Sports and Outdoors",
    "Automotive",
    "Health and Household",
    "Tools and Home Improvement",
    "Grocery",
    "Pet Supplies",
    "Baby",
    "Office Products",
    "Jewelry",
    "Movies and TV",
    "Video Games",
    "Musical Instruments",
    "Industrial and Scientific",
    "Arts, Crafts, and Sewing",
]
