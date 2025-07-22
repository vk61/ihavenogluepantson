# I have no glue 🤕 pants on 
For all these year, I have tried to take up on myself to solve the DSA problems on my own. I believe that the patterns used to solve the DSA problems need not be taught. it should occur to myself while solving. I learned that it is not the case and I am dumb. Here , Now I am trying learning to learn the patterns now. So this is my guide and will always come back here to refresh on these patterns. 👉


![solve_problem_gif](/img/Im-Winston-Wolf.-I-solve-problems..jpg)



# ✨ Sly thin win those 

In many problems dealing with an array (or a LinkedList), we are asked to find or calculate something among all the contiguous subarrays (or sublists) of a given size.

> [!NOTE]
> Most of the problems asks us to find the minimum, maximum subarray or string, use sliding windows pattern.
>

1. [Maximum Sum Subarray of Size K](/sly-thin-win-those/1_max-avg-sub-arr.ipynb)
2. [Smallest Subarray with a given sum](/sly-thin-win-those/2_min-sub-arr-given_sum.ipynb)
3. [Longest Substring with K Distinct Characters](/sly-thin-win-those/3_max-sub-arr-k-distinct-types.ipynb)
4. [No-repeat Substring](/sly-thin-win-those/4_max-sub-arr-only-distinct-types.ipynb)
5. [Longest Substring with Same Letters after Replacement](/sly-thin-win-those/5_max-sub-arr-only-same-type.ipynb)
6. [Permutation in a String](/sly-thin-win-those/6_anagram_of_str1_in_str2.ipynb)
7. [Smallest Window containing Substring](/sly-thin-win-those/7_min-sub-arr-containing_str1.ipynb)
8. [Words Concatenation](/sly-thin-win-those/8_substr_concat_words.ipynb)


![sliding_window_jim_carrey](/img/jim_carrey_slideing_windows.gif)

# 👩🏼‍🎨 Tube Painters  

In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain constraints, the two pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a subarray. 👁️
1. [Pair with Target Sum aka "Two Sum" | two-sum-ii-input-array-is-sorted ](./tube-painters/1_two_sum.ipynb)
2. [Remove Duplicates](./tube-painters/2_remove_duplucates.ipynb)
3. [Squaring a sorted array](./tube-painters/3_squares_of_sorted_arr.ipynb)
4. [Three sum](./tube-painters/4_three_sum.ipynb)
5. [Sub arrays less than product](./tube-painters/5_sub_arr_less_than_product.ipynb)
6. [Dutch National Flag](./tube-painters/6_dutch_national_flag.ipynb)
7. [Four sum](./tube-painters//7_four_sum.ipynb)
8. [Backspace string compare](./tube-painters/8_backspace_str_cmp.ipynb)
9. [minimum wndow sort](./tube-painters/9_min_window_sort.ipynb)

![finger_gun_office](/img/finger_gun_office.gif)

# Pasta and Slow sauce Pointers ♨️

The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

1. [Linked List cycle](./pasta-n-slow-sauce-pointers/1_linked_list_cycle.ipynb)
2. [Happy Number](./pasta-n-slow-sauce-pointers//2_happy_number.ipynb)
3. [Middle of Linked List](./pasta-n-slow-sauce-pointers//3_mid_linked_list.ipynb)
4. [Palindrome Linked List](./pasta-n-slow-sauce-pointers//4_palindrome_linked_list.ipynb)
5. [Rearrange Linked List](./pasta-n-slow-sauce-pointers//5_rearrange_linked_list.ipynb)
6. [Cycle in Circular Array](./pasta-n-slow-sauce-pointers//6_cycle_in_circular_arr.ipynb)

![pasta](/img//pasta.gif)

# Merge Intervals ❤️‍🩹
This pattern describes an efficient technique to deal with overlapping intervals. In a lot of problems involving intervals, we either need to find overlapping intervals or merge intervals if they overlap.

Given two intervals (a and b), there will be six different ways the two intervals can relate to each other:

> 1. __a and b do not overlap__
> 2. __a and b overlap, b ends after a__
> 3. __a completely overlaps b__
> 4. __a and b overlap, a ends after b__
> 5. __b completly overlaps a__
> 6. __a and b do not overlap__

![merge](./img/mergeintervals.png)

1. [Merge Intervals](./merge_intervals/1_merge_intervals.ipynb)
2. [Insert Intervals](./merge_intervals/2_insert_interval.ipynb)
3. [Interval Intersection](./merge_intervals/3_interval_intersections.ipynb)
4. [Conflicting Appointments](./merge_intervals/4_conflicting_appointments.ipynb)
5. [Meeting Rooms](./merge_intervals/5_min_meeting_rooms.ipynb)
6. [Car Polling](./merge_intervals/6_car_pooling.ipynb)

![gudbye mike](./img/gudbye_mike.gif)

# Cyclic Sort 🚵

This pattern describes an interesting approach to deal with problems involving arrays containing numbers in a given range.

For example, take the following problem:
You are given an unsorted array containing numbers taken from the range 1 to n The array can have duplicates, which means that some numbers will be missing. Find all the missing numbers.

To efficiently solve this problem, we can use the fact that the input array contains numbers in the range of 1 to n. For example, to efficiently sort the array, we can try placing each number in its correct place, i.e., placing 1 at index 0, placing 2 at index 1, and so on. Once we are done with the sorting, we can iterate the array to find all indices that are missing the correct numbers. These will be our required numbers.

![cycl mrbean](./img//mr-bean-bean.gif)

1. [Cyclic Sort](./cyclic_sort/cyclic_sort.ipynb)
2. [Duplicate Number](./cyclic_sort/duplicate_number.ipynb)
3. [Find smallest missing number](./cyclic_sort/find_smallest_missing_number.ipynb)
4. [Missing Number](./cyclic_sort/missing_number.ipynb)


# In-place Reversal of a LinkedList
In a lot of problems, we are asked to reverse the links between a set of nodes of a LinkedList. Often, the constraint is that we need to do this in-place, i.e., using the existing node objects and without using extra memory.

1. [Reverse a Linked list](./linked_list_reversal/reverse_linked_list.ipynb)