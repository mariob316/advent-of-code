package main

import (
	"fmt"
	"time"

	"github.com/stradigi-mario-bruno/advent-of-code/2020/go/utils"
)

func main() {
	input := utils.ReadInput("../../input/day03.txt")
	fmt.Println(part1(input))
	fmt.Println(part2(input))
}

func part1(input []string) int {
	defer utils.TimeTrack(time.Now(), "part1")
	width := len(input[0])
	x := 0
	nbrTrees := 0
	for _, p := range input {
		if p[x] == '#' {
			nbrTrees++
		}
		x = (x + 3) % width
	}
	return nbrTrees
}

func part2(input []string) int {
	defer utils.TimeTrack(time.Now(), "part2")
	slopes := [][]int{{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}}
	width := len(input[0])
	total := 1
	for _, slope := range slopes {
		nbrTrees := 0
		x := 0
		y := 0
		for y < len(input) {
			if input[y][x] == '#' {
				nbrTrees++
			}
			x = (x + slope[0]) % width
			y += slope[1]
		}
		total *= nbrTrees
	}
	return total
}
