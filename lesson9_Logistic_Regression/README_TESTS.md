# Unit Tests for Logistic Regression Workflow

## Overview

This test suite provides comprehensive unit tests for the logistic regression data preprocessing and model training workflow. The tests verify the correct functionality of all key components including data splitting, scaling, model initialization, training, and prediction.

## Test Cases Covered

### 1. Train-Test Split Verification
**Test:** `test_01_train_test_split_correctly_splits_data`

Verifies that `train_test_split` correctly splits data into training and testing sets:
- Correct split ratio (90% train, 10% test)
- No data loss during splitting
- Correct shapes maintained
- X and y splits are properly aligned
- Data types are preserved

### 2. Training Data Scaling
**Test:** `test_02_standard_scaler_correctly_scales_training_data`

Verifies that `StandardScaler` correctly scales training data:
- Scaler fits on training data
- Scaled data has mean ≈ 0 and std ≈ 1
- Transformation preserves shape
- No NaN or infinite values introduced
- Scaler learns correct parameters

### 3. Test Data Scaling with Training Parameters
**Test:** `test_03_standard_scaler_uses_training_parameters_for_test_data`

Verifies that `StandardScaler` uses training parameters for test data:
- Test data transformed using training statistics
- `fit_transform` not called on test data
- Only `transform` used for test data
- Scaler parameters remain unchanged
- Transformation is mathematically correct

### 4. LogisticRegression Initialization and Fitting
**Test:** `test_04_logistic_regression_initialization_and_fitting`

Verifies that `LogisticRegression` model works correctly:
- Model initializes with default parameters
- Model fits on scaled training data without errors
- Model learns coefficients and intercept
- Coefficients are non-zero
- Model converges successfully

### 5. Making Predictions on New Data
**Test:** `test_05_logistic_regression_prediction_on_new_data`

Verifies that trained model makes correct predictions:
- Model predicts on new scaled data without errors
- Predictions have correct format and shape
- Prediction probabilities sum to 1
- Probabilities are in valid range [0, 1]
- Predictions consistent with probabilities
- Single sample predictions work correctly

### Edge Cases

#### Constant Feature Handling
**Test:** `test_scaler_with_constant_feature`

Verifies StandardScaler handles constant features gracefully.

#### Reproducibility
**Test:** `test_train_test_split_reproducibility`

Verifies train_test_split produces identical results with same random_state.

## Running the Tests

### Prerequisites

Ensure you have the virtual environment activated:

```bash
cd "/home/andrew/Python projects/DS_ML_course"
source .venv/bin/activate
```

### Run All Tests

```bash
cd lesson9_Logistic_Regression
python test_logistic_regression.py
```

### Run with Verbose Output

```bash
python test_logistic_regression.py -v
```

### Run Specific Test Class

```python
# In Python
import unittest
from test_logistic_regression import TestLogisticRegressionWorkflow

suite = unittest.TestLoader().loadTestsFromTestCase(TestLogisticRegressionWorkflow)
unittest.TextTestRunner(verbosity=2).run(suite)
```

### Run Specific Test Method

```bash
python -m unittest test_logistic_regression.TestLogisticRegressionWorkflow.test_01_train_test_split_correctly_splits_data
```

## Test Results Interpretation

### Success
```
Ran 7 tests in 0.029s

OK
```

All tests passed successfully!

### Failure
If a test fails, you'll see detailed error messages indicating:
- Which assertion failed
- Expected vs actual values
- Line number of the failure
- Descriptive error message

Example:
```
FAIL: test_02_standard_scaler_correctly_scales_training_data
AssertionError: Mean of feature 0 should be close to 0
```

## Test Data

The tests use synthetic data similar to the hearing test dataset:
- 100 samples
- 2 features (age, physical_score)
- Binary target variable (test_result: 0 or 1)
- Reproducible with fixed random seed (42)

## Dependencies

The test suite requires:
- Python 3.6+
- numpy
- pandas
- scikit-learn
- unittest (built-in)

All dependencies are included in the project's virtual environment.

## Integration with Continuous Integration

These tests can be integrated into a CI/CD pipeline:

```yaml
# Example GitHub Actions workflow
name: Run Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install numpy pandas scikit-learn
      - name: Run tests
        run: |
          source venv/bin/activate
          cd "lesson9_Logistic_Regression"
          python test_logistic_regression.py
```

## Extending the Tests

To add new tests:

1. Add a new method to `TestLogisticRegressionWorkflow` class
2. Name it starting with `test_`
3. Use descriptive assertions with error messages
4. Document what the test verifies

Example:
```python
def test_06_custom_test_case(self):
    """
    Brief description of what this test verifies.
    """
    # Setup
    # ... your test code ...
    
    # Assertions
    self.assertEqual(actual, expected, "Descriptive error message")
```

## Best Practices

1. **Isolation**: Each test is independent and doesn't rely on other tests
2. **Reproducibility**: Fixed random seeds ensure consistent results
3. **Clarity**: Descriptive names and docstrings explain what's being tested
4. **Completeness**: Tests cover both happy paths and edge cases
5. **Assertions**: Meaningful error messages help debugging

## Troubleshooting

### Import Errors
If you get `ModuleNotFoundError`:
```bash
# Ensure virtual environment is activated
source .venv/bin/activate

# Verify packages are installed
pip list | grep -E "numpy|pandas|scikit-learn"
```

### Test Failures Due to Random Variation
If tests fail due to statistical variation:
- Check if random seeds are properly set
- Consider relaxing precision requirements for small samples
- Increase sample size for more stable statistics

### Virtual Environment Issues
If virtual environment isn't working:
```bash
# Recreate virtual environment
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
pip install numpy pandas scikit-learn matplotlib seaborn jupyter
```

## Contact and Contribution

For questions or contributions to the test suite, please follow standard Python testing conventions and maintain code quality.

---

**Last Updated:** 2026-01-05
**Test Suite Version:** 1.0
**Python Version:** 3.12+
