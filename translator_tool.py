import sys
from googletrans import Translator, LANGUAGES
from file_handler import extract_text_from_image, extract_text_from_pdf, extract_text_from_ppt

def translate_text(input_text, target_language):
    """
    Translates the given input text to the target language.
    """
    translator = Translator()
    try:
        translation = translator.translate(input_text, dest=target_language)
        return translation.text
    except Exception as e:
        return f"Error during translation: {str(e)}"

def translate_file(file_path, file_type, target_language):
    """
    Translates the content of a file (image, PDF, or PPT) to the target language.
    """
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

    return translate_text(text, target_language)

def main():
    """
    Main function for the command-line interface.
    """
    print("Welcome to the Language Translation Tool")
    print("Choose an option:")
    print("1. Translate Text")
    print("2. Translate File (image, PDF, or PPT)")

    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        input_text = input("Enter the text to translate: ").strip()
        print("\nAvailable Languages:")
        for lang_code, lang_name in LANGUAGES.items():
            print(f"{lang_code}: {lang_name}")

        target_language = input("\nEnter the target language code: ").strip()

        if target_language not in LANGUAGES:
            print("Invalid language code. Exiting.")
            sys.exit(1)

        result = translate_text(input_text, target_language)
        print("\nTranslation Result:")
        print(result)

    elif choice == "2":
        file_path = input("Enter the file path: ").strip()
        file_type = input("Enter the file type (image/pdf/ppt): ").strip().lower()
        
        print("\nAvailable Languages:")
        for lang_code, lang_name in LANGUAGES.items():
            print(f"{lang_code}: {lang_name}")

        target_language = input("\nEnter the target language code: ").strip()

        if target_language not in LANGUAGES:
            print("Invalid language code. Exiting.")
            sys.exit(1)

        result = translate_file(file_path, file_type, target_language)
        print("\nTranslation Result:")
        print(result)

    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
