import time
import random

# 📌 Bubble Sort Implementation (To be completed by students)
def bubble_sort(arr):
    """
    Bubble Sort algorithm to sort a list in ascending order.
    :param arr: List of numbers
    :return: Sorted list
    """
    pass  # TODO: Implement Bubble Sort logic

# 📌 Selection Sort Implementation (To be completed by students)
def selection_sort(arr):
    """
    Selection Sort algorithm to sort a list in ascending order.
    :param arr: List of numbers
    :return: Sorted list
    """
    pass  # TODO: Implement Selection Sort logic

# 📌 Function to test sorting performance
def test_sorting_performance():
    """
    Generates a list of random numbers and tests the execution time of both sorting algorithms.
    """
    small_dataset = [random.uniform(1, 100) for _ in range(50)]
    large_dataset = [random.uniform(1, 100) for _ in range(1000)]
    
    print("\n🔹 Small Dataset (50 elements):")
    
    # Bubble Sort test
    bubble_test = small_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"✅ Bubble Sort took {end_time - start_time:.6f} seconds.")
    
    # Selection Sort test
    selection_test = small_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"✅ Selection Sort took {end_time - start_time:.6f} seconds.")
    
    print("\n🔹 Large Dataset (1000 elements):")
    
    # Bubble Sort test
    bubble_test = large_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"⚠️ Bubble Sort took {end_time - start_time:.6f} seconds.")
    
    # Selection Sort test
    selection_test = large_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"✅ Selection Sort took {end_time - start_time:.6f} seconds.")
    
    # Python Built-in Sort
    python_sort_test = large_dataset.copy()
    start_time = time.time()
    sorted(python_sort_test)
    end_time = time.time()
    print(f"🚀 Python Built-in Sort took {end_time - start_time:.6f} seconds.")

# Run the performance test
test_sorting_performance()
