import pytesseract
from PIL import Image
from docx import Document


def extract_text_from_image(image_path):
    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(Image.open(image_path))
    return text


def save_to_word(text, output_file):
    # Create a new Word document
    doc = Document()

    # Add text to the Word document
    doc.add_paragraph(text)

    # Save the Word document
    doc.save(output_file)
    print(f"Text extracted and saved to {output_file}")


if __name__ == "__main__":
    # Path to your screenshot image
    image_path = "/Users/rjw/Programming/projects/shot-to-doc/screenshot.png"

    # Output Word document name
    output_file = "output.docx"

    # Extract text from the image
    extracted_text = extract_text_from_image(image_path)

    # Save extracted text to a Word document
    save_to_word(extracted_text, output_file)
