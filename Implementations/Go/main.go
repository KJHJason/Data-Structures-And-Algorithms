package main

import (
	"os"
	"fmt"
	"time"
	"sort"
	"math/rand"
	"dsa/algorithms/sort"
	"github.com/fatih/color"
	"github.com/jedib0t/go-pretty/v6/table"
	"github.com/jedib0t/go-pretty/v6/text"
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

// Check if the array is sorted
func CheckArrIsSorted(arr []int, name string, timeTaken time.Duration, t table.Writer) {
	isSorted := true
	result := "✓"
	for i := 0; i < len(arr) - 1; i++ {
		if (arr[i] > arr[i + 1]) {
			isSorted = false
			result = "✗"
			break
		}
	}

	var tableRow []interface{} 
	if (isSorted) {
		// print the result with green color
		tableRow = table.Row{
			color.GreenString(name), 
			color.GreenString(timeTaken.String()),
			color.GreenString(result), 
		}
	} else {
		// print the result with red color
		tableRow = table.Row{
			color.RedString(name), 
			color.RedString(timeTaken.String()),
			color.RedString(result), 
		}
	}
	t.AppendRow(tableRow)
}

// CallSortFunc calls the sorting function and prints the time taken
func CallSortFunc(sortFunc func([]int, bool), arr []int, reverse bool, name string, t table.Writer) {
	arrCopy := make([]int, len(arr))
	copy(arrCopy, arr)

	start := time.Now()
	sortFunc(arrCopy, reverse)
	elapsed := time.Since(start)
	CheckArrIsSorted(arrCopy, name, elapsed, t)
}

// CallNativeSort calls Go's native sort function and prints the time taken
func CallNativeSort(arr []int, reverse bool, t table.Writer) {
	arrCopy := make([]int, len(arr))
	copy(arrCopy, arr)

	start := time.Now()
	if (reverse) {
		sort.Sort(sort.Reverse(sort.IntSlice(arrCopy)))
	} else {
		sort.Ints(arrCopy)
	}
	elapsed := time.Since(start)
	CheckArrIsSorted(arrCopy, "Go's Native Sort (pdqs)", elapsed, t)
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
		fmt.Printf("Unsorted array: [%s...]\n", arrString)
	}

	t := table.NewWriter()
	t.SetOutputMirror(os.Stdout)
	t.AppendHeader(table.Row{"Algorithm", "Time Taken", "Sorted?"})
	t.SetColumnConfigs([]table.ColumnConfig{
		{Number: 1, Align: text.AlignLeft, AlignHeader: text.AlignCenter},
		{Number: 2, Align: text.AlignCenter, AlignHeader: text.AlignCenter},
		{Number: 3, Align: text.AlignCenter, AlignHeader: text.AlignCenter},
	})

	// Call the sorting functions and print the time taken
	fmt.Println("\nSorting in ascending order...")
	CallNativeSort(array, false, t)
	CallSortFunc(sorting_algorithms.BubbleSort, array, false, "Bubble Sort", t)
	CallSortFunc(sorting_algorithms.InsertionSort, array, false, "Insertion Sort", t)
	CallSortFunc(sorting_algorithms.SelectionSort, array, false, "Selection Sort", t)
	t.Render()
}