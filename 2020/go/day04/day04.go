package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
	"time"

	"github.com/stradigi-mario-bruno/advent-of-code/2020/go/utils"
)

type Passports map[string]string

func main() {
	input := utils.ReadInputWithDelim("../../input/day04.txt", "\n\n")
	p := parsePassport(input)
	fmt.Println(part1(p))
	fmt.Println(part2(p))
}

func part1(input []Passports) int {
	defer utils.TimeTrack(time.Now(), "part1")
	nbrValid := 0
	for _, passportMap := range input {
		if passportHasField(passportMap) {
			nbrValid++
		}
	}
	return nbrValid
}

func part2(input []Passports) int {
	defer utils.TimeTrack(time.Now(), "part2")
	nbrValid := 0
	for _, passportMap := range input {
		if passportHasValidField(passportMap) {
			nbrValid++
		}
	}
	return nbrValid
}

func passportHasField(passport Passports) bool {
	for _, field := range []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} {
		_, exist := passport[field]
		if !exist {
			return false
		}
	}
	return true
}

func passportHasValidField(passport Passports) bool {
	if !passportHasField(passport) {
		return false
	}

	for _, field := range []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} {
		value, _ := passport[field]
		hgtMap := map[string][]int{"cm": {150, 193}, "in": {59, 76}}
		switch field {
		case "byr":
			num, _ := strconv.Atoi(value)
			if num < 1920 || num > 2002 {
				return false
			}
		case "iyr":
			num, _ := strconv.Atoi(value)
			if num < 2010 || num > 2020 {
				return false
			}
		case "eyr":
			num, _ := strconv.Atoi(value)
			if num < 2020 || num > 2030 {
				return false
			}
		case "hgt":
			conv := value[len(value)-2:]
			if conv != "cm" && conv != "in" {
				return false
			}

			nb, _ := strconv.Atoi(value[:len(value)-2])
			if nb < hgtMap[conv][0] || nb > hgtMap[conv][1] {
				return false
			}
		case "hcl":
			if !regexp.MustCompile(`^#[0-9a-f]{6}$`).MatchString(value) {
				return false
			}
		case "ecl":
			count := 0
			switch value {
			case "amb", "blu", "brn", "gry", "grn", "hzl", "oth":
				count++
			}
			if count == 0 {
				return false
			}
		case "pid":
			if !regexp.MustCompile(`^[0-9]{9}$`).MatchString(value) {
				return false
			}
		}
	}
	return true
}

func parsePassport(input []string) []Passports {
	var passports []Passports

	for i, p := range input {
		passports = append(passports, make(map[string]string))
		for _, pass := range strings.Split(p, "\n") {
			for _, line := range strings.Split(pass, " ") {
				tmp := strings.Split(line, ":")
				passports[i][tmp[0]] = tmp[1]
			}
		}
	}
	return passports
}
