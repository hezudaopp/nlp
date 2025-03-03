import numpy as np

def print_numpy_info():
    print(np.__version__)
    for key, value in np.__config__.__dict__.items():
        print(key, value)

def create_null_vector_of_size_10():
    return np.zeros(10)

def memory_size_of_array(array):
    return array.nbytes

def create_a_random_vector_of_size_10_and_replace_the_maximum_value_with_0():
    a = np.random.rand(10)
    a[a.argmax()] = 0
    return a

def get_add_function_documentation():
    return np.add.__doc__

def set_fifth_element_to_one(array):
    array[4] = 1
    return array

def create_a_vector_with_values_ranging_from_10_to_49():
    return np.arange(10, 50)

def create_a_3x3_matrix_with_values_ranging_from_0_to_8():
    return np.arange(9).reshape(3, 3)

def reverse_a_vector(array):
    return array[::-1]

def find_indices_of_elements_that_are_not_zero(array):
    return np.nonzero(array)

def create_a_3x3_identity_matrix():
    return np.eye(3)

def create_a_3x3x3_matrix_with_random_values():
    return np.random.rand(3, 3, 3)  

def create_a_10x10_matrix_with_random_values_and_find_the_minimum_and_maximum_values():
    a = np.random.rand(10, 10)
    return a.min(), a.max()

def create_a_random_vector_of_size_10_and_find_the_mean_value():
    a = np.random.rand(10)
    return a.mean()

def create_a_2d_array_with_1s_on_the_border_and_0s_inside(m, n):
    a = np.ones((m, n))
    a[1:-1, 1:-1] = 0
    return a

def add_a_border_of_zeros_around_an_array(array):
    return np.pad(array, 1, mode='constant', constant_values=0)

def result_of_nan_expression():
    print(0 * np.nan)
    print(np.nan == np.nan)
    print(np.inf > np.nan)
    print(np.nan - np.nan)
    print(0.3 == 3 * 0.1)

def create_5x5_matrix_with_values_1234_below_the_diagonal():
    a = np.zeros((5, 5))
    a += np.diag(np.arange(1, 5), k=-1)
    return a
    
    
def create_a_8x8_matrix_and_fill_with_a_checkerboard_pattern():
    a = np.zeros((8, 8))
    a[1::2, ::2] = 1
    a[::2, 1::2] = 1
    return a

def indices_of_the_100th_element_of_a_6x7x8_matrix():
    return np.unravel_index(99, (6, 7, 8))

if __name__ == "__main__":
    # print_numpy_info()
    # v = create_null_vector_of_size_10()
    # print(v)
    # print(memory_size_of_array(v))
    # print(get_add_function_documentation())
    # v = create_null_vector_of_size_10()
    # print(v)
    # v = set_fifth_element_to_one(v)
    # print(v)
    # v = create_a_vector_with_values_ranging_from_10_to_49()
    # print(v)
    # v = reverse_a_vector(v)
    # print(v)
    # m = create_a_3x3_matrix_with_values_ranging_from_0_to_8()
    # print(m)
    # print(m.shape)
    # print(m.size)
    # print(m.ndim)
    # print(m.dtype)
    # print(v)
    # print(find_indices_of_elements_that_are_not_zero(np.array([1,2,0,0,4,0])))
    # print(create_a_3x3_identity_matrix())
    # print(create_a_3x3x3_matrix_with_random_values())
    # print(create_a_10x10_matrix_with_random_values_and_find_the_minimum_and_maximum_values())
    # print(create_a_random_vector_of_size_10_and_find_the_mean_value())
    # print(create_a_2d_array_with_1s_on_the_border_and_0s_inside(6, 5))
    # print(add_a_border_of_zeros_around_an_array(np.array([[1,2,3],[4,5,6],[7,8,9]])))
    # result_of_nan_expression()
    # print(create_5x5_matrix_with_values_1234_below_the_diagonal())
    # print(create_a_8x8_matrix_and_fill_with_a_checkerboard_pattern())
    print(indices_of_the_100th_element_of_a_6x7x8_matrix())