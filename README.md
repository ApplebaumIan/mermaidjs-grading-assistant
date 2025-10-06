# MermaidJS UML Grading Assistant

<center>

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ApplebaumIan/mermaidjs-grading-assistant)
[![Open in Dev Container](https://img.shields.io/badge/Open%20in-Dev%20Container-blue?logo=visualstudiocode)](https://code.visualstudio.com/docs/remote/containers)
[![Open in Jetbrains](https://img.shields.io/badge/Open%20in-JetBrains-blue?logo=jetbrains)](https://www.jetbrains.com/help/idea/connect-to-devcontainer.html)

</center>

This repository contains a simple grading assistant for UML diagrams created using MermaidJS. The program renders student's UML written in MermaidJS Markdown provided from a CanvasLMS quiz results CSV. As long as the student added their mermaidjs markdown in the essay response field this program can render it!

```shell
python process_quiz_data.py ./data/{YOUR_CSV_FILE}.csv {COLUMN_NUMBER_1} {COLUMN_NUMBER_2} ...
```

After running the command, the program will generate one markdown file per student in the `mermaid_diagrams` directory. Each file will contain the student's name as the filename, and all their UML diagrams from the specified columns, rendered in MermaidJS format under the appropriate question heading.

## Prerequisites
- Python 3.x
- pandas library (install via `pip install pandas`)
- MermaidJS (for rendering the diagrams, can be used in Markdown viewers that support it)

All of which are available in the provided devcontainer.json for VSCode and Jetbrains. This can be used in GitHub Codespaces as well if Docker is not installed locally.

## Usage

1. Clone the repository to your local machine.
2. Open the repository in VSCode or Jetbrains IDE.
3. If using VSCode, open the command palette (Ctrl+Shift+P) and select "Remote-Containers: Open Folder in Container...". If using Jetbrains, open the project and ensure the Docker plugin is enabled.
4. Open a terminal in the IDE.
5. Run the provided command with your CSV file and the column numbers containing the MermaidJS UML diagrams. You can list multiple column numbers separated by spaces.
6. Check the `mermaid_diagrams` directory for the generated markdown files.

**If using GitHub Codespaces, simply open the repository in a new codespace and follow steps 4-6.**

### Rendering as an Image (Optional)

To render the diagrams as images using the `mermaid.ink` service, you can use the `--render-url` flag. This is useful for sharing or for platforms that do not support MermaidJS rendering.

```shell
python process_quiz_data.py ./data/{YOUR_CSV_FILE}.csv {COLUMN_NUMBER_1} {COLUMN_NUMBER_2} ... --render-url
```

This will generate markdown files containing a link to the rendered image for each specified column, along with the raw MermaidJS code for grading purposes.

### Full Manual Install Process without devcontainer (if needed)
1. Ensure you have Python 3.x installed on your machine.
2. Install the pandas library using pip:
   ```shell
   pip install pandas
   ```
3. Clone the repository to your local machine.
4. Open a terminal and navigate to the cloned repository.
5. Run the provided command with your CSV file and the column numbers containing the MermaidJS UML diagrams.
6. Check the `mermaid_diagrams` directory for the generated markdown files.
7. Use a Markdown viewer that supports MermaidJS to view the rendered diagrams.