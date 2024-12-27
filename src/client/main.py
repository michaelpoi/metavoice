from tkinter import Tk, Text, Button, Scrollbar, Entry, END, PhotoImage
from client.cur_assistant import voice_assistant
from assistant.listener import get_voice_input
import threading

class VoiceAssistantChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant Chat Interface")

        self.server_thread = None
        self.stop_server = False
        #self.root.geometry('1200x800')

        # Chat display configuration
        self.chat_display = Text(self.root,wrap='none', height=20, width=50)
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.chat_display.configure(state="disabled")

        # Scrollbar for chat display
        self.scrollbar = Scrollbar(self.root, command=self.chat_display.yview)
        self.x_scrollbar = Scrollbar(self.root, command=self.chat_display.xview, orient='horizontal')
        self.chat_display.configure(yscrollcommand=self.scrollbar.set)
        self.chat_display.configure(xscrollcommand=self.x_scrollbar.set)
        self.scrollbar.grid(row=0, column=2, sticky="ns")
        self.x_scrollbar.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10)


        # Entry box for user text input
        self.entry_box = Entry(self.root, width=40)
        self.entry_box.grid(row=2, column=0, padx=10, pady=10)

        # Send button for text commands
        self.send_icon = PhotoImage(file='assets/arrow.png').subsample(8, 8)
        self.send_button = Button(self.root, image=self.send_icon, command=self.process_text_command)
        self.send_button.grid(row=2, column=1, padx=5, pady=10)

        # Create and resize microphone icon
        self.microphone_icon = PhotoImage(file="assets/micro.png").subsample(8, 8)  # Resize the icon
        
        # Microphone button for audio input
        self.microphone_button = Button(self.root, image=self.microphone_icon, command=self.get_audio_input)
        self.microphone_button.grid(row=2, column=2, padx=3, pady=10)
        
        # Cancel Microphone button, hidden by default
        self.cancel_microphone_icon = PhotoImage(file="assets/stop.png").subsample(4, 4)  # Resize the icon
        self.cancel_microphone_button = Button(self.root, image=self.cancel_microphone_icon, command=self.cancel_microphone_input)
        self.cancel_microphone_button.grid(row=2, column=2, padx=5, pady=10)
        self.cancel_microphone_button.grid_remove()

    def process_text_command(self):
        user_input = self.entry_box.get()
        if user_input.strip():
            self.chat_display.configure(state="normal")
            self.chat_display.insert(END, f"You: {user_input}\n")
            response = voice_assistant.process_command(user_input)
            self.chat_display.insert(END, f"Voice Assistant: {response}\n")
            self.chat_display.configure(state="disabled")
            self.entry_box.delete(0, END)

    def cancel_microphone_input(self):
        # Hide Cancel Microphone button and show Microphone button
        self.cancel_microphone_button.grid_remove()
        self.microphone_button.grid()
        self.send_button.configure(state="normal")

        self.stop_server = True
        self.server_thread.join()
    
        # Re-enable Text area
        self.chat_display.configure(state="normal")
    
        # Add cancellation message in chat display
        self.chat_display.insert(END, "Voice Assistant: [Voice input canceled]\n")
        self.chat_display.configure(state="disabled")

    def reinit_thread(self):
        self.server_thread = threading.Thread(target=self.serve_ui)

    def get_audio_input(self):
        self.microphone_button.grid_remove()
        self.cancel_microphone_button.grid()
        self.send_button.configure(state="disabled")
    
        # Disable Text area
        self.chat_display.configure(state="disabled")

        # Add processing message in chat display
        self.chat_display.configure(state="normal")
        # text = get_voice_input()
        # output = None
        # if text:
        #     self.chat_display.insert(END, f"You: {text}\n")
        #     output = voice_assistant.process_command(text)
        #     self.chat_display.insert(END, f"Voice Assistant: {output}\n")

        self.reinit_thread()
        self.server_thread.start()

        #self.microphone_button.configure(state="normal")
        self.send_button.configure(state="normal")

    def serve_ui(self):
        while True:
            text = get_voice_input()
            output = None
            if self.stop_server:
                print("Thread stopped")
                self.stop_server = False
                break
            if text:
                self.chat_display.insert(END, f"You: {text}\n")
                output = voice_assistant.process_command(text)
                self.chat_display.insert(END, f"Voice Assistant: {output}\n")


if __name__ == "__main__":
    root = Tk()
    app = VoiceAssistantChatApp(root)
    root.mainloop()