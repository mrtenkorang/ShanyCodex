// Even Check, finding whether a number is even or not 

package main

import "fmt"

func evenCheck(number int) bool {
	even := false
	if number%2 == 0 {
		even = true

	} else {
		even = false
	}
	return even
}

func main() {
	fmt.Println(evenCheck(4567890987))

}

