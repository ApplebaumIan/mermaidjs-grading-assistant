# MermaidJS UML Grading Assistant

This repository contains a simple grading assistant for UML diagrams created using MermaidJS. The program renders student's UML written in MermaidJS Markdown provided from a CanvasLMS quiz results CSV.

```shell
python process_quiz_data.py ./data/{YOUR_CSV_FILE}.csv {ROW_NUMBER}
```

After running the command, the program will generate markdown files per student in the `mermaid_diagrams` directory. Each file will contain the student's name as the filename, and their UML diagram rendered in MermaidJS format.

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
5. Run the provided command with your CSV file and the row number containing the MermaidJS UML diagrams.
6. Check the `mermaid_diagrams` directory for the generated markdown files.

**If using GitHub Codespaces, simply open the repository in a new codespace and follow steps 4-6.**

### Full Manual Install Process without devcontainer (if needed)
1. Ensure you have Python 3.x installed on your machine.
2. Install the pandas library using pip:
   ```shell
   pip install pandas
   ```
3. Clone the repository to your local machine.
4. Open a terminal and navigate to the cloned repository.
5. Run the provided command with your CSV file and the row number containing the MermaidJS UML diagrams.
6. Check the `mermaid_diagrams` directory for the generated markdown files.
7. Use a Markdown viewer that supports MermaidJS to view the rendered diagrams.