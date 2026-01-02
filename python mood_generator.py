import random
from datetime import datetime

class MoodCodeGenerator:
    def __init__(self):
        self.moods = {
            "happy": {"colors": ["#FFD700", "#FFA500"], "symbols": ["☀️", "😊"], "codes": ["SUN", "JOY"]},
            "calm": {"colors": ["#87CEEB", "#98FB98"], "symbols": ["🌊", "☁️"], "codes": ["PEACE", "CALM"]},
            "energetic": {"colors": ["#FF4500", "#32CD32"], "symbols": ["⚡", "🔥"], "codes": ["ZAP", "POWER"]},
            "creative": {"colors": ["#9370DB", "#FF69B4"], "symbols": ["🎨", "💡"], "codes": ["INSP", "CREATE"]}
        }
    
    def generate(self, selected=None):
        selected = selected if selected in self.moods else random.choice(list(self.moods.keys()))
        mood = self.moods[selected]
        
        code = f"{random.choice(mood['codes'])}-{datetime.now().strftime('%H%M')}"
        color = random.choice(mood['colors'])
        symbol = random.choice(mood['symbols'])
        
        return {
            "mood": selected.upper(),
            "code": code,
            "color": color,
            "symbol": symbol,
            "time": datetime.now().strftime("%H:%M")
        }
    
    def display(self, mood):
        print(f"\n{'='*40}")
        print(f"🌟 MOOD CODE: {mood['code']}")
        print(f"{'='*40}")
        print(f"Mood: {mood['mood']} {mood['symbol']}")
        print(f"Color: {mood['color']}")
        print(f"Time: {mood['time']}")
        print(f"{'='*40}")

def main():
    gen = MoodCodeGenerator()
    
    print("🌼 MOOD CODE GENERATOR 🌼")
    
    while True:
        print("\n1. Random Mood")
        print("2. Choose Mood")
        print("3. Exit")
        
        choice = input("\nChoice (1-3): ")
        
        if choice == "1":
            mood = gen.generate()
            gen.display(mood)
        elif choice == "2":
            print("\nAvailable moods:")
            for i, m in enumerate(gen.moods.keys(), 1):
                print(f"{i}. {m.capitalize()}")
            
            try:
                idx = int(input("\nSelect (1-4): ")) - 1
                moods_list = list(gen.moods.keys())
                if 0 <= idx < len(moods_list):
                    mood = gen.generate(moods_list[idx])
                    gen.display(mood)
                else:
                    print("Invalid! Random mood:")
                    mood = gen.generate()
                    gen.display(mood)
            except:
                print("Invalid! Random mood:")
                mood = gen.generate()
                gen.display(mood)
        elif choice == "3":
            print("\n🌈 Keep shining! Goodbye! 🌈")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
