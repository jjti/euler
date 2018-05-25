package main

import (
	"fmt"
	"math/big"
)

/*
Powerful digit sum
Problem 56
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
*/
func main() {
	curr := new(big.Int)
	currMod := new(big.Int)
	currMax := big.NewInt(0)
	sum := new(big.Int)
	for a := 1; a < 100; a++ {
		for b := 1; b < 100; b++ {
			// set the current exponent
			curr.Exp(big.NewInt(int64(a)), big.NewInt(int64(b)), nil)
			sum.Set(big.NewInt(0))
			for {
				newMod := new(big.Int)
				curr, currMod = newMod.DivMod(curr, big.NewInt(10), currMod)
				sum.Set(sum.Add(sum, currMod))
				if curr.Cmp(big.NewInt(0)) == 0 {
					break
				}
			}
			if sum.Cmp(currMax) > 0 {
				currMax.Set(sum)
			}
		}
	}
	fmt.Println(currMax)
}
