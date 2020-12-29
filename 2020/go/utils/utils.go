package utils

import (
	"io/ioutil"
	"log"
	"strconv"
	"strings"
	"time"
)

func ReadInput(fileName string) []string {
	return ReadInputWithDelim(fileName, "\n")
}

func ReadInputWithDelim(fileName string, delim string) []string {
	data, err := ioutil.ReadFile(fileName)
	if err != nil {
		return nil
	}

	lines := strings.Split(string(data), delim)
	var i []string
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		i = append(i, string(line))
	}
	return i
}

func ReadInputInt(fileName string) []int {
	return ReadInputIntWithDelim(fileName, "\n")
}

func ReadInputIntWithDelim(fileName string, delim string) []int {
	data, err := ioutil.ReadFile(fileName)
	if err != nil {
		return nil
	}

	lines := strings.Split(string(data), delim)
	var i []int
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}

		num, err := strconv.Atoi(line)
		if err != nil {
			return nil
		}
		i = append(i, num)
	}
	return i
}

func TimeTrack(start time.Time, name string) {
	elapsed := time.Since(start)
	log.Printf("%s took %s", name, elapsed)
}
