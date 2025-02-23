import markdown
import sys


def convert_markdown_to_html(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f_in:
            markdown_text = f_in.read()
        html_text = markdown.markdown(markdown_text)
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write(html_text)
        print(f"Operation successful: {input_file} -> {output_file}")
    except FileNotFoundError:
        print(f"Error: File {input_file} not Found")
    except Exception as e:
        print(f"Error: An error occured during conversion: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python file_converter.py markdown <inputfule.md> <outputfile.html>")
        sys.exit(1)

    command, input_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3]

    if command != "markdown":
        print("Error: Command needs to be 'markdown' ")
        sys.exit(1)

    convert_markdown_to_html(input_file, output_file)