package sorting_algorithms

// Sorts an array of integers using the selection sort algorithm
//
// Time complexities:
// Ο(n^2), θ(n^2), Ω(n^2)
//
// Space complexity: Ο(1)
//
// Stable: No
func SelectionSort(array []int, reverse bool) {
	for i := 0; i < len(array); i++ {
		idx := i // initialise index of
				 // smallest or largest element based on reverse
		for j := i + 1; j < len(array); j++ {
			if (reverse) {
				if (array[j] > array[idx]) {
					idx = j
				}
			} else {
				if (array[j] < array[idx]) {
					idx = j
				}
			}
		}
		if (idx != i) {
			array[i], array[idx] = array[idx], array[i]
		}
	}
}