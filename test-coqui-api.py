from gradio_client import Client
import os

def generate_speech(text, reference_audio_path):
    # Initialize client
    client = Client("https://coqui-xtts.hf.space/--replicas/5891u/")
    
    # Ensure reference audio path exists and is accessible
    if not os.path.exists(reference_audio_path):
        raise FileNotFoundError(f"Reference audio file not found at: {reference_audio_path}")
    
    try:
        # Make prediction
        result = client.predict(
            text,                   # Text to convert to speech
            "en",                   # Language selection (simplified)
            reference_audio_path,   # Reference audio file path
            "",                     # No microphone input
            False,                  # Don't use microphone
            False,                  # Cleanup reference voice
            True,                   # Don't use language auto-detect
            True,                   # Agree to terms
            fn_index=1
        )
        return result
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    text = "Transformers, introduced in 2017, are sequence-to-sequence models that use self-attention to process input and output simultaneously, capturing long-range dependencies."
    reference_audio = "" # Iskobot url wav goes here
    result = generate_speech(text, reference_audio)
    if result:
        print(f"Speech generated successfully. Output: {result}")