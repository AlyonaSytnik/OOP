# OOP

## Installation

1. Clone the repository:
```
git clone https://github.com/AlyonaSytnik/OOP.git
```
2. Navigate to the project directory:
```
cd oop
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Run the main script:
```
python main.py
```
## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Submit a pull request.

## Testing

To run the tests, execute the following command:

```
python -m unittest discover -s tests -p "test_*.py"
```

Alternatively, you can use a testing framework like `pytest`:

```
pytest tests/
```

The project includes the following test files:
- `conftest` (for usage in tests)
- `test_categories.py`
- `test_products.py`

Tests coverage: