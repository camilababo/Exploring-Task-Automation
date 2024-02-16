import argparse
import pyttsx3
import PyPDF3


def pdf_to_mp3(pdf_file):
    """
    Extracts the text in a pdf file and transcribes it to a mp3 file.
    :param pdf_file: PDF file to transcribe.
    :return: mp3 file
    """

    try:
        pdf_reader = PyPDF3.PdfFileReader(open(pdf_file, 'rb'))
        speaker = pyttsx3.init()

        for page_num in range(pdf_reader.numPages):
            text = pdf_reader.getPage(page_num).extractText()
            clean_text = text.strip().replace('\n', '  ')
            print(clean_text)

        output_file = pdf_file + '_AUDIO.mp3'

        speaker.save_to_file(clean_text, output_file)
        speaker.runAndWait()

        speaker.stop()
        print("Conversion completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert PDF to MP3')
    parser.add_argument('-file', dest='pdf_file', required=True, help='File path to the PDF file')
    args = parser.parse_args()

    pdf_to_mp3(args.pdf_file)
