# 📌 Sorting Algorithms Exercise: Bubble Sort & Selection Sort



## 📖 Scenario: Sorting Product Weights
Imagine you are working for a logistics company that needs to **sort product weights** before shipping them. The warehouse receives products with different weights, and it is important to arrange them in **ascending order** before packaging.

Your task is to implement **Bubble Sort** and **Selection Sort** to sort a list of product weights and compare their performance.

---

## 🚀 Instructions

### 1️⃣ Implement Bubble Sort
Bubble Sort works by repeatedly swapping adjacent elements if they are in the wrong order. Implement the function to sort a list in ascending order.

**Steps:**
- Loop through the list multiple times.
- Compare adjacent elements and swap them if needed.
- Stop if no swaps occur in a full pass (list is sorted).

### 2️⃣ Implement Selection Sort
Selection Sort works by repeatedly selecting the smallest element and moving it to its correct position. Implement the function to sort a list in ascending order.

**Steps:**
- Find the smallest element in the list.
- Swap it with the first unsorted element.
- Repeat until the entire list is sorted.

### 3️⃣ Measure Sorting Performance
- Generate **two lists** of product weights:
  - A **small dataset** (50 random weights)
  - A **large dataset** (1000 random weights)
- Measure and compare the execution time of **Bubble Sort**, **Selection Sort**, and Python’s built-in `sorted()` function.

### 4️⃣ Analyze the Results
- Compare execution times for different dataset sizes.
- Which algorithm performs better for large datasets? Why?
- What are the real-world implications of using inefficient sorting methods?

---


## 🏁 Deliverables
- Your implementation of **Bubble Sort** and **Selection Sort**.
- Execution time comparison for small and large datasets.
- A short analysis of the results and conclusions.

---
### 4️⃣ -------------------------------MY PART------------------------------------------
## ⚡ Example Output
```
🔹 Small Dataset (50 elements):
✅ Bubble Sort took 0.000000 seconds.
✅ Selection Sort took 0.000000 seconds.
✅ Insetion Sort took 0.047963 seconds.
🚀 Python Built-in Sort took 0.000000 seconds.

🔹 Large Dataset (1000 elements):
⚠️ Bubble Sort took 0.111151 seconds.
✅ Selection Sort took 0.026874 seconds.
✅ Insetion Sort took 0.025510 seconds.
🚀 Python Built-in Sort took 0.000000 seconds.

🔹 solarge Dataset (10000 elements):
✅ Bubble Sort took 6.873538 seconds.
✅ Selection Sort took 2.196297 seconds.
✅ Insetion Sort took 2.654933 seconds.
🚀 Python Built-in Sort took 0.001432 seconds.

---


## 🚀 observation
- we can see that the bublle sort and selection sort are near to each other
- 
- the build in python sort have less time complexity
- Selection sort < Insetion Sort < Bubble Sort in time complexity

Thank you for reading! 🚀