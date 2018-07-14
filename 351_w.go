package main

import (
	"fmt"
	"math"
	"sync"
)

type ConTotient struct {
	sync.Mutex
	Value int
}

func (c *ConTotient) FactorDecrease(prime int) {
	c.Lock()
	defer c.Unlock()

	c.Value -= c.Value / prime
}

// assert the value is true or panic
func assert(expected interface{}, actual interface{}) {
	if expected != actual {
		panic(fmt.Sprintf("%v not equal to %v", expected, actual))
	}
}

// genPrimes is for creating a slice of primes up to the limit
func genPrimes(limit int) []int {
	pSieve := make([]bool, limit, limit)

	i := 0
	for i < limit {
		pSieve[i] = true
		i++
	}
	pSieve[0] = false
	pSieve[1] = false

	for i := 2; i < limit; i++ {
		if pSieve[i] {
			for j := i * 2; j < limit; j += i {
				pSieve[j] = false
			}
		}
	}

	primes := []int{}
	i = 0
	for i < limit {
		if pSieve[i] {
			primes = append(primes, i)
		}
		i++
	}

	return primes
}

// phiSieveGen creates phi for all values up to limi
func phiSieveGen(limit int) []int {

	primes := genPrimes(limit)

	// start := time.Now()
	phiValues := make([]ConTotient, limit, limit)
	for index := range phiValues {
		phiValues[index] = ConTotient{Value: index}
	}

	wg := &sync.WaitGroup{}
	for _, prime := range primes {
		wg.Add(1)
		go func(p int, w *sync.WaitGroup) {
			defer wg.Done()
			for j := p; j < limit; j += p {
				phiValues[j].FactorDecrease(p)
			}
		}(prime, wg)
	}

	wg.Wait()

	phis := []int{}
	for i := range phiValues {
		phis = append(phis, phiValues[i].Value)
	}
	return phis
}

// hexorchard returns the number of "hidden" coordintes in the orchard
func hexorchard(order int) int {
	phiValues := phiSieveGen(order + 1)

	hiddenCoors := 0
	for i, phi := range phiValues {
		hiddenCoors += i - phi
	}

	return hiddenCoors * 6
}

func main() {
	assert(30, hexorchard(5))
	assert(138, hexorchard(10))
	assert(1177848, hexorchard(1000))
	// 5 = 0.38, 6 = 0.6, 7 = 2.6, 8 = 29
	fmt.Println(hexorchard(int(math.Pow10(8)))) // 11762187201804552 in 29 seconds
}
