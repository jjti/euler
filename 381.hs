{-

For a prime p let S(p) = (∑(p-k)!) mod(p) for 1 ≤ k ≤ 5.

For example, if p=7,
(7-1)! + (7-2)! + (7-3)! + (7-4)! + (7-5)! = 6! + 5! + 4! + 3! + 2! = 720+120+24+6+2 = 872.
As 872 mod(7) = 4, S(7) = 4.

It can be verified that ∑S(p) = 480 for 5 ≤ p < 100.

Find ∑S(p) for 5 ≤ p < 10**8.

-}

factorial :: Integer -> Integer -- get the factorial at
factorial n = product [1..n]

functionS :: Integer -> Integer -- (∑(p-k)!)
functionS n = descFactorial 5 `mod` n
    where
    descFactorial 1 = factorial (n - 1)
    descFactorial x = descFactorial (x - 1) + factorial (n - x)

primesTo :: Integer -> [Integer] -- create the prime list up to the limit
primesTo limit = 2 : erathnos [3,5..limit]
    where
    erathnos [] = []
    erathnos (x:xs) = x : erathnos [y | y <- xs, y `mod` x /= 0]

primesFiveTo :: Integer -> [Integer] -- get all primes greater than or equal to 5
primesFiveTo limit = filter (>= 5) (primesTo limit)

summedSTo :: Integer -> Integer -- ∑S(p)
summedSTo limit =
    let primesList     = primesFiveTo limit
    in sum (map functionS primesList)

main = print (zip primes (map functionS primes))
    where primes = primesTo 60
