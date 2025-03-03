# 📌 Sorting Algorithms Exercise: Bubble Sort & Selection Sort

## 📝 Objective
In this exercise, you will implement and compare two fundamental sorting algorithms: **Bubble Sort** and **Selection Sort**. You will also measure their execution time to understand their efficiency on different dataset sizes.

## 🏆 Learning Outcomes
By completing this exercise, you will:
- Understand the working principles of **Bubble Sort** and **Selection Sort**.
- Implement sorting algorithms from scratch.
- Compare the efficiency of sorting algorithms using execution time.
- Apply sorting concepts to a real-world scenario.

---

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

## ⚡ Example Output
```
🔹 Small Dataset (50 product weights):
✅ Bubble Sort took 0.000245 seconds.
✅ Selection Sort took 0.000197 seconds.

🔹 Large Dataset (1000 product weights):
⚠️ Bubble Sort took 0.129456 seconds.
✅ Selection Sort took 0.078943 seconds.
🚀 Python Built-in Sort took 0.000032 seconds.
```

---

## 🏁 Deliverables
- Your implementation of **Bubble Sort** and **Selection Sort**.
- Execution time comparison for small and large datasets.
- A short analysis of the results and conclusions.

---

## 📌 Tips
- Focus on understanding the sorting logic before implementing it.
- Use **comments** to explain each step in your code.
- Compare the results carefully to draw meaningful conclusions.
- Think about where these sorting algorithms might be useful in real-world applications.

Good luck and happy coding! 🚀