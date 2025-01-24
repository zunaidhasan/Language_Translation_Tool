from tkinter import *
from tkinter import ttk, filedialog
from file_handler import extract_text_from_image, extract_text_from_pdf, extract_text_from_ppt
from googletrans import Translator, LANGUAGES

def translate_file(file_path, file_type, target_language):
    if file_type == "image":
        text = extract_text_from_image(file_path)
    elif file_type == "pdf":
        text = extract_text_from_pdf(file_path)
    elif file_type == "ppt":
        text = extract_text_from_ppt(file_path)
    else:
        return "Unsupported file type"
    
    if "Error" in text:
        return text
    
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def upload_file():
    file_path = filedialog.askopenfilename()
    file_type = file_path.split('.')[-1].lower()
    target_language = dest_lang.get()

    if file_type in ["png", "jpg", "jpeg"]:
        result = translate_file(file_path, "image", target_language)
    elif file_type == "pdf":
        result = translate_file(file_path, "pdf", target_language)
    elif file_type in ["ppt", "pptx"]:
        result = translate_file(file_path, "ppt", target_language)
    else:
        result = "Unsupported file type"

    Output_text.delete(1.0, END)
    Output_text.insert(END, result)

root = Tk()
root.geometry('800x400')
root.title('Language Translation Tool')

Label(root, text="Language Translator", font="Arial 20 bold").pack()

Button(root, text="Upload File for Translation", command=upload_file).pack(pady=20)

language = list(LANGUAGES.values())
dest_lang = ttk.Combobox(root, values=language, width=22)
dest_lang.set("Choose Target Language")
dest_lang.pack(pady=20)

Output_text = Text(root, font='Arial 12', height=10, width=80)
Output_text.pack()

root.mainloop()
