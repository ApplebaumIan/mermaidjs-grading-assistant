import pandas as pd
import re
import os
import argparse
import html
import base64

def clean_mermaid_code(raw_code):
    if not isinstance(raw_code, str):
        return ""

    # Unescape HTML entities like &lt;, &gt;, etc.
    code = html.unescape(raw_code)
    # Replace <br> with newlines
    code = re.sub(r'<br\s*/?>', '\n', code, flags=re.IGNORECASE)
    # Remove HTML tags like <pre>, <span>, <p>, etc.
    code = re.sub(r'</?\w+(?:\s+[^>]*?)?>', '', code)
    # Remove ```mermaid and ```
    code = re.sub(r'```mermaid', '', code)
    code = re.sub(r'```', '', code)
    # Trim leading/trailing whitespace
    return code.strip()

def main():
    parser = argparse.ArgumentParser(description='Process quiz data to extract and clean MermaidJS diagrams.')
    parser.add_argument('input_file', help='The path to the input CSV file.')
    parser.add_argument('column_identifiers', nargs='+', help='The names or indices of the columns containing MermaidJS code.')
    parser.add_argument('--output_dir', default='mermaid_diagrams', help='The directory to save the output .md files.')
    parser.add_argument('--render-url', action='store_true', help='Generate a mermaid.ink URL for rendering the image.')

    args = parser.parse_args()

    # Load the CSV file
    try:
        df = pd.read_csv(args.input_file)
    except FileNotFoundError:
        print(f"Error: The specified CSV file was not found at {args.input_file}")
        exit()

    columns_to_process = []
    for identifier in args.column_identifiers:
        try:
            col_idx = int(identifier)
            if col_idx >= len(df.columns):
                print(f"Error: Column index {col_idx} is out of bounds. The file has {len(df.columns)} columns.")
                exit()
            columns_to_process.append(df.columns[col_idx])
        except ValueError:
            if identifier not in df.columns:
                print(f"Error: Column '{identifier}' not found in the CSV file.")
                print("Available columns are:")
                for col in df.columns:
                    print(f"- '{col}'")
                exit()
            columns_to_process.append(identifier)

    # Create a directory to store the mermaid files
    os.makedirs(args.output_dir, exist_ok=True)

    # Get the base name of the input file
    csv_filename = os.path.basename(args.input_file)

    # Iterate over the dataframe and create a file for each student
    for index, row in df.iterrows():
        student_name = row.get('Name', f'student_{index}')

        # Start file content with headings
        file_content = f"# {csv_filename}\n## {student_name}\n\n"
        has_content = False

        for column_name in columns_to_process:
            mermaid_code = row[column_name]
            cleaned_code = clean_mermaid_code(mermaid_code)

            if cleaned_code:
                has_content = True
                # Add a subheading for the question/column
                file_content += f"### Question: {column_name}\n\n"

                # The cleaned code should contain the diagram type
                mermaid_diagram_code = cleaned_code

                if args.render_url:
                    # Base64 encode the mermaid code
                    base64_bytes = base64.b64encode(mermaid_diagram_code.encode('utf-8'))
                    base64_string = base64_bytes.decode('utf-8')
                    # Generate the mermaid.ink URL
                    file_content += f"![Mermaid Diagram](https://mermaid.ink/img/{base64_string})\n\n```mermaid\n{mermaid_diagram_code}\n```\n\n"
                else:
                    file_content += f"```mermaid\n{mermaid_diagram_code}\n```\n\n"

        # Only create a file if there was some mermaid code to process
        if has_content:
            # Sanitize student name for filename
            safe_filename = "".join([c for c in student_name if c.isalpha() or c.isdigit() or c==' ']).rstrip()
            output_filename = os.path.join(args.output_dir, f"{safe_filename}.md")

            with open(output_filename, 'w') as f:
                f.write(file_content)
            print(f"Created {output_filename}")

    print("Processing complete.")

if __name__ == '__main__':
    main()
