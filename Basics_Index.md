# 🔤 DSA Basics

These notes cover the basics of **Data Structures & Algorithms**, starting with a classic problem, based on the 2019 lecture videos.

---

## 🚩 Problem 1: Running Median

> **Problem Statement:**  
> Given a stream of integers, **calculate the median** every time a new integer is received from the stream.

---

## 💡 Brute Force Approach

- **Method:**  
  Keep inserting each number into an array and sort the array after every insertion.

- **Time Complexity:**
  - Sorting: `O(n * log n)`
  - Finding median: `O(1)`

- **Alternative:**  
  Use **Insertion Sort** instead of full sorting to place each new number in its correct position.
  - Complexity: `O(n)` for each insertion

---

## ⚙️ Efficient Solution: Using Heaps

To improve performance, we use two heaps:

### 1. **Max Heap**  
- Keeps track of the **smaller half** of the numbers  
- Allows access to the maximum of the lower half in `O(1)`  
- Insertion and deletion in `O(log n)`

### 2. **Min Heap**  
- Keeps track of the **larger half** of the numbers  
- Allows access to the minimum of the upper half in `O(1)`  
- Insertion and deletion in `O(log n)`

> By balancing both heaps correctly, the **median** can be calculated in `O(1)` time after each insertion.

---

### 📊 Heap Structure Illustration

![min_heap_max_heap](/img/max-heap-min-heap.png)

---

## ⏱️ Final Time Complexity

| Operation         | Time Complexity |
|------------------|------------------|
| Insertion         | `O(log n)`       |
| Get Median        | `O(1)`           |

---

## 📌 Notes

- Use a **max heap** to keep track of the **lower half**
- Use a **min heap** to keep track of the **upper half**
- Make sure the size difference between the heaps is at most `1`
- If sizes are equal, median is average of both heap tops
- If one heap is larger, the median is the top of that heap

---

