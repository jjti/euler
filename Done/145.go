package main

import (
	"fmt"
	"math"
	"time"
)

// Assert the value is true or panic
func Assert(expected interface{}, actual interface{}) {
	if expected != actual {
		panic(fmt.Sprintf("%v not equal to %v", expected, actual))
	}
}

// Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits.
// For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible.
// Leading zeroes are not allowed in either n or reverse(n).
// There are 120 reversible numbers below one-thousand.
// How many reversible numbers are there below one-billion (109)?

// 1. between two numbers, need two starting digits to be odd and two to be even

// Split a single int into a slice of ints
func Split(n int) []int {
	dC := int(math.Log10(float64(n))) + 1 // digit count
	digits := make([]int, dC, dC)
	for n > 0 {
		digits[dC-1] = n % 10
		n /= 10
		dC--
	}
	return digits
}

// Join the split digits back together
func Join(digs []int) int {
	num := 0
	for _, d := range digs {
		num *= 10
		num += d
	}
	return num
}

// Reverse the digits in a number
func Reverse(digs []int) int {
	num := 0
	for i, d := range digs {
		num += int(math.Pow(10, float64(i))) * d
	}
	return num
}

// find the sum of "reversible numbers"
func reversibleNums(limit int) int {
	// 0 is unknown, 1 is true, -1 is false
	valid := make([]int, limit, limit)

	for i, isValid := range valid {
		if isValid == 0 && i > 0 {
			digs := Split(i)
			last := digs[len(digs)-1]

			valid[i] = 1

			// can't end in 0
			if last == 0 {
				valid[i] = -1
				continue
			}

			rev := Reverse(digs)
			valid[rev] = 1

			// split and check for odd nums in the sum of the two
			for _, d := range Split(i + rev) {
				if d%2 == 0 {
					valid[i] = -1
					valid[rev] = -1
					break
				}
			}
		}
	}

	min := limit
	numReversible := 0
	for i, isValid := range valid {
		if isValid == 1 {
			if i < min {
				min = i
			}
			numReversible++
		}
	}
	return numReversible
}

func main() {
	Assert(len(Split(108)), 3)
	Assert(Join([]int{1, 6, 7}), 167)
	Assert(Reverse([]int{3, 4, 5}), 543)

	// 6 = 0.5, 7 = 2.55, 8 = 26, 9 =
	t := time.Now()
	for _, n := range []int{2, 3, 4, 5, 6, 7} {
		s := fmt.Sprintf("%v %v", reversibleNums(int(math.Pow10(n))), time.Since(t))
		t = time.Now()
		fmt.Println(s)
	}
}

// 20
// 120
// 720
// 720
// 18720
// 68720
// 608720
// 608720?
