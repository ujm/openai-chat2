import openai
import sys
import os

def transcribe_audio(sound_path):
    # Open the audio file
    with open(sound_path, "rb") as audio_file:
        # Transcribe the audio file
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    # Format the transcript
    formatted_transcript = transcript["text"].replace("。", "。\n")
    print(f"Transcription:\n{formatted_transcript}")

    return transcript["text"]

def chat_with_gpt(initial_message):
    conversation = [{"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": initial_message}]

    while True:
        user_input = input("Your question: ")

        if user_input.lower() == "exit":
            print("Ending the chat.")
            break

        conversation.append({"role": "user", "content": user_input})

        # Limit conversation history to last 4 user messages
        conversation = conversation[-4:]

        # Get response from GPT-3.5-turbo model
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )

        # Print the summarized content
        print(f"GPT-3.5-turbo response:\n{completion.choices[0].message.content}\n")

if __name__ == "__main__":
    sound_path = sys.argv[1]
    initial_transcription = transcribe_audio(sound_path)
    chat_with_gpt(initial_transcription)
