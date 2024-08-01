import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Chatbot")

# Create the chat display
chat_display = tk.Text(root, height=20, width=50)
chat_display.pack()

# Create the entry box for user input
user_input = tk.Entry(root, width=50)
user_input.pack()

# Function to handle user input and display bot response
def send_message():
    message = user_input.get()
    chat_display.insert(tk.END, "You: " + message + "\n")
    
    # Classify intent and get the response
    intent = classify_intent(message)
    response = get_response(intent)
    chat_display.insert(tk.END, "Bot: " + response + "\n")
    
    user_input.delete(0, tk.END)

# Bind the Enter key to the send_message function
user_input.bind("<Return>", lambda event: send_message())

# Create the send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Run the Tkinter main loop
root.mainloop()
