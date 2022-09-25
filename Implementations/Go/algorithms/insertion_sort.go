package algorithms

// Sorts an array of integers using the insertion sort algorithm
//
// Time complexities:
// Ο(n^2), θ(n^2), Ω(n)
//
// Space complexity: Ο(1)
//
// Stable: Yes
func InsertionSort(array []int, reverse bool) {
	for i := 1; i < len(array); i++ {
		for j := i; j > 0; j-- {
			if (reverse) {
				if (array[j] > array[j-1]) {
					array[j], array[j-1] = array[j-1], array[j]
				}
			} else {
				if (array[j] < array[j-1]) {
					array[j], array[j-1] = array[j-1], array[j]
				}
			}
		}
	}
}