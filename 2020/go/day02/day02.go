package main

import (
	"fmt"
	"strconv"
	"strings"
	"time"

	"github.com/stradigi-mario-bruno/advent-of-code/2020/go/utils"
)

func main() {
	input := utils.ReadInput("../../input/day02.txt")
	passwords := parse(input)
	fmt.Println(part1(passwords))
	fmt.Println(part2(passwords))
}

type password struct {
	password string
	letter   string
	min      int
	max      int
}

func parse(input []string) []password {
	passwords := []password{}
	for _, i := range input {
		split := strings.Split(i, ":")
		rule := strings.Split(split[0], " ")
		min, _ := strconv.Atoi(strings.Split(rule[0], "-")[0])
		max, _ := strconv.Atoi(strings.Split(rule[0], "-")[1])
		letter := rule[1]
		p := password{
			password: strings.TrimSpace(split[1]),
			letter:   letter,
			min:      min,
			max:      max,
		}
		passwords = append(passwords, p)
	}
	return passwords
}

func part1(input []password) int {
	defer utils.TimeTrack(time.Now(), "part1")
	nbrValid := 0
	for _, p := range input {
		count := strings.Count(p.password, p.letter)
		if count >= p.min && count <= p.max {
			nbrValid++
		}
	}
	return nbrValid
}

func part2(input []password) int {
	defer utils.TimeTrack(time.Now(), "part2")
	nbrValid := 0
	for _, p := range input {
		first := p.password[p.min-1] == p.letter[0]
		second := p.password[p.max-1] == p.letter[0]
		if first != second {
			nbrValid++
		}
	}
	return nbrValid
}
