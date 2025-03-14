import time
import random
#swap function
def swap(a,b):
    temp=a
    a=b
    b=temp
# 📌 Bubble Sort Implementation (To be completed by students)
def bubble_sort(arr):
    """
    Bubble Sort algorithm to sort a list in ascending order.
    :param arr: List of numbers
    :return: Sorted list
    """
    n=len(arr)#take the length of the array
    l=n#take the length of the array to change it later
    e=0#varibale to count the number of swap
    p=1#a varibale to count the number of pass
    while(p<=n-1):#the code will run while the number of pass less then the length of table
        for i in range(l-1):#pass from the first element to the last-2 element
            if arr[i]>arr[i+1]:#compare each two succesive element
                swap(arr[i],arr[i+1])#if the first element grater then the second wap them
                e+=1#increase the number of swap
        if e==0:#if the code didn't swap element the traitment end
            return
        else:
            l-=1#decrease the number of element element in the next eteration
        p+=1#increase the number of pass


     # TODO: Implement Bubble Sort logic

# 📌 Selection Sort Implementation (To be completed by students)
def selection_sort(arr):
    """
    Selection Sort algorithm to sort a list in ascending order.
    :param arr: List of numbers
    :return: Sorted list
    """
    l=len(arr)#take the length of the array
    for i in range(l-2):#itrate the table from the first element to the last -3
        small=i#take the index of first element as the smallest
        for j in range(i+1,l-1):#itrate the rest of array to ind the smallest one
            if arr[j]<arr[small]:#compare the elemnt
                small=j
        if small!=j:
            swap(arr[i],arr[small])#swap the elements first element with the smallest one
      # TODO: Implement Selection Sort logic

def insertion_sort(arr):
    """
    Selection Sort algorithm to sort a list in ascending order.
    :param arr: List of numbers
    :return: Sorted list
    """
    for j in range(len(arr)):#itrate all the array from the second element
        key=arr[j]#take the first element in not sorted part
        i=j-1#take the first index of the not sorted part
        while i>0 and arr[i]>key:#itrate the sorted part to find the element location
            arr[i+1]=arr[i]
            i-=1
        arr[i+1]=key
    
        





# 📌 Function to test sorting performance
def test_sorting_performance():
    """
    Generates a list of random numbers and tests the execution time of both sorting algorithms.
    """
    small_dataset = [random.uniform(1, 100) for _ in range(50)]
    large_dataset = [random.uniform(1, 100) for _ in range(1000)]
    solarge_dataset = [random.uniform(1, 100) for _ in range(20000)]
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
    # Insetion Sort test
    insertion_test = large_dataset.copy()
    start_time = time.time()
    insertion_sort(insertion_test)
    end_time = time.time()
    print(f"✅ Insetion Sort took {end_time - start_time:.6f} seconds.")

    # Python Built-in Sort
    python_sort_test = small_dataset.copy()
    start_time = time.time()
    sorted(python_sort_test)
    end_time = time.time()
    print(f"🚀 Python Built-in Sort took {end_time - start_time:.6f} seconds.")
    
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

    # Insetion Sort test
    insertion_test = large_dataset.copy()
    start_time = time.time()
    insertion_sort(insertion_test)
    end_time = time.time()
    print(f"✅ Insetion Sort took {end_time - start_time:.6f} seconds.")
    
    # Python Built-in Sort
    python_sort_test = large_dataset.copy()
    start_time = time.time()
    sorted(python_sort_test)
    end_time = time.time()
    print(f"🚀 Python Built-in Sort took {end_time - start_time:.6f} seconds.")


    print("\n🔹 solarge Dataset (10000 elements):")
    
    # Bubble Sort test
    bubble_test = solarge_dataset.copy()
    start_time = time.time()
    bubble_sort(bubble_test)
    end_time = time.time()
    print(f"✅ Bubble Sort took {end_time - start_time:.6f} seconds.")
    
    # Selection Sort test
    selection_test = solarge_dataset.copy()
    start_time = time.time()
    selection_sort(selection_test)
    end_time = time.time()
    print(f"✅ Selection Sort took {end_time - start_time:.6f} seconds.")
    # Insetion Sort test
    insertion_test = solarge_dataset.copy()
    start_time = time.time()
    insertion_sort(insertion_test)
    end_time = time.time()
    print(f"✅ Insetion Sort took {end_time - start_time:.6f} seconds.")

    # Python Built-in Sort
    python_sort_test = solarge_dataset.copy()
    start_time = time.time()
    sorted(python_sort_test)
    end_time = time.time()
    print(f"🚀 Python Built-in Sort took {end_time - start_time:.6f} seconds.")

# Run the performance test
test_sorting_performance()
