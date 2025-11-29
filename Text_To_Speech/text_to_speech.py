"""
Text to Speech - A simple text to speech converter
Uses pyttsx3 library for offline TTS
"""


class TextToSpeech:
    """Text to Speech converter class."""

    def __init__(self, engine_type="offline"):
        """Initialize the TTS engine."""
        self.engine_type = engine_type
        self.engine = None
        self.rate = 150  # Default speech rate
        self.volume = 1.0  # Default volume
        self.voice_id = 0  # Default voice
        self._initialize_engine()

    def _initialize_engine(self):
        """Initialize the appropriate TTS engine."""
        if self.engine_type == "offline":
            try:
                import pyttsx3
                self.engine = pyttsx3.init()
                self.engine.setProperty('rate', self.rate)
                self.engine.setProperty('volume', self.volume)
                voices = self.engine.getProperty('voices')
                if voices:
                    self.engine.setProperty('voice', voices[self.voice_id].id)
            except ImportError:
                print("pyttsx3 not installed. Install with: pip install pyttsx3")
                self.engine = None

    def speak(self, text):
        """Convert text to speech and play it."""
        if not text.strip():
            return False, "No text provided."

        if self.engine is None:
            return False, "TTS engine not initialized."

        try:
            self.engine.say(text)
            self.engine.runAndWait()
            return True, "Speech completed."
        except Exception as e:
            return False, f"Error during speech: {str(e)}"

    def save_to_file(self, text, filename):
        """Save speech to an audio file."""
        if not text.strip():
            return False, "No text provided."

        if self.engine is None:
            return False, "TTS engine not initialized."

        try:
            if not filename.endswith('.mp3'):
                filename += '.mp3'
            self.engine.save_to_file(text, filename)
            self.engine.runAndWait()
            return True, f"Audio saved to {filename}"
        except Exception as e:
            return False, f"Error saving audio: {str(e)}"

    def set_rate(self, rate):
        """Set speech rate (words per minute)."""
        if rate < 50 or rate > 300:
            return False, "Rate must be between 50 and 300."
        self.rate = rate
        if self.engine:
            self.engine.setProperty('rate', rate)
        return True, f"Speech rate set to {rate} wpm."

    def set_volume(self, volume):
        """Set speech volume (0.0 to 1.0)."""
        if volume < 0.0 or volume > 1.0:
            return False, "Volume must be between 0.0 and 1.0."
        self.volume = volume
        if self.engine:
            self.engine.setProperty('volume', volume)
        return True, f"Volume set to {volume*100:.0f}%."

    def list_voices(self):
        """List available voices."""
        if self.engine is None:
            return False, "TTS engine not initialized."

        try:
            voices = self.engine.getProperty('voices')
            result = []
            for i, voice in enumerate(voices):
                result.append(f"{i}. {voice.name}")
            return True, "\n".join(result)
        except Exception as e:
            return False, str(e)

    def set_voice(self, voice_id):
        """Set the voice by ID."""
        if self.engine is None:
            return False, "TTS engine not initialized."

        try:
            voices = self.engine.getProperty('voices')
            if 0 <= voice_id < len(voices):
                self.voice_id = voice_id
                self.engine.setProperty('voice', voices[voice_id].id)
                return True, f"Voice set to: {voices[voice_id].name}"
            return False, "Invalid voice ID."
        except Exception as e:
            return False, str(e)

    def get_settings(self):
        """Get current TTS settings."""
        return {
            "rate": self.rate,
            "volume": self.volume,
            "voice_id": self.voice_id,
            "engine_type": self.engine_type
        }


def main():
    """Main function to run the TTS application."""
    print("=" * 50)
    print("       Welcome to Text to Speech")
    print("=" * 50)

    # Try to initialize TTS
    tts = TextToSpeech()

    if tts.engine is None:
        print("\n⚠️  pyttsx3 is not installed.")
        print("Install it with: pip install pyttsx3")
        print("\nRunning in demo mode (no actual speech)...")

    while True:
        print("\n" + "-" * 50)
        print("1. Speak Text")
        print("2. Save to Audio File")
        print("3. List Available Voices")
        print("4. Change Voice")
        print("5. Adjust Speech Rate")
        print("6. Adjust Volume")
        print("7. View Current Settings")
        print("8. Exit")
        print("-" * 50)

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            text = input("Enter text to speak: ")
            if tts.engine:
                print("🔊 Speaking...")
                success, msg = tts.speak(text)
                print(msg)
            else:
                print(f"Demo: Would speak: '{text}'")

        elif choice == "2":
            text = input("Enter text to save: ")
            filename = input("Enter filename (without extension): ")
            if tts.engine:
                success, msg = tts.save_to_file(text, filename)
                print(msg)
            else:
                print(f"Demo: Would save '{text}' to {filename}.mp3")

        elif choice == "3":
            if tts.engine:
                success, msg = tts.list_voices()
                print("\n🎤 Available Voices:")
                print(msg)
            else:
                print("Demo: Voice listing not available")

        elif choice == "4":
            try:
                voice_id = int(input("Enter voice ID: "))
                if tts.engine:
                    success, msg = tts.set_voice(voice_id)
                    print(msg)
                else:
                    print(f"Demo: Would set voice to ID {voice_id}")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "5":
            try:
                rate = int(input("Enter speech rate (50-300 wpm): "))
                success, msg = tts.set_rate(rate)
                print(msg)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "6":
            try:
                volume = float(input("Enter volume (0.0-1.0): "))
                success, msg = tts.set_volume(volume)
                print(msg)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "7":
            settings = tts.get_settings()
            print("\n⚙️ Current Settings:")
            print(f"   Rate: {settings['rate']} wpm")
            print(f"   Volume: {settings['volume']*100:.0f}%")
            print(f"   Voice ID: {settings['voice_id']}")
            print(f"   Engine: {settings['engine_type']}")

        elif choice == "8":
            print("\nThank you for using Text to Speech. Goodbye! 🔊")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
