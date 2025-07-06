import asyncio
import sys
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import uuid

# MongoDB Atlas connection
# Replace this with your actual MongoDB Atlas connection string
MONGO_URL = "mongodb+srv://username:password@cluster.mongodb.net/portfolio?retryWrites=true&w=majority"
DB_NAME = "portfolio"

# Project data for Owen Roth's portfolio
projects_data = [
    # Web Services
    {
        "id": str(uuid.uuid4()),
        "title": "Social Media (Google Drive)",
        "description": "Most of the backend is Python, with frontend using HTML and JavaScript. This is code for a site generator that can create static pages, server-side dynamic pages, and client-side dynamic pages. Implements dynamic layout management along with many of Instagram's features. It achieves this using JavaScript programming, asynchronous programming (AJAX), and REST APIs. This is both code for a website and the backend.",
        "category": "Web Services",
        "technologies": ["Python", "HTML", "JavaScript", "AJAX", "REST API"],
        "github_url": "https://github.com/owenroth/social-media-google-drive",
        "google_drive_url": None,
        "demo_url": None,
        "image_url": None,
        "featured": True,
        "created_at": datetime.utcnow()
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Wikipedia Search Engine (Google Drive)",
        "description": "This is the code for a scalable search engine that scours Wikipedia pages and returns pages based on the input. This search engine automatically filters (PageRank) and parallel data processing with MapReduce to return the best results. This is both code for a webpage and the backend.",
        "category": "Web Services",
        "technologies": ["Python", "MapReduce", "PageRank", "Search Algorithms"],
        "github_url": "https://github.com/owenroth/wikipedia-search-engine",
        "google_drive_url": None,
        "demo_url": None,
        "image_url": None,
        "featured": True,
        "created_at": datetime.utcnow()
    },
    {
        "id": str(uuid.uuid4()),
        "title": "iTunes Artist Search (GitHub)",
        "description": "This was made in JavaScript and HTML. This is a simple website I made using iTunes HTML to try and practice web interface. This website allows the user to search the iTunes platform with sorting and filtering options. It also allows the user to play samples and leave reviews to practice website development.",
        "category": "Web Services",
        "technologies": ["JavaScript", "HTML", "iTunes API"],
        "github_url": "https://github.com/owenroth/itunes-artist-search",
        "google_drive_url": None,
        "demo_url": None,
        "image_url": None,
        "featured": False,
        "created_at": datetime.utcnow()
    },
    
    # Game Development
    {
        "id": str(uuid.uuid4()),
        "title": "Metroid (Unity Remaster) (itch.io)",
        "description": "This is a recreation of Metroid with a new mechanic. I was responsible for implementing all of the enemies, health, collectibles, doors, the custom mechanic, and the level. Additionally, I authored the research piece on the custom mechanic and level design.",
        "category": "Game Development",
        "technologies": ["Unity", "C#", "Game Design"],
        "github_url": None,
        "google_drive_url": None,
        "demo_url": "https://owenroth.itch.io/metroid-remaster",
        "image_url": None,
        "featured": True,
        "created_at": datetime.utcnow()
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Project Z Gold Spike (itch.io)",
        "description": "This is a game with a novel mechanic created during a timed development project. This is an improved version of the same game, polished after peer feedback. However, it was still implemented within a tight timeline.",
        "category": "Game Development",
        "technologies": ["Unity", "C#", "Game Mechanics"],
        "github_url": None,
        "google_drive_url": None,
        "demo_url": "https://owenroth.itch.io/project-z-gold-spike",
        "image_url": None,
        "featured": False,
        "created_at": datetime.utcnow()
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Project 3 Gold (itch.io)",
        "description": "This is a roguelike infinite runner-style game made by a group of three students over the course of a month. I was responsible for implementing the endless enemies, collectibles, miscellaneous sprites, game balancing, and fine tuning. I also helped my partners with bug fixes in their sections. Videos of the game can also be found at the link.",
        "category": "Game Development",
        "technologies": ["Unity", "C#", "Roguelike", "Game Balancing"],
        "github_url": None,
        "google_drive_url": None,
        "demo_url": "https://owenroth.itch.io/project-3-gold",
        "image_url": None,
        "featured": True,
        "created_at": datetime.utcnow()
    },
    
    # Miscellaneous
    {
        "id": str(uuid.uuid4()),
        "title": "NBA Allstar Database (GitHub)",
        "description": "This was mostly made in Python. This is a simple API project that retrieves data from multiple APIs and stored it in an SQL database. I then created a table joining information from the different sources and added new values based on calculations derived from the original information. Visuals were also created to further understand the information.",
        "category": "Miscellaneous",
        "technologies": ["Python", "SQL", "API Integration", "Data Visualization"],
        "github_url": "https://github.com/owenroth/nba-allstar-database",
        "google_drive_url": None,
        "demo_url": None,
        "image_url": None,
        "featured": False,
        "created_at": datetime.utcnow()
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Discord Bot (GitHub)",
        "description": "This was made in JavaScript. This was a simple Discord Bot I created for my little brother and his friends with various commands. Many of the commands scrape information from a website to display video game stats, as there really is not any public API to use. There are also some simpler commands similar to prior request.",
        "category": "Miscellaneous",
        "technologies": ["JavaScript", "Discord API", "Web Scraping"],
        "github_url": "https://github.com/owenroth/discord-bot",
        "google_drive_url": None,
        "demo_url": None,
        "image_url": None,
        "featured": False,
        "created_at": datetime.utcnow()
    }
]

async def populate_atlas_database():
    """
    Populate MongoDB Atlas with portfolio projects
    
    Before running this script:
    1. Update the MONGO_URL with your actual MongoDB Atlas connection string
    2. Make sure you have motor installed: pip install motor
    """
    
    if "username:password" in MONGO_URL:
        print("❌ ERROR: Please update the MONGO_URL with your actual MongoDB Atlas connection string!")
        print("   Replace 'username:password' with your actual MongoDB Atlas credentials")
        print("   Example: mongodb+srv://myuser:mypass@cluster.mongodb.net/portfolio?retryWrites=true&w=majority")
        return
    
    try:
        print("🔄 Connecting to MongoDB Atlas...")
        client = AsyncIOMotorClient(MONGO_URL)
        db = client[DB_NAME]
        
        # Test connection
        await client.server_info()
        print("✅ Successfully connected to MongoDB Atlas!")
        
        # Clear existing projects
        print("🔄 Clearing existing projects...")
        await db.projects.delete_many({})
        
        # Insert new projects
        print("🔄 Inserting portfolio projects...")
        await db.projects.insert_many(projects_data)
        
        print(f"✅ Successfully populated {len(projects_data)} projects!")
        
        # Print summary
        categories = {}
        for project in projects_data:
            category = project['category']
            if category not in categories:
                categories[category] = 0
            categories[category] += 1
        
        print("\n📊 Project summary by category:")
        for category, count in categories.items():
            print(f"   {category}: {count} projects")
        
        print("\n🎉 Database setup complete! Your portfolio is ready for deployment.")
            
    except Exception as e:
        print(f"❌ Error populating MongoDB Atlas: {e}")
        print("\nTroubleshooting tips:")
        print("1. Check your MongoDB Atlas connection string")
        print("2. Ensure your IP address is whitelisted (0.0.0.0/0)")
        print("3. Verify your MongoDB Atlas credentials")
        print("4. Make sure your cluster is running")
    finally:
        if 'client' in locals():
            client.close()

if __name__ == "__main__":
    print("🚀 MongoDB Atlas Database Setup for Owen Roth's Portfolio")
    print("=" * 60)
    asyncio.run(populate_atlas_database())