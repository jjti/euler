package main

import (
	"fmt"
)

func buildChanceMap(diceCount int, maxDiceVal int) map[int]int {
	outcomes := []int{0}
	for diceCount > 0 {
		newOutcomes := []int{}
		for _, val := range outcomes {
			i := maxDiceVal
			for i > 0 {
				newOutcomes = append(newOutcomes, i+val)
				i--
			}
		}
		outcomes = newOutcomes
		diceCount--
	}

	outcomesMap := make(map[int]int)
	for _, outcome := range outcomes {
		outcomesMap[outcome]++
	}
	return outcomesMap
}

// Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
// Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
// Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.
// What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg

// Notes: looks like a dynamic programming algo, count up all possibilities 4 ** 9 and 6 ** 6, and their possible outcomes
// Then find the ratio of Pete's outcomes that exceed Colin's outcome
func main() {
	// fmt.Println(buildChanceMap(3, 6))

	peterOutcomes := buildChanceMap(9, 4)
	colinOutcomes := buildChanceMap(6, 6)

	peterTotal := 0
	for _, count := range peterOutcomes {
		peterTotal += count
	}

	colinTotal := 0
	for _, count := range colinOutcomes {
		colinTotal += count
	}

	peterWins := 0.0
	// peter dice total, peter dice total count
	for pT, pTC := range peterOutcomes {

		// colin dice total, colin dice total count
		winsAgainst := 0.0
		for cT, cTC := range colinOutcomes {
			if pT > cT {
				winsAgainst += float64(cTC)
			}
		}
		winRatio := winsAgainst / float64(colinTotal)
		handRatio := float64(pTC) / float64(peterTotal)
		peterWins += winRatio * handRatio
	}

	fmt.Println(peterWins) // round and include a zero at the start
}
