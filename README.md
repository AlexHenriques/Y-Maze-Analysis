# Y-Maze Analysis

![GitHub](https://img.shields.io/github/license/alexhenriques/Y-Maze-Analysis)
![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)

This Python script performs Y-Maze analysis of sequence of entries. To assess spatial working memory, the analysis focuses on three types of behaviors: Spontaneous Alternation Performance (SAP), Alternate Arm Returns (AAR), and Same Arm Returns (SAR).

## Behavior Definitions

- **Spontaneous Alternation Performance:**
  - SAP refers to the tendency of an animal to alternate its arm choices during three consecutive trials.
  - SAP: ABC, ACB, BAC, BCA, CAB, CBA.

- **Alternate Arm Returns:**
  - AAR measures the number of times an animal returns to an arm it previously visited.
  - AAR: ABA, ACA, BAB, BCB, CBC, CAC

- **Same Arm Returns:**
  - SAR measures the number of times an animal returns to the same arm it just visited.
  - SAR: AA, BB, CC

## Code Structure

The Python script performs the following tasks:

1. Import data:
   - Collects the number of animals to analyze.
   - Collects animal IDs and their respective arm paths.

2. Calculate behavior statistics:
   - Calculates the number of entries (arm visits) for each animal.
   - Calculates the number of possible triads (groups of three arms).
   - Calculates the occurrence of SAP, AAR, and SAR for each animal.
   - Calculates the percentages of SAP, AAR, and SAR.

3. Export results CSV:
   - Exports the calculated results including IDs, paths, entries, possible triads, percentages of behaviors, and the actual number of behaviour occurrences.

## Installation

If you haven't already, make sure to install Git and Python

Follow these steps in a terminal:

1. Clone this repository to your local machine `git clone https://github.com/AlexHenriques/Y-MazeAnalysis.git`
2. Open a terminal and navigate to the repository's directory `cd Y-MazeAnalysis`.
3. Run the script using the command `python y-mazetool.py`.

## Usage

1. Enter the number of animals to analyze.
2. Enter animal IDs and their arm paths.

## Important Note

This script assumes that there are three arms (A, B, C) the arm paths are represented in order by "ABC" or "A,B,C".

## Requirements

- Python 3.6 or higher
- Git (optional, only required for cloning the repository))

## Author

- Alexandre Henriques
- Contact: alexandresshenriques@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
