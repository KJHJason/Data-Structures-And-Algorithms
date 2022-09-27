package sorting_algorithms

// Sorts an array of integers using the bubble sort algorithm
//
// Time complexities:
// Ο(n^2), θ(n^2), Ω(n)
//
// Space complexity: Ο(1)
//
// Stable: Yes
func BubbleSort(array []int, reverse bool) {
	for i := 0; i < len(array); i++ {
		for j := 0; j < len(array)-1; j++ {
			if (reverse) {
				if (array[j] < array[j+1]) {
					array[j], array[j+1] = array[j+1], array[j]
				}
			} else {
				if (array[j] > array[j+1]) {
					array[j], array[j+1] = array[j+1], array[j]
				}
			}
		}
	}
}