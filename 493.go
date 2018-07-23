package main

// recursively add each ball option
func drawBall(balls string, rem string, acc *[]string, targetNum int) {
	// check if we're done (have drawn all of them)
	if len(balls) == targetNum {
		*acc = append(*acc, balls)
		return
	}

	// for every remaining ball, create new balls array and keep going
	for i, ball := range rem {
		drawBall(balls, append(rem[:i], rem[i+1:]...), acc, targetNum)
	}
}

// 70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.
// What is the expected number of distinct colors in 20 randomly picked balls?
// Give your answer with nine digits after the decimal point (a.bcdefghij).

// looks like another DP problem... count up chance of each happening
// func main() {

// 	//sinitialize the balls string, with all of them
// 	in := ""
// 	for i := 0; i < 7; i++ {
// 		for j := 0; j < 10; j++ {
// 			in += strconv.Itoa(j)
// 		}
// 	}

// 	// 4 == 11.6
// }
