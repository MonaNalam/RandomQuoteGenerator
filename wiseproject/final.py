import tkinter as tk
import random
import sqlite3
connection = sqlite3.connect("quotations.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS quotations (
                    category TEXT,
                    quotation TEXT
                )''')

quotations = {
    "Sad": [
        "The way sadness works is one of the strange riddles of the world. – Lemony Snicket",
        "Behind every sweet smile, there is a bitter sadness that no one can see and feel. – Tupac Shakur",
        "Tears are words that need to be written. – Paulo Coelho",
        "The word 'happiness' would lose its meaning if it were not balanced by sadness. – Carl Jung",
        "Sadness flies away on the wings of time. – Jean de La Fontaine",
        "Sometimes you have to be your own hero.",
        "The scars you can't see are the hardest to heal.",
        "Pain changes people.",
        "When you can't look on the bright side, I will sit with you in the dark.",
    ],
    "Happy": [
        "The happiness of your life depends upon the quality of your thoughts. – Marcus Aurelius",
        "Happiness is not something ready-made. It comes from your own actions. – Dalai Lama",
        "The best way to cheer yourself up is to try to cheer somebody else up. – Mark Twain",
        "The only joy in the world is to begin. – Cesare Pavese",
        "The happiness of your life depends upon the quality of your thoughts. – Marcus Aurelius",
        "Every day is a new beginning.",
        "Life is short, smile while you still have teeth.",
        "Happiness is a choice.",
        "Don't worry, be happy!",
        "Happiness is homemade."
    ],
    "Motivational": [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
        "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
        "Opportunities don't happen. You create them. – Chris Grosser",
        "Don't be afraid to give up the good to go for the great. – John D. Rockefeller",
         "You are stronger than you think.",
        "Dream big and dare to fail.",
        "The harder you work for something, the greater you'll feel when you achieve it.",
        "Believe you can and you're halfway there.",
        "Success is not the key to happiness. Happiness is the key to success."
    ],
    "Love": [
        "The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves. – Victor Hugo",
        "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage. – Lao Tzu",
        "You know you're in love when you can't fall asleep because reality is finally better than your dreams. – Dr. Seuss",
        "To love and be loved is to feel the sun from both sides. – David Viscott",
        "Love is composed of a single soul inhabiting two bodies. – Aristotle",
        "The best thing to hold onto in life is each other.",
        "Love isn't something you find. Love is something that finds you.",
        "A true love story never ends.",
        "Love is all you need.",
        "You are my today and all of my tomorrows."
    ],
    "Funny": [
        "I am so clever that sometimes I don't understand a single word of what I am saying. – Oscar Wilde",
        "A day without sunshine is like, you know, night. – Steve Martin",
        "If at first you don't succeed, then skydiving definitely isn't for you. – Steven Wright",
        "I'm not lazy, I'm just on my energy-saving mode. – Unknown",
        "I told my wife she was drawing her eyebrows too high. She looked surprised. – Unknown",
        "I'm not clumsy, I'm just gravity-challenged.",
        "I'm on a seafood diet. I see food and I eat it.",
        "I'm not short, I'm vertically challenged.",
        "I put the 'pro' in procrastinate.",
        "I'm not arguing, I'm just explaining why I'm right."
    ]
}

def insert_quotations():
    for category, quotes in quotations.items():
        for quote in quotes:
            cursor.execute("INSERT INTO quotations (category, quotation) VALUES (?, ?)", (category, quote))
    connection.commit()

def retrieve_quotation(category):
    cursor.execute("SELECT quotation FROM quotations WHERE category=?", (category,))
    quotations = cursor.fetchall()
    if quotations:
        return random.choice(quotations)[0]
    else:
        return "No quotations found for this category."
    
def display_quotation(category):
    global quotation_window  
    if 'quotation_window' in globals() and quotation_window.winfo_exists():
        quotation_window.destroy()

    quotation_window = tk.Toplevel(root)
    quotation_window.title(category + " Quotation")
    quotation_window.geometry("400x200")
    quotation_window.configure(bg=button_colors[category])

    quotation = retrieve_quotation(category)
    quotation_label = tk.Label(quotation_window, text=quotation, wraplength=350, justify="center", font=("Helvetica", 12), bg=button_colors[category])
    quotation_label.pack(pady=20)

root = tk.Tk()
root.title("Random Quotation Generator")
root.geometry("800x500")

heading_label = tk.Label(root, text="Pick your choice", font=("Helvetica", 20))
heading_label.pack(pady=10)

button_colors = {
    "Sad": "lightgrey",
    "Happy": "lightblue",
    "Motivational": "orange",
    "Love": "lightpink",
    "Funny": "yellow"
}

insert_quotations()

cursor.execute("SELECT * FROM quotations")
print("Quotations in the database:")
for row in cursor.fetchall():
    print(row)

for category, color in button_colors.items():
    button = tk.Button(root, text=category, command=lambda cat=category: display_quotation(cat), width=15, height=2,
    bg=color, fg="black")
    button.pack(pady=5, padx=10, ipadx=10, ipady=10)

root.mainloop()