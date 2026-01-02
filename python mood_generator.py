import random
from datetime import datetime
import json
import os

class MoodCodeGenerator:
    def __init__(self):
        # Mood categories with their color representations
        self.moods = {
            "happy": {
                "colors": ["#FFD700", "#FFA500", "#FFFF00"],
                "symbols": ["☀️", "🌟", "😊", "🌈"],
                "codes": ["SUN", "GLOW", "JOY", "BEAM"]
            },
            "calm": {
                "colors": ["#87CEEB", "#98FB98", "#E6E6FA"],
                "symbols": ["🌊", "🌿", "☁️", "🕊️"],
                "codes": ["SERNE", "PEACE", "STILL", "CALM"]
            },
            "energetic": {
                "colors": ["#FF4500", "#FF6347", "#32CD32"],
                "symbols": ["⚡", "🔥", "🚀", "💥"],
                "codes": ["ZAP", "BURST", "SURGE", "POWER"]
            },
            "creative": {
                "colors": ["#9370DB", "#FF69B4", "#00CED1"],
                "symbols": ["🎨", "✨", "💡", "🦄"],
                "codes": ["INSP", "INNOV", "CREATE", "DREAM"]
            },
            "melancholy": {
                "colors": ["#708090", "#4682B4", "#6A5ACD"],
                "symbols": ["🌧️", "🌫️", "🌙", "🎵"],
                "codes": ["BLUE", "MIST", "ECHO", "SOUL"]
            },
            "focused": {
                "colors": ["#2F4F4F", "#008080", "#5F9EA0"],
                "symbols": ["🎯", "📊", "🔍", "⚙️"],
                "codes": ["FOCUS", "CLARITY", "PRECIS", "SHARP"]
            }
        }
        
        # Load previous moods if saved
        self.mood_history = self.load_mood_history()
    
    def generate_mood_code(self, selected_mood=None):
        """Generate a unique mood code based on current mood"""
        
        # If no mood is selected, pick a random one
        if not selected_mood or selected_mood.lower() not in self.moods:
            selected_mood = random.choice(list(self.moods.keys()))
        else:
            selected_mood = selected_mood.lower()
        
        mood_data = self.moods[selected_mood]
        
        # Generate components
        color = random.choice(mood_data["colors"])
        symbol = random.choice(mood_data["symbols"])
        base_code = random.choice(mood_data["codes"])
        
        # Add timestamp-based uniqueness
        timestamp = datetime.now().strftime("%H%M")
        mood_code = f"{base_code}-{timestamp}"
        
        # Create the full mood object
        mood_object = {
            "mood": selected_mood.capitalize(),
            "code": mood_code,
            "color": color,
            "symbol": symbol,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "rgb": self.hex_to_rgb(color)
        }
        
        # Add to history
        self.mood_history.append(mood_object)
        self.save_mood_history()
        
        return mood_object
    
    def hex_to_rgb(self, hex_color):
        """Convert hex color to RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def display_mood_code(self, mood_object):
        """Display the mood code with visual elements"""
        print("\n" + "="*50)
        print("🌻 YOUR MOOD CODE 🌻")
        print("="*50)
        
        # Create a simple color block
        color_block = f"\033[48;2;{mood_object['rgb'][0]};{mood_object['rgb'][1]};{mood_object['rgb'][2]}m    \033[0m"
        
        print(f"\nMood: {mood_object['mood']} {mood_object['symbol']}")
        print(f"Code: {mood_object['code']}")
        print(f"Color: {color_block} {mood_object['color']}")
        print(f"Time: {mood_object['timestamp']}")
        
        # Add a motivational message
        messages = {
            "Happy": "Your positivity is contagious! Keep shining! ✨",
            "Calm": "Peace is within you. Carry this serenity forward. 🕊️",
            "Energetic": "Channel that energy into something amazing! ⚡",
            "Creative": "The world needs your unique perspective. 🎨",
            "Melancholy": "Every feeling is valid. This too shall pass. 🌧️",
            "Focused": "Your concentration will lead to great things. 🎯"
        }
        
        print(f"\n{messages.get(mood_object['mood'], 'Embrace your current state.')}")
        print("="*50 + "\n")
    
    def get_mood_history(self, limit=5):
        """Retrieve recent mood history"""
        return self.mood_history[-limit:] if self.mood_history else []
    
    def display_mood_history(self):
        """Display recent mood history"""
        history = self.get_mood_history(10)
        
        if not history:
            print("\nNo mood history found. Generate some moods first!")
            return
        
        print("\n" + "="*50)
        print("📓 YOUR MOOD HISTORY 📓")
        print("="*50)
        
        for i, mood in enumerate(reversed(history), 1):
            print(f"{i}. {mood['timestamp']} - {mood['mood']} {mood['symbol']} - {mood['code']}")
        
        print("="*50 + "\n")
    
    def save_mood_history(self):
        """Save mood history to a file"""
        try:
            with open("mood_history.json", "w") as f:
                json.dump(self.mood_history, f, indent=2)
        except Exception as e:
            print(f"Could not save mood history: {e}")
    
    def load_mood_history(self):
        """Load mood history from a file"""
        try:
            if os.path.exists("mood_history.json"):
                with open("mood_history.json", "r") as f:
                    return json.load(f)
        except Exception as e:
            print(f"Could not load mood history: {e}")
        
        return []

def main():
    generator = MoodCodeGenerator()
    
    print("🌼 MOOD CODE GENERATOR 🌼")
    print("Generate a unique code representing your current emotional state!")
    
    while True:
        print("\nOptions:")
        print("1. Generate a random mood code")
        print("2. Select a specific mood")
        print("3. View mood history")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            mood = generator.generate_mood_code()
            generator.display_mood_code(mood)
            
        elif choice == "2":
            print("\nAvailable moods:")
            for i, mood in enumerate(generator.moods.keys(), 1):
                print(f"{i}. {mood.capitalize()}")
            
            try:
                mood_choice = int(input("\nSelect a mood (by number): "))
                mood_list = list(generator.moods.keys())
                
                if 1 <= mood_choice <= len(mood_list):
                    selected_mood = mood_list[mood_choice - 1]
                    mood = generator.generate_mood_code(selected_mood)
                    generator.display_mood_code(mood)
                else:
                    print("Invalid selection. Generating random mood instead.")
                    mood = generator.generate_mood_code()
                    generator.display_mood_code(mood)
                    
            except ValueError:
                print("Invalid input. Generating random mood instead.")
                mood = generator.generate_mood_code()
                generator.display_mood_code(mood)
                
        elif choice == "3":
            generator.display_mood_history()
            
        elif choice == "4":
            print("\nThank you for using the Mood Code Generator!")
            print("Remember: All feelings are valid. Take care! 🌈\n")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
