package main

import "fmt"

/*
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
*/

/*
Strategy is create to a map between each number (int) and whether it reaches 89 (as opposed to 1)

So for each test case, first refer to cache and pull results if it already exists but, if it
doesn't, save each step along the way to determining whether it reaches 1 or 89, then update
all of the previous values once it's known which number it converges on
*/
func main() {
	CACHE := make(map[int]bool)
	CACHE[89] = true
	CACHE[1] = false

	// loop over every index from 1 to 10M
	for i := 1; i < 10000000; i++ {

		// start storing all tested values
		tested := []int{}
		j := i
		for {
			tested = append(tested, j)

			// has this been seen before
			val, defined := CACHE[j]
			if defined {
				// update all the values that were tested
				for _, t := range tested {
					CACHE[t] = val
				}
				break
			} else {
				// square digits and try again
				j = squareDigits(j)
			}
		}
	}

	sum := 0
	for k := range CACHE {
		if CACHE[k] {
			sum++
		}
	}
	fmt.Println(sum)
}

/*
split a number, n, into a slice of integers for each of its digits
*/
func split(n int) []int {
	digits := []int{}
	for {
		d := n % 10
		digits = append([]int{d}, digits...)
		n /= 10
		if n == 0 {
			break
		}
	}
	return digits
}

/*
squareDigits, ie, return the sum of the square of every digit in the number (using split)
*/
func squareDigits(n int) int {
	s := split(n)

	sum := 0
	for _, m := range s {
		sum += m * m
	}
	return sum
}
