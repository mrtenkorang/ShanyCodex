package main

import "fmt"

// Checking whether a number is odd or not by returning a true or false statement

func evenCheck(number int) bool {
	even := false
	if number%2 == 0 {
		even = true

	} else {
		even = false
	}
	return even
}

func oddCheck(number int) bool {
	odd := false
	if number%2 == 1 {
		odd = true
	}
	return odd
}

func main() {
	fmt.Println(oddCheck(4567890987))

}
