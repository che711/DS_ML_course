"""
Unit Tests for Logistic Regression Workflow

This module contains unit tests for the following cases:
1. Verify that the data is correctly split into training and testing sets using train_test_split.
2. Verify that the StandardScaler correctly scales the training data.
3. Verify that the StandardScaler correctly scales the test data using the parameters learned from the training data.
4. Verify that the LogisticRegression model can be initialized and fitted to the scaled training data without errors.
5. Verify that the trained LogisticRegression model can make predictions on new, scaled data.
"""

import unittest
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


class TestLogisticRegressionWorkflow(unittest.TestCase):
    """Test suite for logistic regression workflow including data preprocessing and model training."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test data that will be used across all tests."""
        # Create sample dataset similar to the hearing test data
        np.random.seed(42)
        n_samples = 100
        
        # Generate synthetic features
        age = np.random.uniform(18, 90, n_samples)
        physical_score = np.random.uniform(0, 50, n_samples)
        
        # Generate target variable (0 or 1) with some relationship to features
        # Higher age and lower physical score tend to result in test failure (0)
        test_result = ((age < 50) & (physical_score > 30)).astype(int)
        
        # Create DataFrame
        cls.df = pd.DataFrame({
            'age': age,
            'physical_score': physical_score,
            'test_result': test_result
        })
        
        # Prepare X and y
        cls.X = cls.df.drop('test_result', axis=1)
        cls.y = cls.df['test_result']
    
    def test_01_train_test_split_correctly_splits_data(self):
        """
        Test Case 1: Verify that the data is correctly split into training and testing sets.
        
        This test checks:
        - The split ratio is correct (90% train, 10% test)
        - No data is lost during splitting
        - The splits maintain the correct shapes
        - X and y splits are aligned
        """
        # Perform train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.1, random_state=101
        )
        
        # Verify split ratios
        total_samples = len(self.X)
        expected_test_size = int(total_samples * 0.1)
        expected_train_size = total_samples - expected_test_size
        
        self.assertEqual(len(X_train), expected_train_size, 
                        f"Training set should contain {expected_train_size} samples")
        self.assertEqual(len(X_test), expected_test_size,
                        f"Test set should contain {expected_test_size} samples")
        
        # Verify no data is lost
        self.assertEqual(len(X_train) + len(X_test), total_samples,
                        "Total samples should equal sum of train and test")
        
        # Verify X and y splits are aligned
        self.assertEqual(len(X_train), len(y_train),
                        "X_train and y_train should have same length")
        self.assertEqual(len(X_test), len(y_test),
                        "X_test and y_test should have same length")
        
        # Verify shapes
        self.assertEqual(X_train.shape[1], self.X.shape[1],
                        "Training features should have same number of columns as original")
        self.assertEqual(X_test.shape[1], self.X.shape[1],
                        "Test features should have same number of columns as original")
        
        # Verify data types are preserved
        self.assertIsInstance(X_train, pd.DataFrame,
                             "X_train should be a DataFrame")
        self.assertIsInstance(X_test, pd.DataFrame,
                             "X_test should be a DataFrame")
        self.assertIsInstance(y_train, pd.Series,
                             "y_train should be a Series")
        self.assertIsInstance(y_test, pd.Series,
                             "y_test should be a Series")
    
    def test_02_standard_scaler_correctly_scales_training_data(self):
        """
        Test Case 2: Verify that the StandardScaler correctly scales the training data.
        
        This test checks:
        - The scaler fits on training data
        - Scaled data has mean ≈ 0 and std ≈ 1
        - The transformation doesn't change the shape
        - No NaN or infinite values are introduced
        """
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.1, random_state=101
        )
        
        # Initialize and fit scaler
        scaler = StandardScaler()
        scaled_X_train = scaler.fit_transform(X_train)
        
        # Verify shape is preserved
        self.assertEqual(scaled_X_train.shape, X_train.shape,
                        "Scaled data should have same shape as original")
        
        # Verify standardization: mean should be close to 0
        means = np.mean(scaled_X_train, axis=0)
        for i, mean in enumerate(means):
            self.assertAlmostEqual(mean, 0.0, places=10,
                                  msg=f"Mean of feature {i} should be close to 0")
        
        # Verify standardization: std should be close to 1
        stds = np.std(scaled_X_train, axis=0, ddof=1)  # ddof=1 for sample std
        for i, std in enumerate(stds):
            self.assertAlmostEqual(std, 1.0, places=1,
                                  msg=f"Std of feature {i} should be close to 1")
        
        # Verify no NaN or infinite values
        self.assertFalse(np.any(np.isnan(scaled_X_train)),
                        "Scaled data should not contain NaN values")
        self.assertFalse(np.any(np.isinf(scaled_X_train)),
                        "Scaled data should not contain infinite values")
        
        # Verify scaler learned the parameters
        self.assertTrue(hasattr(scaler, 'mean_'),
                       "Scaler should have learned mean_")
        self.assertTrue(hasattr(scaler, 'scale_'),
                       "Scaler should have learned scale_")
        self.assertEqual(len(scaler.mean_), X_train.shape[1],
                        "Scaler mean_ should match number of features")
    
    def test_03_standard_scaler_uses_training_parameters_for_test_data(self):
        """
        Test Case 3: Verify that the StandardScaler correctly scales the test data 
        using the parameters learned from the training data.
        
        This test checks:
        - Test data is transformed using training parameters
        - fit_transform is not called on test data
        - Only transform is used for test data
        - The transformation is consistent
        """
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.1, random_state=101
        )
        
        # Fit scaler on training data only
        scaler = StandardScaler()
        scaled_X_train = scaler.fit_transform(X_train)
        
        # Store the learned parameters
        train_mean = scaler.mean_.copy()
        train_scale = scaler.scale_.copy()
        
        # Transform test data using training parameters
        scaled_X_test = scaler.transform(X_test)
        
        # Verify shape is preserved
        self.assertEqual(scaled_X_test.shape, X_test.shape,
                        "Scaled test data should have same shape as original")
        
        # Verify the scaler parameters haven't changed
        np.testing.assert_array_equal(scaler.mean_, train_mean,
                                     "Scaler mean should not change after transforming test data")
        np.testing.assert_array_equal(scaler.scale_, train_scale,
                                     "Scaler scale should not change after transforming test data")
        
        # Verify transformation uses training statistics
        # Manually compute what the scaled test data should be
        expected_scaled_test = (X_test.values - train_mean) / train_scale
        np.testing.assert_array_almost_equal(scaled_X_test, expected_scaled_test,
                                            err_msg="Test data should be scaled using training statistics")
        
        # Verify no NaN or infinite values in test data
        self.assertFalse(np.any(np.isnan(scaled_X_test)),
                        "Scaled test data should not contain NaN values")
        self.assertFalse(np.any(np.isinf(scaled_X_test)),
                        "Scaled test data should not contain infinite values")
        
        # Note: Test data mean and std will NOT be 0 and 1 because it uses training parameters
        # This is correct behavior - we verify this
        test_means = np.mean(scaled_X_test, axis=0)
        test_stds = np.std(scaled_X_test, axis=0)
        
        # These should generally NOT be 0 and 1 (unless by coincidence)
        # We just verify they are reasonable values
        self.assertTrue(np.all(np.abs(test_means) < 10),
                       "Test data means should be reasonable values")
        self.assertTrue(np.all(test_stds > 0),
                       "Test data stds should be positive")
    
    def test_04_logistic_regression_initialization_and_fitting(self):
        """
        Test Case 4: Verify that the LogisticRegression model can be initialized 
        and fitted to the scaled training data without errors.
        
        This test checks:
        - Model can be initialized with default parameters
        - Model can be fitted on scaled training data
        - Model learns coefficients and intercept
        - No errors occur during fitting
        """
        # Prepare data
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.1, random_state=101
        )
        
        scaler = StandardScaler()
        scaled_X_train = scaler.fit_transform(X_train)
        
        # Initialize LogisticRegression model
        model = LogisticRegression(max_iter=1000, random_state=42)
        
        # Verify model is properly initialized
        self.assertIsInstance(model, LogisticRegression,
                             "Model should be an instance of LogisticRegression")
        
        # Fit the model - this should not raise any errors
        try:
            model.fit(scaled_X_train, y_train)
            fitting_successful = True
        except Exception as e:
            fitting_successful = False
            self.fail(f"Model fitting raised an exception: {str(e)}")
        
        self.assertTrue(fitting_successful, "Model should fit without errors")
        
        # Verify model learned parameters
        self.assertTrue(hasattr(model, 'coef_'),
                       "Fitted model should have coef_ attribute")
        self.assertTrue(hasattr(model, 'intercept_'),
                       "Fitted model should have intercept_ attribute")
        
        # Verify coefficient dimensions
        n_features = scaled_X_train.shape[1]
        self.assertEqual(model.coef_.shape[1], n_features,
                        f"Model should have {n_features} coefficients")
        
        # Verify coefficients are not all zeros
        self.assertTrue(np.any(model.coef_ != 0),
                       "Model coefficients should not all be zero")
        
        # Verify model has classes_ attribute
        self.assertTrue(hasattr(model, 'classes_'),
                       "Fitted model should have classes_ attribute")
        self.assertEqual(len(model.classes_), 2,
                        "Binary classification should have 2 classes")
        
        # Verify convergence
        if hasattr(model, 'n_iter_'):
            self.assertTrue(model.n_iter_[0] < model.max_iter,
                           "Model should converge before max_iter")
    
    def test_05_logistic_regression_prediction_on_new_data(self):
        """
        Test Case 5: Verify that the trained LogisticRegression model can make 
        predictions on new, scaled data.
        
        This test checks:
        - Model can predict on new scaled data
        - Predictions are in the correct format
        - Prediction probabilities sum to 1
        - Predictions are consistent with probabilities
        """
        # Prepare full workflow
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.1, random_state=101
        )
        
        # Scale data
        scaler = StandardScaler()
        scaled_X_train = scaler.fit_transform(X_train)
        scaled_X_test = scaler.transform(X_test)
        
        # Train model
        model = LogisticRegression(max_iter=1000, random_state=42)
        model.fit(scaled_X_train, y_train)
        
        # Make predictions - this should not raise errors
        try:
            predictions = model.predict(scaled_X_test)
            prediction_successful = True
        except Exception as e:
            prediction_successful = False
            self.fail(f"Model prediction raised an exception: {str(e)}")
        
        self.assertTrue(prediction_successful, "Model should predict without errors")
        
        # Verify prediction shape
        self.assertEqual(len(predictions), len(scaled_X_test),
                        "Predictions should have same length as test data")
        
        # Verify predictions are valid class labels
        self.assertTrue(np.all(np.isin(predictions, model.classes_)),
                       "All predictions should be valid class labels")
        
        # Test predict_proba
        try:
            probabilities = model.predict_proba(scaled_X_test)
            proba_successful = True
        except Exception as e:
            proba_successful = False
            self.fail(f"Model predict_proba raised an exception: {str(e)}")
        
        self.assertTrue(proba_successful, "Model should predict probabilities without errors")
        
        # Verify probability shape
        self.assertEqual(probabilities.shape, (len(scaled_X_test), 2),
                        "Probabilities should have shape (n_samples, n_classes)")
        
        # Verify probabilities sum to 1
        prob_sums = np.sum(probabilities, axis=1)
        np.testing.assert_array_almost_equal(prob_sums, np.ones(len(scaled_X_test)),
                                            err_msg="Probabilities should sum to 1 for each sample")
        
        # Verify probabilities are in valid range [0, 1]
        self.assertTrue(np.all(probabilities >= 0) and np.all(probabilities <= 1),
                       "Probabilities should be between 0 and 1")
        
        # Verify consistency between predict and predict_proba
        predicted_classes_from_proba = np.argmax(probabilities, axis=1)
        predicted_classes_from_predict = predictions
        
        # Convert predictions to indices if they're not already
        if not np.issubdtype(predicted_classes_from_predict.dtype, np.integer):
            class_to_idx = {cls: idx for idx, cls in enumerate(model.classes_)}
            predicted_classes_from_predict = np.array([class_to_idx[p] for p in predictions])
        
        np.testing.assert_array_equal(predicted_classes_from_proba, predicted_classes_from_predict,
                                     err_msg="Predictions should be consistent with highest probability class")
        
        # Test prediction on single sample
        single_sample = scaled_X_test[[0]]
        single_prediction = model.predict(single_sample)
        self.assertEqual(len(single_prediction), 1,
                        "Single sample should produce single prediction")


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error conditions."""
    
    def test_scaler_with_constant_feature(self):
        """Test StandardScaler behavior with a constant feature."""
        # Use larger sample for more accurate std
        X = np.array([[1, 5], [1, 6], [1, 7], [1, 8], [1, 5.5], [1, 6.5], 
                      [1, 7.5], [1, 8.5], [1, 5.2], [1, 6.8]])
        scaler = StandardScaler()
        
        # This should handle constant feature gracefully
        scaled = scaler.fit_transform(X)
        
        # First feature should be all zeros (constant after scaling)
        self.assertTrue(np.allclose(scaled[:, 0], 0),
                       "Constant feature should scale to zero")
        
        # Second feature should be properly scaled (mean close to 0, std close to 1)
        # Note: With small samples, std might not be exactly 1 due to sample variance
        self.assertTrue(np.abs(np.mean(scaled[:, 1])) < 1e-10,
                       "Mean should be very close to 0")
        self.assertTrue(0.9 < np.std(scaled[:, 1], ddof=1) < 1.1,
                       "Std should be close to 1 (allowing for sample variance)")
    
    def test_train_test_split_reproducibility(self):
        """Test that train_test_split is reproducible with same random_state."""
        X = np.random.rand(100, 2)
        y = np.random.randint(0, 2, 100)
        
        # Split twice with same random_state
        X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y, test_size=0.2, random_state=42)
        X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Results should be identical
        np.testing.assert_array_equal(X_train1, X_train2)
        np.testing.assert_array_equal(X_test1, X_test2)
        np.testing.assert_array_equal(y_train1, y_train2)
        np.testing.assert_array_equal(y_test1, y_test2)


def run_tests():
    """Run all tests and print results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add tests
    suite.addTests(loader.loadTestsFromTestCase(TestLogisticRegressionWorkflow))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return True if all tests passed
    return result.wasSuccessful()


if __name__ == '__main__':
    # Run tests when script is executed directly
    success = run_tests()
    exit(0 if success else 1)
