Permutation algorithm
=======
Next permutation is a process that rearranges numbers into the lexicographically next greater permutation of numbers. After several submissions and the clear and beautiful explanation in [Project Nayuki!](https://www.nayuki.io/page/next-lexicographical-permutation-algorithm), I think I've completely understood this algorithm. Here is my thoughts (may have some repeat thoughts with Nayuki's). Also use the example and image in Nayuki's post.
<img src="https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/next-permutation-algorithm.svg" alt="next permutation example" width="350"/>

## Algorithms
The key idea is to find out the pivot in the array that before the subarray at left of the pivot is non-decreasing while the subarray at right of the is non-increasing. That pivot is the number you need to change for next permutation. So the algorithm includes the following three steps:

1. Find the pivot. Search from the end of the list, and find the longest non-increasing suffix. That means the highest permutation of that suffix. You can't do anything with that suffix to get the next permutation. Then you need to work with the pivot (left of the suffix).

2. Switch the pivot and an element in suffix. According to the process of generating next suffix, the next element which should be put in the pivot is the one which is just greater than the pivot. In this case, 3. In my submissions, I made some mistakes here (switch the pivot with the smallest element). So search from the end, and switch the first element which is greater than pivot.

3. Rearrange the suffix. Because we switch the pivot, we need to make the suffix lowest again. Here, Nayuki used a very smart method, which just reverse the suffix because the suffix is non-decreasing. And this can be done in place.


## Previous Permutation
The process of finding previous permutation is similar to next permutation. Just search from start to find out the longest non-decreasing suffix, and switch pivot with the value in suffix which is just smaller than the pivot. At last reverse the the suffix. 

## Generate Permutation
We can generate the permutation by generating next permutation one by one. May take advantage of some information from previous step. 
