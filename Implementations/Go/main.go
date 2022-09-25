package main

import (
	"fmt"
	"time"
	"sort"
	"math/rand"
	"dsa/algorithms"
)

// GetRandomArr returns an array of random integers
// based on the size provided
func GetRandomArr(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = rand.Intn(100)
	}
	return arr
}

// Get a nearly sorted array
// with a 1/n chance of multiplying the element by 2
func GetNearlySortedArr(size int) []int {
	arr := make([]int, size)
	chances := int(size / 2)
	for i := 0; i < size; i++ {
		if (rand.Intn(chances) != 0) {
			arr[i] = i
		} else {
			arr[i] = i * 2
		}
	}
	return arr
}

// CallSortFunc calls the sorting function and prints the time taken
func CallSortFunc(sortFunc func([]int, bool), baseArr []int, arr []int, reverse bool, name string) {
	start := time.Now()
	sortFunc(arr, reverse)
	elapsed := time.Since(start)
	fmt.Println(
		fmt.Sprintf("%s: %v", name, elapsed),
	)

	// Reset the array
	copy(arr, baseArr)
}

// CallNativeSort calls Go's native sort function and prints the time taken
func CallNativeSort(baseArr []int, arr []int, reverse bool, name string) {
	start := time.Now()
	if (reverse) {
		sort.Sort(sort.Reverse(sort.IntSlice(arr)))
	} else {
		sort.Ints(arr)
	}
	elapsed := time.Since(start)
	fmt.Println(
		fmt.Sprintf("%s: %v", name, elapsed),
	)

	// Reset the array
	copy(arr, baseArr)
}

func main() {
	var size int
	fmt.Print("Enter size of array: ")
	fmt.Scan(&size)

	array := GetRandomArr(size)
	if (size < 20) {
		fmt.Println("Unsorted array: ", array)
	} else {
		arrString := ""
		for i := 0; i < 10; i++ {
			arrString += fmt.Sprintf("%d, ", array[i])
		}
		fmt.Println(
			fmt.Sprintf("Unsorted array: [%s...]", arrString),
		)
	}
	baseArray := make([]int, size) // copy of array
	copy(baseArray, array)

	// Call the sorting functions and print the time taken
	fmt.Println("\nSorting in ascending order...")
	CallNativeSort(baseArray, array, false, "Go's native sort")
	CallSortFunc(algorithms.BubbleSort, baseArray, array, false, "Bubble Sort")
	CallSortFunc(algorithms.InsertionSort, baseArray, array, false, "Insertion Sort")
}