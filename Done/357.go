package main

import (
	"fmt"
	"math"
	"runtime"
	"sync"
)

type ConcNum struct {
	sync.Mutex
	Value    int
	Valid    bool
	Divisors []int
}

func (c *ConcNum) CheckIfValidDivisor(d int, primeSet map[int]bool, wg *sync.WaitGroup) {
	c.Lock()
	defer c.Unlock()
	defer wg.Done()

	for n := d; n <= int(math.Pow(float64(c.Value), 0.5)); n += d {
		if c.Value%n == 0 {
			// c.Divisors = append(c.Divisors, n)
			_, isPrime := primeSet[n+c.Value/n]
			if !isPrime {
				c.Valid = false
				return
			}
		}
	}
}

// genPrimes is for creating a slice of primes up to the limit
func genPrimes(limit int) []int {
	pSieve := make([]bool, limit, limit)

	for i := range pSieve {
		pSieve[i] = true
	}

	for i := 2; i < limit; i++ {
		if pSieve[i] {
			for j := i * 2; j < limit; j += i {
				pSieve[j] = false
			}
		}
	}

	primes := []int{}
	for i, isPrime := range pSieve {
		if i > 1 && isPrime {
			primes = append(primes, i)
		}
	}

	return primes
}

// primeGeneratingPairsSum is the solution func
func primeGeneratingPairsSum(limit int) int {
	primes := genPrimes(limit)
	primeSet := make(map[int]bool)

	for _, prime := range primes {
		primeSet[prime] = true
	}

	primeGenerators := make([]ConcNum, limit, limit)
	for i := range primeGenerators {
		primeGenerators[i].Valid = false
		primeGenerators[i].Value = i
	}

	for _, prime := range primes {
		primeGenerators[prime-1].Valid = true // note 2
	}

	wg := &sync.WaitGroup{}
	for _, prime := range primes {
		wg.Add(1)
		go func(p int) {
			defer wg.Done()
			for j := p; j < limit; j += p {
				if primeGenerators[j].Valid {
					wg.Add(1)
					go primeGenerators[j].CheckIfValidDivisor(p, primeSet, wg)
				}
			}
		}(prime)
	}
	wg.Wait()

	sum := 0
	for i := range primeGenerators {
		if primeGenerators[i].Valid {
			// fmt.Println(primeGenerators[i].Value, primeGenerators[i].Divisors)
			sum += primeGenerators[i].Value
		}
	}
	return sum
}

// Consider the divisors of 30: 1,2,3,5,6,10,15,30.
// It can be seen that for every divisor d of 30, d+30/d is prime.

// Find the sum of all positive integers n not exceeding 100 000 000
// such that for every divisor d of n, d+n/d is prime.

// Notes:
// 1. Only even integers. Any odd integer + 1 won't be prime
// 2. Relatedly, can filter on only number one less than a prime, since
// 	the num divided by itself == 1, so n+1 needs to be prime
// 3. Add one to the sum
func main() {
	fmt.Println(fmt.Sprintf("former processors: %v \n", runtime.GOMAXPROCS(runtime.NumCPU())))

	// 6 = 0.676, 7 = 2.754, 8 = 88
	fmt.Println(primeGeneratingPairsSum(int(math.Pow10(8))))
}
