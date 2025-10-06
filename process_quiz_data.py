import pandas as pd
import re
import os
import argparse
import html

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
    # Remove classDiagram case-insensitively
    code = re.sub(r'classDiagram', '', code, flags=re.IGNORECASE)
    # Trim leading/trailing whitespace
    return code.strip()

def main():
    parser = argparse.ArgumentParser(description='Process quiz data to extract and clean MermaidJS diagrams.')
    parser.add_argument('input_file', help='The path to the input CSV file.')
    parser.add_argument('column_identifier', help='The name or index of the column containing the MermaidJS code.')
    parser.add_argument('--output_dir', default='mermaid_diagrams', help='The directory to save the output .md files.')

    args = parser.parse_args()

    # Load the CSV file
    try:
        df = pd.read_csv(args.input_file)
    except FileNotFoundError:
        print(f"Error: The specified CSV file was not found at {args.input_file}")
        exit()

    try:
        col_idx = int(args.column_identifier)
        if col_idx >= len(df.columns):
            print(f"Error: Column index {col_idx} is out of bounds. The file has {len(df.columns)} columns.")
            exit()
        column_to_process = df.columns[col_idx]
    except ValueError:
        column_to_process = args.column_identifier
        if column_to_process not in df.columns:
            print(f"Error: Column '{column_to_process}' not found in the CSV file.")
            print("Available columns are:")
            for col in df.columns:
                print(f"- '{col}'")
            exit()


    # Create a directory to store the mermaid files
    os.makedirs(args.output_dir, exist_ok=True)

    # Iterate over the dataframe and create a file for each student
    for index, row in df.iterrows():
        student_name = row.get('Name', f'student_{index}')
        mermaid_code = row[column_to_process]

        cleaned_code = clean_mermaid_code(mermaid_code)

        if cleaned_code:
            # Create the full mermaid diagram content
            full_mermaid_content = f"```mermaid\nclassDiagram\n{cleaned_code}\n```"

            # Sanitize student name for filename
            safe_filename = "".join([c for c in student_name if c.isalpha() or c.isdigit() or c==' ']).rstrip()
            output_filename = os.path.join(args.output_dir, f"{safe_filename}.md")

            with open(output_filename, 'w') as f:
                f.write(full_mermaid_content)
            print(f"Created {output_filename}")

    print("Processing complete.")

if __name__ == '__main__':
    main()
