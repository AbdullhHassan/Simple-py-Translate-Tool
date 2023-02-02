import tkinter as tk
import webbrowser
import requests

def translate_word(word, lang_pair):
    url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl={lang_pair[0]}&tl={lang_pair[1]}&dt=t&q={word}'
    result = requests.get(url)
    result = result.json()
    return result[0][0][0]

class TranslateWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("400x200")
        self.title("Translate Tool by Abdullah Hassan")

        self.entry = tk.Entry(self, width=80)
        self.entry.pack()
        self.entry.focus()
        self.entry.bind('<Return>', self.translate)

        self.text = tk.Text(self, height=10, width=60, wrap=tk.WORD)
        self.text.pack()
        self.text.bind("<Control-c>", self.copy)
        self.text.bind("<Control-x>", self.cut)
        self.text.bind("<Control-v>", self.paste)
        self.text.bind("<Control-a>", self.select_all)
        
        self.youtube_button = tk.Button(self, text="YouTube", command=self.open_youtube, width=60)
        self.youtube_button.pack()

    def translate(self, event=None):
        word = self.entry.get()
        if word.isalpha() and word.isascii():
            lang_pair = ('en', 'ar')
        else:
            lang_pair = ('ar', 'en')
        translation = translate_word(word, lang_pair)
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", translation)

    def copy(self, event=None):
        self.text.event_generate("<<Copy>>")

    def cut(self, event=None):
        self.text.event_generate("<<Cut>>")

    def paste(self, event=None):
        self.text.event_generate("<<Paste>>")

    def select_all(self, event=None):
        self.text.tag_add("sel", "1.0", tk.END)

    def delete_text(self, event=None):
        self.entry.delete(0, tk.END)
        self.text.delete("1.0", tk.END)

    def open_youtube(self):
        webbrowser.open_new("https://www.youtube.com/channel/UCnN4_Dfa-GFQb5ORjBjWMJg")

        

if __name__ == '__main__':
    app = TranslateWindow()
    app.mainloop()
