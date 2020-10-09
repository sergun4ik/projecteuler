package main

import (
	"fmt"
)

func get_fibonacci(x int, y int) []int {
	return make([]int, y, (x + y))
}

func main() {
	a := get_fibonacci(1, 1)
	b := make([]int, a[1], (a[0] + a[1]))
	fmt.Println(b)
}
