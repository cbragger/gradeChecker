from unittest import TestCase, mock, main

# All test classes must have the same name
# We'll come up with something better than TestTest I hope
class TestTest(TestCase):

    def __init__(self, method_name='subTest', test_func:callable=None) -> None:
        super().__init__(method_name)
        self.test_func = test_func

    @mock.patch('builtins.input', create=True)
    @mock.patch('builtins.print')
    def test_happy_path(self, mock_print, inputs):
        # Arrange
        inputs.side_effect = ['3']
        expected_outputs = ['1','2','3']

        # Act
        self.test_func()
        actual_outputs = mock_print.call_args_list

        # Assert
        for i in range(len(expected_outputs)):
            self.assertEqual(expected_outputs[i], str(actual_outputs[i][0][0]))

if __name__ == "__main__":

    def test_func():
        num_times = int(input("Give number from 1-10: "))
        for i in range(num_times):
            print(i + 1)

    test = TestTest(test_func=test_func)
    print(test.run())