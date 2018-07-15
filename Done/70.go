package main

import (
	"fmt"
	"math"
	"sort"
)

// Assert the value is true or panic
func Assert(expected interface{}, actual interface{}) {
	if expected != actual {
		panic(fmt.Sprintf("%v not equal to %v", expected, actual))
	}
}

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

// Create slice of prime factors up to a target limit
func primeFactors(limit int) [][]int {
	factors := make([][]int, limit, limit)

	primeSieve := make([]bool, limit, limit)
	for i := range primeSieve {
		if i > 1 {
			primeSieve[i] = true
		}
	}

	for i, prime := range primeSieve {
		if prime {
			for j := i; j < limit; j += i {
				primeSieve[j] = false
				factors[j] = append(factors[j], i)
			}
		}
	}

	return factors
}

// create a totient array using the prime factors at each index
func totientGen(factorMap [][]int) []int {
	totients := make([]int, len(factorMap), len(factorMap))

	for i, factors := range factorMap {
		totients[i] = i // starts out equal to self
		for _, factor := range factors {
			totients[i] -= totients[i] / factor
		}
	}

	return totients
}

func arePermutations(first int, second int) bool {
	if first%9 != second%9 {
		return false
	}

	firDigs := Split(first)
	secDigs := Split(second)

	sort.Ints(firDigs)
	sort.Ints(secDigs)

	firString := fmt.Sprint(firDigs)
	secString := fmt.Sprint(secDigs)

	return firString == secString
}

// Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of
// positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8,
// are all less than nine and relatively prime to nine, φ(9)=6.
// The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
// Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
// Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

func main() {
	Assert(true, arePermutations(1890, 9810))
	Assert(false, arePermutations(198, 1980))

	primeFacts := primeFactors(int(math.Pow10(7)))
	totients := totientGen(primeFacts)

	Assert(8, totients[20])
	Assert(8, totients[30])

	minRatio := float64(math.Inf(1))
	minValue := 0
	minTotient := 0
	for i, t := range totients {
		if i == 1 {
			continue
		}

		// first check if it would be a new min, faster than string comparison
		if float64(i)/float64(t) < minRatio {
			if arePermutations(i, t) {
				minRatio = float64(i) / float64(t)
				minValue = i
				minTotient = t
			}
		}
	}

	fmt.Println(minRatio, minValue, minTotient)
}
