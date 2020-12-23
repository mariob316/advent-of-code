package main

import (
	"fmt"

	"github.com/stradigi-mario-bruno/advent-of-code/2020/go/utils"
)

func main() {
	input := inputMap(utils.ReadInputInt("../../input/day01.txt"))
	fmt.Println(part1(input))
	fmt.Println(part2(input))
}

func part1(input map[int]bool) int {
	for i := range input {
		x := 2020 - i
		if input[x] {
			return i * (2020 - i)
		}
	}
	return 0
}

func part2(input map[int]bool) int {
	for i := range input {
		for j := range input {
			x := 2020 - i - j
			if input[x] {
				return i * j * (2020 - i - j)
			}
		}
	}
	return 0
}

// go doesn't have `in` array without needing to loop  manually...
// so to speed things up i put it in a map to have quicker lookup
// In this case it prob doesn't help since i need to loop again to create the map
// but i wanted the code as similar to the python code
func inputMap(input []int) map[int]bool {
	x := make(map[int]bool)
	for _, num := range input {
		x[num] = true
	}
	return x
}
