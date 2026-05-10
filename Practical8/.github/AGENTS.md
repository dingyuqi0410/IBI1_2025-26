# AI Coding Agent Guidance

## Project overview
This repository contains a small Python exercise workspace with two scripts:
- `nutrition_data_tracker.py` — calculates nutrition totals for a list of food items
- `predicting_protein_mass.py` — estimates protein mass from an amino acid sequence

No existing tests, packaging, or documentation files are present.

## What to do
- Treat this as a simple Python learning exercise.
- Prefer clear, idiomatic Python and PEP 8 naming conventions.
- Keep functions reusable: avoid printing inside core logic if the user asks for refactoring.
- If adding examples, use a `if __name__ == "__main__":` guard.
- Do not assume any external libraries beyond the Python standard library.

## File-specific notes
- `nutrition_data_tracker.py`
  - This file currently mixes data modeling and script output.
  - `food_item` should be a class name like `FoodItem`, and the nutritional calculation should return values cleanly.
  - Fix typos in warning text and avoid hardcoded example data in reusable functions.

- `predicting_protein_mass.py`
  - The mass lookup is dictionary-based and should validate sequences explicitly.
  - Use exceptions or clear error handling for invalid amino acids.
  - Ensure mass calculation works for uppercase and lowercase input.

## When asked to improve code
- Favor safe bug fixes over speculative feature additions.
- Preserve existing script behavior unless the user explicitly asks for a different interface.
- Keep changes small and readable in this educational project.

## If creating new files
- Use plain Python modules at the repository root.
- Create tests only if requested or if a refactor benefits from verification.
- Name test files `test_*.py` and keep the test dependency-free when possible.
